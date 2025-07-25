# openai-codex-test

This repository contains a sample Next.js + TypeScript client and a FastAPI server that demonstrates how to interact with the Korea Investment & Securities (KIS) API. The server exposes endpoints to query stocks based on short-term, medium-term and long-term strategies (qualitative or quantitative) and periodically fetches chart data for analysis. The client provides a minimal UI that fetches data from the server.

## Structure

- `client/` – Next.js application (app directory).
- `server/` – FastAPI application.
- `.gitignore` – ignores runtime files, node modules, and environment files.

## Usage

1. Copy `.env.example` to `.env` in both `client` and `server` directories and fill in the required values.
2. Install dependencies:

```bash
cd server && pip install -r requirements.txt
cd ../client && npm install
```

3. Run the API server:

```bash
cd server
uvicorn main:app --reload
```

4. Start the Next.js development server:

```bash
cd client
npm run dev
```

The client will fetch stock data from the FastAPI server.
