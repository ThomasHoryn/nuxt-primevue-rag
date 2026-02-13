# 📋 Example Questions for Testing RAG System

## PrimeVue - Components

### DataTable

- "How to do sorting in DataTable?"
- "How to add pagination to DataTable in PrimeVue?"
- "How to customize columns in DataTable?"
- "How to make filters in DataTable?"
- "How to handle selection in DataTable?"

### Dialog/Modal

- "How to create Dialog in PrimeVue?"
- "How to pass data to Dialog in PrimeVue?"
- "How to handle Dialog closing?"

### Form Components

- "How to use InputText in PrimeVue?"
- "How to do form validation with PrimeVue?"
- "How to use Dropdown in PrimeVue?"
- "How to use Calendar for date selection?"

### Toast/Messages

- "How to show toast notification in PrimeVue?"
- "How to use Toast service in PrimeVue?"
- "How to add Message to component?"

### Styling

- "How to customize theme in PrimeVue?"
- "How to use Tailwind with PrimeVue?"
- "How to style PrimeVue components?"

---

## Nuxt 3 - Core Concepts

### Routing

- "How do dynamic routes work in Nuxt 3?"
- "How to use route params in Nuxt 3?"
- "How to make nested routes in Nuxt 3?"
- "How to use middleware in Nuxt 3?"

### Data Fetching

- "How to use useFetch in Nuxt 3?"
- "What is the difference between useFetch and $fetch in Nuxt 3?"
- "How to handle errors in useFetch?"
- "How to do server-side fetching in Nuxt 3?"

### Composables

- "How to create composable in Nuxt 3?"
- "How to use useState in Nuxt 3?"
- "How to make shared state in Nuxt 3?"
- "Where to place composables in Nuxt 3?"

### Server

- "How to create API endpoint in Nuxt 3?"
- "How to use server routes in Nuxt 3?"
- "How to handle POST request in Nuxt server?"

### Configuration

- "How to configure Nuxt 3?"
- "How to add modules to Nuxt 3?"
- "How to use runtime config in Nuxt 3?"
- "How to configure TypeScript in Nuxt 3?"

### Components

- "How do auto-imports work in Nuxt 3?"
- "How to make layout in Nuxt 3?"
- "How to use pages in Nuxt 3?"

---

## Combined (Nuxt + PrimeVue)

### Integration

- "How to integrate PrimeVue with Nuxt 3?"
- "How to use PrimeVue components in Nuxt 3?"
- "How to configure PrimeVue in nuxt.config?"

### CRUD Operations

- "How to make CRUD with DataTable in Nuxt 3?"
- "How to handle edit form in Nuxt with PrimeVue?"
- "How to connect useFetch with DataTable in PrimeVue?"

### State Management

- "How to manage form state with PrimeVue in Nuxt 3?"
- "How to share state between PrimeVue components in Nuxt?"

### Real-world Scenarios

- "How to build user management table with DataTable + useFetch?"
- "How to create product catalog with PrimeVue + Nuxt 3?"
- "How to implement authentication flow with PrimeVue Dialog + Nuxt composables?"

---

## Advanced Questions

### Performance

- "How to optimize DataTable performance with large datasets?"
- "How to implement virtual scrolling in PrimeVue?"
- "How to lazy load data in DataTable?"

### Error Handling

- "How to handle API errors in Nuxt 3 with Toast notifications?"
- "How to show loading state in DataTable while fetching?"
- "How to implement retry logic with useFetch?"

### TypeScript

- "How to type PrimeVue components in TypeScript?"
- "How to type Nuxt 3 composables with TypeScript?"
- "How to type useFetch return value?"

### Testing

- "How to test PrimeVue Dialog component?"
- "How to test Nuxt composables?"
- "How to mock useFetch in tests?"

---

## Tips for Asking Questions

### ✅ Good Questions (Specific)

- "How to enable row selection in PrimeVue DataTable **with checkbox column**?"
- "How to use **useFetch** for GET request in Nuxt 3 **with query parameters**?"
- "How to customize **Dialog header** in PrimeVue?"

### ❌ Bad Questions (Too General)

- "How to use DataTable?" (which aspect?)
- "How does Nuxt work?" (too broad)
- "How to fetch data?" (which method?)

### 🎯 Question Formula

```
How to [action] in [framework] [specific context/constraint]?
```

Examples:

- "How to **create dynamic routes** in **Nuxt 3** with **route parameters**?"
- "How to **handle form submission** in **PrimeVue** with **validation**?"
- "How to **implement pagination** in **DataTable** with **server-side data**?"

---

## Testing Workflow

### Test 1: Simple Component

```bash
python3 generate_prompt.py
```

Question: "How to create Button in PrimeVue?"
Expected: Basic Button code with props

### Test 2: Complex Component

```bash
python3 generate_prompt.py
```

Question: "How to create DataTable with pagination, sorting and filters?"
Expected: Complete DataTable setup with all features

### Test 3: Framework Integration

```bash
python3 generate_prompt_universal.py
```

Choose: `3` (Both)
Question: "How to use useFetch with DataTable in Nuxt 3?"
Expected: Composable + DataTable integration code

### Test 4: Edge Case

```bash
python3 generate_prompt.py
```

Question: "How to customize DataTable empty message?"
Expected: Specific template slot documentation

---

## Success Criteria

When testing questions, verify:

- ✅ Copilot **cites sources** (Header 1 > Header 2)
- ✅ Code uses **only APIs from context**
- ✅ No **invented props** or methods
- ✅ Code is **syntactically correct**
- ✅ Follows **Composition API** (not Options API)
- ✅ Uses **TypeScript** if applicable

---

Made with 🧠 + ChromaDB + 💚 Nuxt/PrimeVue
