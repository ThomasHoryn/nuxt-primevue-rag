# 🎬 Quick Start Guide - Step by Step

## 🎯 Goal

Teach GitHub Copilot to use **exclusively** Nuxt and PrimeVue documentation from your vector database, without hallucinations.

---

## ⚡ Quick start (5 minutes)

### 1. Make sure the databases are indexed

```bash
ls -la RAG/chroma_db_*
```

There should be 2 directories:

- `chroma_db_nuxt/` (37MB)
- `chroma_db_primevue/` (24MB)

If they don't exist, run:

```bash
cd RAG
python3 index_db.py
```

### 2. Test a simple query

```bash
cd RAG
python3 generate_prompt.py
```

When asked "What do you want to ask?", type:

```
How to do sorting in DataTable?
```

It should display a long prompt with documentation fragments.

### 3. Copy and paste to Copilot Chat

1. **Select** text between the lines:

   ```
   ================ COPY BELOW ================
   ...
   ================ END COPY ================
   ```

2. **Copy** (Ctrl+C / Cmd+C)

3. **Open GitHub Copilot Chat** in VS Code:
   - Keyboard: `Ctrl+Alt+I` (Linux/Win) or `Cmd+Alt+I` (Mac)
   - Or: Copilot icon in sidebar → Chat

4. **Paste** (Ctrl+V) and press Enter

5. **Check response:**
   - ✅ Cites sources (e.g. "DataTable > Sortable Mode")
   - ✅ Code uses props from documentation
   - ✅ DOES NOT invent non-existent APIs

---

## 📋 Complete workflow example

### Scenario: You want to build CRUD with PrimeVue

#### Step 1: DataTable

```bash
python3 generate_prompt.py
```

Question: "How to create DataTable with pagination and sorting?"
→ Copy → Paste to Copilot → You'll get DataTable code

#### Step 2: Edit Dialog

```bash
python3 generate_prompt.py
```

Question: "How to create Dialog for record editing in PrimeVue?"
→ Copy → Paste to Copilot → You'll get Dialog code

#### Step 3: API in Nuxt

```bash
python3 generate_prompt_universal.py
```

Choose: `2` (Nuxt)
Question: "How to execute PUT request in Nuxt 3?"
→ Copy → Paste to Copilot → You'll get composable with useFetch

---

## 🔥 Advanced Tips

### Tip 1: Use universal generator for multi-framework questions

```bash
python3 generate_prompt_universal.py
```

- Option `1`: PrimeVue only
- Option `2`: Nuxt only
- Option `3`: Both (7 fragments each = 14 total)

### Tip 2: Increase number of fragments for complex questions

Edit `generate_prompt.py`:

```python
TOP_K = 10  # Default: 7
```

More fragments = more context = more complete answers.

### Tip 3: Save frequently used prompts

Create a file `my_prompts.txt` with ready contexts for:

- Standard DataTable
- Standard Form with validation
- Standard CRUD composable

Copy-paste when needed!

### Tip 4: Remind Copilot when it hallucinates

If Copilot starts making things up, paste again:

```
REMEMBER: Use ONLY the provided context. No external knowledge.
```

---

## 🐛 Common Problems

### Problem: "Script not finding databases"

**Solution:**

```bash
cd RAG
python3 index_db.py --all
```

Wait 1-2 minutes for indexing.

### Problem: "Copilot ignores context"

**Solution:**

1. Check if you copied **entire prompt** (with `<context>` tags)
2. Try with smaller model: GPT-3.5 sometimes ignores instructions
3. Use GPT-4 or Claude Sonnet

### Problem: "No fragments for my question"

**Solution:**

1. Be more specific - add framework name (e.g. "in Nuxt 3", "in PrimeVue")
2. Check if topic is in documentation:
   - `nuxt-llms-full.txt` for Nuxt
   - `primevue-llms-full.txt` for PrimeVue
3. Change question wording

---

## ✅ Checklist for each question

- [ ] Formulate specific question
- [ ] Run `generate_prompt.py` or `generate_prompt_universal.py`
- [ ] Copy **entire** generated prompt
- [ ] Paste to Copilot Chat
- [ ] Verify Copilot cites sources
- [ ] Check if code uses only APIs from context
- [ ] Test code in project

---

## 📚 Next Steps

1. ✅ **Try 5-10 questions** from [EXAMPLE_QUESTIONS.md](EXAMPLE_QUESTIONS.md)
2. 📖 Read full guide [USAGE.md](USAGE.md)
3. 🚀 Check automation tools [AUTOMATION.md](../AUTOMATION.md)
4. 🔧 Customize `TOP_K` and rules in scripts
5. 🎯 Build real project with zero hallucinations!

---

**Questions? Problems? → [GitHub Repository](https://github.com/ThomasHoryn/nuxt-primevue-rag)**

🎉 **Happy coding without hallucinations!**
