# 🚀 Quick Start Guide - Automation Edition

## 🎯 Cel

Ten przewodnik pokazuje **3 sposoby** automatyzacji RAG workflow dla maksymalnego DX (Developer Experience).

## 📦 Opcje automatyzacji

### 🥇 Option 1: VSCode Extension (NAJLEPSZY DX!)

**Czas setup:** 5 minut
**DX Level:** 🔥🔥🔥🔥🔥 (10/10)

#### Instalacja:

```bash
# 1. Przejdź do folderu extension
cd /home/tom/development/nuxt-primevue-rag/.vscode-extension

# 2. Zainstaluj dependencies
npm install

# 3. (Opcjonalnie) Zainstaluj vsce do pakowania
npm install -g @vscode/vsce

# 4. (Opcjonalnie) Spakuj extension
vsce package

# 5. Zainstaluj extension
code --install-extension rag-copilot-helper-1.0.0.vsix
```

**ALBO tryb development:**

```bash
# 1. Otwórz folder .vscode-extension w VSCode
code /home/tom/development/nuxt-primevue-rag/.vscode-extension

# 2. Naciśnij F5 - otworzy Extension Development Host
# 3. Extension będzie aktywny w nowym oknie!
```

#### Użycie:

1. **Naciśnij `Ctrl+Shift+R`**
2. Wpisz pytanie: "How to use DataTable in PrimeVue?"
3. Wybierz źródło (Both/PrimeVue/Nuxt)
4. ✨ **GOTOWE!** Prompt jest w edytorze + w schowku
5. Kliknij "Open Copilot Chat" lub `Ctrl+Alt+I`
6. Wklej (Ctrl+V) i otrzymaj kod! 🎉

**Konfiguracja** (VSCode Settings):

```json
{
  "ragCopilot.pythonPath": "python3",
  "ragCopilot.ragPath": "${workspaceFolder}/RAG",
  "ragCopilot.autoOpenCopilot": true,
  "ragCopilot.autoCopyClipboard": true
}
```

---

### 🥈 Option 2: VSCode Tasks + Keybindings (Szybkie)

**Czas setup:** 1 minuta (już skonfigurowane!)
**DX Level:** 🔥🔥🔥🔥 (8/10)

Tasks i keybindings są już w `.vscode/tasks.json` i `.vscode/keybindings.json`.

#### Użycie:

**Metoda 1: Keybindings**

- `Ctrl+Shift+R Q` - Quick Query (z promptem)
- `Ctrl+Shift+R P` - Query PrimeVue
- `Ctrl+Shift+R N` - Query Nuxt
- `Ctrl+Shift+R B` - Query Both

**Metoda 2: Command Palette**

1. `Ctrl+Shift+P`
2. Wpisz: "Tasks: Run Task"
3. Wybierz: "RAG: Quick Query"
4. Wpisz pytanie w prompt
5. Wybierz database (primevue/nuxt/both)

**Metoda 3: Terminal Menu**

1. Menu: `Terminal > Run Task...`
2. Wybierz task

---

### 🥉 Option 3: Python CLI Script (Programmatyczne)

**Czas setup:** 0 minut (już gotowe!)
**DX Level:** 🔥🔥🔥 (7/10)

Użyj `quick_query.py` bezpośrednio z terminala.

#### Użycie:

```bash
cd RAG

# Basic query
python3 quick_query.py "How to use DataTable?" --db primevue

# Query with both databases
python3 quick_query.py "useFetch with DataTable" --db both

# Query Nuxt only
python3 quick_query.py "useState in Nuxt 3" --db nuxt

# With auto-copy to clipboard (wymaga xclip/xsel)
python3 quick_query.py "Your question" --db both --copy
```

**Parametry:**

- `question` - Twoje pytanie (wymagane)
- `--db` - Źródło: `primevue`, `nuxt`, `both` (default: `both`)
- `--copy` - Auto-kopiuj do schowka (wymaga `xclip` lub `xsel`)

**Instalacja xclip (dla --copy):**

```bash
sudo apt install xclip
# LUB
sudo apt install xsel
```

