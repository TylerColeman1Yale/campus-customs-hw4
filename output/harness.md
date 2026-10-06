# System harness

## Database

`catalogue` contains product ID, name, garment type, description, colors, search tags, image path, and price. These fields power product cards, search, images, and factual prices. `inventory` contains an ID, product ID foreign key, size, and quantity; its unique product/size pair supports exact checks. `users` contains ID, name, email, password hash, created time, first name, and last name. `chat_messages` contains ID, user ID, role, content, product JSON, and created time for logged-in history.

## Flow and safety

FastAPI serves products, authentication, history, and chat. Passwords use PBKDF2-HMAC-SHA256 with random salts and hashes never leave the backend. `tools.py` joins catalogue to inventory. Chat returns `{reply, products}` and the front end renders returned cards. Logged-in messages use the authenticated user ID; product context is sent as `product_id`; guests are not persisted. The prompt requires database facts for prices and stock, protects private data and secrets, rejects bypass requests, asks clarifying questions, caps results at 12, and uses one lookup per request.

## Audit trail

Each completed chat request appends a JSON object to `output/audit_trail.json` with UTC time, tool name, non-sensitive argument summary, result summary, and stop reason. Existing entries are preserved. Message text, passwords, hashes, API keys, and other secrets are not logged.

## Run

From `backend/`: `uvicorn main:app --reload --port 8000`. From `frontend/`: `npm install && npm run dev`. The local data pack is required. The design uses Yale-inspired blue, orange accents, cream backgrounds, DM Sans, Playfair Display, hover lift, responsive layout, and persistent chat.
