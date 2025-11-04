# Finstop Frontend (placeholder)

Planned stack: React + Vite + TypeScript + Tailwind + TanStack Query.

Pages:
- OTP Login
- Upload & Parse Status
- Tool Selection
- Results Dashboard & Exports

Setup later:
```bash
npm create vite@latest finstop-frontend -- --template react-ts
cd finstop-frontend
npm i @tanstack/react-query axios zod react-hook-form recharts tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Point API base URL to `http://localhost:8000/api/v1` in development.

