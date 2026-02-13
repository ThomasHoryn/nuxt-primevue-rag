const vscode = require("vscode");
const { exec } = require("child_process");
const path = require("path");
const { promisify } = require("util");
const execAsync = promisify(exec);

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  console.log("RAG Copilot Helper is now active!");

  // Quick query command (main one)
  let queryCommand = vscode.commands.registerCommand(
    "rag-copilot.query",
    async function () {
      await runRAGQuery();
    },
  );

  // Specific database commands
  let queryPrimeVueCommand = vscode.commands.registerCommand(
    "rag-copilot.queryPrimeVue",
    async function () {
      await runRAGQuery("primevue");
    },
  );

  let queryNuxtCommand = vscode.commands.registerCommand(
    "rag-copilot.queryNuxt",
    async function () {
      await runRAGQuery("nuxt");
    },
  );

  let queryBothCommand = vscode.commands.registerCommand(
    "rag-copilot.queryBoth",
    async function () {
      await runRAGQuery("both");
    },
  );

  context.subscriptions.push(
    queryCommand,
    queryPrimeVueCommand,
    queryNuxtCommand,
    queryBothCommand,
  );
}

async function runRAGQuery(predefinedDb = null) {
  try {
    // Get configuration
    const config = vscode.workspace.getConfiguration("ragCopilot");
    const pythonPath = config.get("pythonPath", "python3");
    const ragPath = config.get("ragPath", "${workspaceFolder}/RAG");
    const autoOpenCopilot = config.get("autoOpenCopilot", true);
    const autoCopyClipboard = config.get("autoCopyClipboard", true);

    // Resolve workspace folder
    const workspaceFolder = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (!workspaceFolder) {
      vscode.window.showErrorMessage("No workspace folder open!");
      return;
    }

    const resolvedRagPath = ragPath.replace(
      "${workspaceFolder}",
      workspaceFolder,
    );

    // Get question from user
    const question = await vscode.window.showInputBox({
      prompt: "What do you want to ask about Nuxt/PrimeVue?",
      placeHolder: "e.g., How to use DataTable in PrimeVue?",
      ignoreFocusOut: true,
    });

    if (!question) {
      return; // User cancelled
    }

    // Get database selection (if not predefined)
    let db = predefinedDb;
    if (!db) {
      const dbChoice = await vscode.window.showQuickPick(
        [
          { label: "📘 Both (Nuxt + PrimeVue)", value: "both" },
          { label: "🎨 PrimeVue Only", value: "primevue" },
          { label: "⚡ Nuxt Only", value: "nuxt" },
        ],
        {
          placeHolder: "Select documentation source",
          ignoreFocusOut: true,
        },
      );

      if (!dbChoice) {
        return; // User cancelled
      }

      db = dbChoice.value;
    }

    // Show progress
    await vscode.window.withProgress(
      {
        location: vscode.ProgressLocation.Notification,
        title: `Querying ${db} documentation...`,
        cancellable: false,
      },
      async (progress) => {
        progress.report({
          increment: 30,
          message: "Loading vector database...",
        });

        // Run Python script
        const scriptPath = path.join(resolvedRagPath, "quick_query.py");
        const command = `cd "${resolvedRagPath}" && "${pythonPath}" quick_query.py "${question.replace(/"/g, '\\"')}" --db ${db}`;

        try {
          progress.report({
            increment: 40,
            message: "Generating RAG prompt...",
          });

          const { stdout, stderr } = await execAsync(command, {
            maxBuffer: 10 * 1024 * 1024, // 10MB buffer
          });

          // Extract prompt between === markers
          const promptMatch = stdout.match(/={80}\n([\s\S]+?)\n={80}/);
          if (!promptMatch) {
            throw new Error("Could not extract prompt from output");
          }

          const prompt = promptMatch[1].trim();

          progress.report({ increment: 20, message: "Processing result..." });

          // Copy to clipboard if enabled
          if (autoCopyClipboard) {
            await vscode.env.clipboard.writeText(prompt);
          }

          // Show result in new document
          const doc = await vscode.workspace.openTextDocument({
            content: prompt,
            language: "markdown",
          });
          await vscode.window.showTextDocument(doc, {
            preview: false,
            viewColumn: vscode.ViewColumn.Beside,
          });

          progress.report({ increment: 10, message: "Done!" });

          // Show success message
          const action = autoCopyClipboard
            ? "Prompt generated and copied to clipboard!"
            : "Prompt generated!";

          const selection = await vscode.window.showInformationMessage(
            `✅ ${action}`,
            "Open Copilot Chat",
            "Copy Again",
          );

          if (
            selection === "Open Copilot Chat" ||
            (selection === undefined && autoOpenCopilot)
          ) {
            // Open GitHub Copilot Chat
            await vscode.commands.executeCommand("workbench.action.chat.open");
          } else if (selection === "Copy Again") {
            await vscode.env.clipboard.writeText(prompt);
            vscode.window.showInformationMessage("Copied to clipboard!");
          }
        } catch (error) {
          throw new Error(
            `Python script error: ${error.message}\n${error.stderr || ""}`,
          );
        }
      },
    );
  } catch (error) {
    vscode.window.showErrorMessage(`RAG Query failed: ${error.message}`);
    console.error("RAG Query error:", error);
  }
}

function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
