# 🚀 Quick Start Guide - Automation Edition

## 🎯 Goal

This guide shows **3 ways** to automate the RAG workflow for maximum DX (Developer Experience).

## 📦 Automation options

### 🥇 Option 1: VSCode Extension (BEST DX!)

**Setup time:** 5 minutes
**DX Level:** 🔥🔥🔥🔥🔥 (10/10)

#### Installation:

```bash
# 1. Navigate to extension folder
cd /home/tom/development/nuxt-primevue-rag/.vscode-extension

# 2. Install dependencies
npm install

# 3. (Optional) Install vsce for packaging
npm install -g @vscode/vsce

# 4. (Optional) Package extension
vsce package

# 5. Install extension
code --install-extension rag-copilot-helper-1.0.0.vsix
```

**OR development mode:**

```bash
# 1. Open .vscode-extension folder in VSCode
code /home/tom/development/nuxt-primevue-rag/.vscode-extension

# 2. Press F5 - opens Extension Development Host
# 3. Extension will be active in the new window!
```

#### Usage:

1. **Press `Ctrl+Shift+R`**
2. Type your question: "How to use DataTable in PrimeVue?"
3. Select source (Both/PrimeVue/Nuxt)
4. ✨ **DONE!** Prompt is in editor + clipboard
5. Click "Open Copilot Chat" or `Ctrl+Alt+I`
6. Paste (Ctrl+V) and get code! 🎉

**Configuration** (VSCode Settings):

```json
{
  "ragCopilot.pythonPath": "python3",
  "ragCopilot.ragPath": "${workspaceFolder}/RAG",
  "ragCopilot.autoOpenCopilot": true,
  "ragCopilot.autoCopyClipboard": true
}
```

---

### 🥈 Option 2: VSCode Tasks + Keybindings (Fast)

**Setup time:** 1 minute (already configured!)
**DX Level:** 🔥🔥🔥🔥 (8/10)

Tasks and keybindings are already in `.vscode/tasks.json` and `.vscode/keybindings.json`.

#### Usage:

**Method 1: Keybindings**

- `Ctrl+Shift+R Q` - Quick Query (with prompt)
- `Ctrl+Shift+R P` - Query PrimeVue
- `Ctrl+Shift+R N` - Query Nuxt
- `Ctrl+Shift+R B` - Query Both

**Method 2: Command Palette**

1. `Ctrl+Shift+P`
2. Type: "Tasks: Run Task"
3. Select: "RAG: Quick Query"
4. Type your question in the prompt
5. Select database (primevue/nuxt/both)

**Method 3: Terminal Menu**

1. Menu: `Terminal > Run Task...`
2. Select task

---

### 🥉 Option 3: Python CLI Script (Programmatic)

**Setup time:** 0 minutes (already ready!)
**DX Level:** 🔥🔥🔥 (7/10)

Use `quick_query.py` directly from terminal.

#### Usage:

```bash
cd RAG

# Basic query
python3 quick_query.py "How to use DataTable?" --db primevue

# Query with both databases
python3 quick_query.py "useFetch with DataTable" --db both

# Query Nuxt only
python3 quick_query.py "useState in Nuxt 3" --db nuxt

# With auto-copy to clipboard (requires xclip/xsel)
python3 quick_query.py "Your question" --db both --copy
```

**Parameters:**

- `question` - Your question (required)
- `--db` - Source: `primevue`, `nuxt`, `both` (default: `both`)
- `--copy` - Auto-copy to clipboard (requires `xclip` or `xsel`)

**Install xclip (for --copy):**

```bash
sudo apt install xclip
# OR
sudo apt install xsel
```

---

## 📊 Method comparison

| Method              | Setup | Clicks | Time | DX Score         |
| ------------------- | ----- | ------ | ---- | ---------------- |
| VSCode Extension    | 5 min | 3      | 3s   | 🔥🔥🔥🔥🔥 10/10 |
| Tasks + Keybindings | 0 min | 4      | 5s   | 🔥🔥🔥🔥 8/10    |
| Python CLI          | 0 min | 0      | 2s   | 🔥🔥🔥 7/10      |

## 🎬 Complete workflow (Extension)

```
👨‍💻 You: "I need DataTable with sorting"
      ↓ [Ctrl+Shift+R]
🤖 Extension: "What do you want to ask?"
      ↓ [type your question]
🤖 Extension: "Select documentation source"
      ↓ [select "Both"]
📚 RAG: [loads databases, searches fragments]
      ↓ [1-2 seconds]
📝 VSCode: [opens prompt in editor]
📋 Clipboard: [prompt already copied]
      ↓ [click "Open Copilot Chat"]
💬 Copilot Chat: [opens]
      ↓ [Ctrl+V to paste]
🧠 Copilot: [analyzes 7-14 fragments]
      ↓ [2-3 seconds]
✅ Copilot: [generates code ZERO hallucination]
      ↓ [copy code]
🎉 DONE! Feature ready!
```

**Total time: < 10 seconds from idea to code! ⚡**

## 🔥 Pro Tips

### Tip 1: Use Extension in development mode

If you want to modify the extension:

```bash
cd .vscode-extension
code .
# Press F5 - opens Extension Development Host
# You can debug and live-reload changes!
```

### Tip 2: Aliases for CLI

Add to `~/.bashrc` or `~/.zshrc`:

```bash
alias rag='python3 /home/tom/development/nuxt-primevue-rag/RAG/quick_query.py'
alias ragp='rag --db primevue'
alias ragn='rag --db nuxt'
alias ragb='rag --db both'
```

Usage:

```bash
ragp "How to use DataTable?"
ragn "useState in Nuxt 3"
ragb "useFetch with DataTable"
```

### Tip 3: VS Code Task in terminal

```bash
# Quick access through VSCode integrated terminal
# Keybindings already configured!
```

### Tip 4: Keybindings customization

Edit `.vscode/keybindings.json` to change shortcuts:

```json
[
  {
    "key": "ctrl+space ctrl+space", // Your custom shortcut
    "command": "rag-copilot.query"
  }
]
```

## 🐛 Troubleshooting

### Extension not working

```bash
# 1. Check if Python works
python3 --version

# 2. Check if RAG/quick_query.py works
cd RAG
python3 quick_query.py "test" --db primevue

# 3. Check VSCode Output
# View > Output > Select "RAG Copilot Helper"
```

### Tasks not working

```bash
# Check if you're in workspace folder
# Tasks require an open workspace folder!
```

### Clipboard not working (--copy)

```bash
# Install xclip
sudo apt install xclip

# OR xsel
sudo apt install xsel
```

## 📚 Next steps

1. ✅ **Try Extension** - best DX!
2. 📖 Read [USAGE.md](../RAG/USAGE.md) - full documentation
3. 🧪 See [EXAMPLE_QUESTIONS.md](../RAG/EXAMPLE_QUESTIONS.md) - 50+ examples
4. 🔧 Customize settings according to preferences
5. 🚀 Build amazing apps with zero hallucination!

---

**Questions? Issues? → [GitHub Repository](https://github.com/ThomasHoryn/nuxt-primevue-rag)**

🎉 **Happy coding without hallucinations!**
