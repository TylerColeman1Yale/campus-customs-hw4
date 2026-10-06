# Campus Customs

React/Vite/TypeScript storefront with a FastAPI and PydanticAI-ready chatbot backed by the supplied SQLite catalogue.

Copy the supplied `data/` pack into this folder. Install backend dependencies with `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`. Run `cd backend && uvicorn main:app --reload --port 8000`. In another terminal run `cd frontend && npm install && npm run dev`.

The local database and images are intentionally ignored by Git. Copy `.env.example` to `.env` for optional Portkey configuration; never commit the real file.
