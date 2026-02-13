# 🎯 How to use RAG with GitHub Copilot - ZERO HALLUCINATION

## Philosophy

Instead of letting Copilot "make up" code based on its training, **you feed it actual documentation fragments** before each question. Copilot becomes a "documentation translator", not an "oracle".

---

## 🚀 Quick Start (3 steps)

### 1. Run the prompt generator

```bash
cd RAG
python3 generate_prompt.py          # PrimeVue only
# or
python3 generate_prompt_universal.py  # Choose: PrimeVue/Nuxt/Both
```

### 2. Ask a question

```
🔎 What do you want to ask?: How to do sorting in DataTable?
```

The script will search the vector database and generate a ready-made prompt.

### 3. Copy and paste to Copilot Chat

1. **Select** text between `===== COPY BELOW =====`
2. **Copy** (Ctrl+C)
3. **Open GitHub Copilot Chat** in VS Code (Ctrl+Alt+I or icon)
4. **Paste** (Ctrl+V) and send

Copilot receives:

- 7 documentation fragments exactly about what you asked
- Strict rule: "Use ONLY this context"
- Your question

---

## 🎬 Example Workflow

### Example 1: Creating a PrimeVue component

**Question:** "How to create DataTable with pagination and sorting?"

```bash
python3 generate_prompt.py
# Type question
# Copy generated prompt
# Paste to Copilot Chat
```

**What you'll get:**

- DataTable code with all props
- Data binding
- Column configuration
- **NO outdated API** - because the source is your current documentation

### Example 2: Composables in Nuxt

**Question:** "How to make a composable for API handling in Nuxt 3?"

```bash
python3 generate_prompt_universal.py
# Choose: 2 (Nuxt)
# Type question
# Copy + paste to Copilot
```

**What you'll get:**

- Correct `/composables/useApi.ts` structure
- `useFetch` vs `$fetch` - when to use what
- Auto-import
- TypeScript types

---

## ⚙️ VS Code configuration for maximum precision

### Settings `.vscode/settings.json` (already configured)

```json
{
  "github.copilot.advanced": {
    "debug.overrideEngine": "gpt-4" // Better model = less hallucination
  },
  "github.copilot.enable": {
    "*": true,
    "markdown": true,
    "python": true,
    "typescript": true,
    "vue": true
  }
}
```

### Additional settings (optional)

If you want even more control over Copilot:

```json
{
  "github.copilot.editor.enableAutoCompletions": true,
  "github.copilot.editor.enableCodeActions": true
}
```

---

## 📋 Anti-Hallucination Rules

### ✅ DO THIS:

1. **Always use `generate_prompt.py` before complex questions**
   - "How to do X in PrimeVue?" → generator → Copilot

2. **Verify response with context fragments**
   - Copilot provides source (Header 1 > Header 2)
   - Check if it makes sense

3. **Ask specifically**
   - ❌ "How does routing work?"
   - ✅ "How to use dynamic route params in Nuxt 3?"

4. **Use generated prompt as "source of truth"**
   - If Copilot deviates from context → remind: "Use ONLY the context provided"

### ❌ DON'T DO THIS:

1. **Don't ask Copilot blindly about API**
   - Without context it may invent non-existent props

2. **Don't trust autocompletions unconditionally**
   - Inline suggestions may be from training, not documentation

3. **Don't mix frameworks in one question**
   - Choose database (Nuxt OR PrimeVue) and stick to it

---

## 🔧 Advanced: Workflow for larger tasks

### Scenario: Building CRUD with PrimeVue

1. **Question 1:** "How to create DataTable with CRUD operations?"

   ```bash
   python3 generate_prompt_universal.py  # Both databases
   ```

2. **Question 2:** "How to make Dialog for record editing?"

   ```bash
   python3 generate_prompt.py  # PrimeVue only
   ```

3. **Question 3:** "How to execute PUT request in Nuxt 3?"
   ```bash
   python3 generate_prompt_universal.py  # Nuxt
   ```

Each question = new prompt → clean separation of concerns → zero confusion.

---

## 🛠️ Parameters to experiment with

### In `generate_prompt.py` you can change:

```python
TOP_K = 7  # How many documentation fragments (3-10)
```

- **3-5**: Quick answers, less context
- **7-10**: More complete, longer prompts
- **Claude Sonnet**: Can handle even 15 fragments

---

## 🎓 Why does this work?

| Problem                  | RAG Solution                                   |
| ------------------------ | ---------------------------------------------- |
| Copilot invents old API  | You get current documentation                  |
| Copilot mixes frameworks | You choose database (Nuxt XOR PrimeVue)        |
| Copilot "guesses"        | Rule: "NO OUTSIDE KNOWLEDGE"                   |
| No sources               | Each fragment has header (Header 1 > Header 2) |

---

## 📚 Additional Materials

- [RAG/README.md](README.md) - How indexing works
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) - Project conventions

---

## 💡 Pro Tips

1. **Keep terminal with `generate_prompt.py` open** while coding
   - Ask → Copy → Paste → Code → Repeat

2. **Save frequently used prompts** in a text file
   - `my_prompts.txt` with ready contexts

3. **Use Claude Sonnet instead of GPT-4 in Copilot Chat?**
   - Sonnet is better at sticking to context
   - Copilot settings: Experiment with models

4. **Add your own rules to prompt**
   - E.g. "Always use TypeScript strict mode"
   - Edit `generate_prompt.py` → `<critical_rules>` section

---

## 🐛 Troubleshooting

### "Copilot still hallucinates"

1. Check if you copied **entire prompt** (with `<context>`)
2. Increase `TOP_K` to 10 (more context)
3. Add at end of prompt: "REMEMBER: Use ONLY the provided context. No external knowledge."

### "No fragments for my question"

1. Your question may be too general → Be more specific
2. Check if topic is in documentation (`nuxt-llms-full.txt` / `primevue-llms-full.txt`)
3. Change question wording (semantic search is sensitive to keywords)

### "Script crashes"

```bash
pip install --upgrade langchain-community langchain-chroma sentence-transformers
```

---

## ✅ Checklist for each new feature

- [ ] Run `generate_prompt.py` with question
- [ ] Copy generated prompt
- [ ] Paste to Copilot Chat
- [ ] Check if code uses ONLY patterns from context
- [ ] Verify cited sources (Headers)
- [ ] Test code

**If Copilot deviates from documentation → New prompt with more precise question.**

---

Made with 🧠 + ChromaDB + 💚 Nuxt/PrimeVue