---

## 📊 Porównanie metod

| Metoda              | Setup | Kliknięć | Czas | DX Score         |
| ------------------- | ----- | -------- | ---- | ---------------- |
| VSCode Extension    | 5 min | 3        | 3s   | 🔥🔥🔥🔥🔥 10/10 |
| Tasks + Keybindings | 0 min | 4        | 5s   | 🔥🔥🔥🔥 8/10    |
| Python CLI          | 0 min | 0        | 2s   | 🔥🔥🔥 7/10      |

## 🎬 Kompletny workflow (Extension)

```
👨‍💻 Ty: "Potrzebuję DataTable z sortowaniem"
      ↓ [Ctrl+Shift+R]
🤖 Extension: "What do you want to ask?"
      ↓ [wpisujesz pytanie]
🤖 Extension: "Select documentation source"
      ↓ [wybierasz "Both"]
📚 RAG: [ładuje bazy, szuka fragmentów]
      ↓ [1-2 sekundy]
📝 VSCode: [otwiera prompt w edytorze]
📋 Clipboard: [prompt już skopiowany]
      ↓ [klikasz "Open Copilot Chat"]
💬 Copilot Chat: [otwiera się]
      ↓ [Ctrl+V wklejasz]
🧠 Copilot: [analizuje 7-14 fragmentów]
      ↓ [2-3 sekundy]
✅ Copilot: [generuje kod ZERO halucynacji]
      ↓ [kopiujesz kod]
🎉 DONE! Feature gotowy!
```

**Total time: < 10 sekund od pomysłu do kodu! ⚡**

## 🔥 Pro Tips

### Tip 1: Używaj Extension w trybie development

Jeśli chcesz modyfikować extension:

```bash
cd .vscode-extension
code .
# Naciśnij F5 - otwiera Extension Development Host
# Możesz debugować i live-reload zmian!
```

### Tip 2: Aliasy dla CLI

Dodaj do `~/.bashrc` lub `~/.zshrc`:

```bash
alias rag='python3 /home/tom/development/nuxt-primevue-rag/RAG/quick_query.py'
alias ragp='rag --db primevue'
alias ragn='rag --db nuxt'
alias ragb='rag --db both'
```

Użycie:

```bash
ragp "How to use DataTable?"
ragn "useState in Nuxt 3"
ragb "useFetch with DataTable"
```

### Tip 3: VS Code Task w terminalu

```bash
# Szybki dostęp przez VSCode integrated terminal
# Już skonfigurowane keybindings!
```

### Tip 4: Keybindings customization

Edytuj `.vscode/keybindings.json` aby zmienić skróty:

```json
[
  {
    "key": "ctrl+space ctrl+space", // Twój custom shortcut
    "command": "rag-copilot.query"
  }
]
```

## 🐛 Troubleshooting

### Extension nie działa

```bash
# 1. Sprawdź czy Python działa
python3 --version

# 2. Sprawdź czy RAG/quick_query.py działa
cd RAG
python3 quick_query.py "test" --db primevue

# 3. Sprawdź VSCode Output
# View > Output > Select "RAG Copilot Helper"
```

### Tasks nie działają

```bash
# Sprawdź czy jesteś w workspace folder
# Tasks wymagają otwartego folderu workspace!
```

### Clipboard nie działa (--copy)

```bash
# Zainstaluj xclip
sudo apt install xclip

# ALBO xsel
sudo apt install xsel
```

## 📚 Następne kroki

1. ✅ **Wypróbuj Extension** - najlepszy DX!
2. 📖 Przeczytaj [USAGE.md](../RAG/USAGE.md) - pełna dokumentacja
3. 🧪 Zobacz [EXAMPLE_QUESTIONS.md](../RAG/EXAMPLE_QUESTIONS.md) - 50+ przykładów
4. 🔧 Customizuj settings według preferencji
5. 🚀 Build amazing apps z zero halucynacji!

---

**Pytania? Issues? → [GitHub Repository](https://github.com/ThomasHoryn/nuxt-primevue-rag)**

🎉 **Happy coding without hallucinations!**
