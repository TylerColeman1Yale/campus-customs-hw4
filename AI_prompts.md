# Homework 4 prompts

## Question 1 — Vibe coder prompts

I want you to help me build my Homework 4 project: a Campus Customs shop with a working chatbot.

We will work through questions in order, one question at a time. Complete and check each question before moving to the next. Let me know if you need something from me, like the data files, API configuration, an answer, or approval. If you need me, tell me specifically what you need and where we're at. Once I answer, continue from that point.

Keep the explanations and write-ups clear and straightforward, like how I'm writing here.

Actually build the project and run or test the parts you can. Keep track of what has been completed, what still needs checking, and any setup step I need to do myself. Do not just give me general instructions when you can make the files and implement the feature.

## Question 2 — Analyze the database

Look at campus_customs.db and figure out how the database is structured before building around it.

At a minimum, inspect the catalogue, inventory, and users tables. Understand the actual fields, their types, and how the tables connect. Don't assume the schema.

Also check the other tables that may be useful for customer memory or the chatbot. Record the real table names, columns, relationships, and a few useful facts in output/harness.md so the later features are based on the supplied data instead of guesses.

## Question 3 — Build the Campus Customs website

Build the front end with React, Vite, and TypeScript.

Put a navigation bar at the top with Home, Products, About Us, Login, and Create account. Use yalebulldogblue.com to understand Campus Customs and the feel of the business. Write the Home and About Us pages in original, straightforward wording. Add real catalogue products, product pages, and a chat interface.

Use the actual product records and image paths from the database. Product cards should be easy to scan and should open a full product page with the image, description, price, sizes, and available stock when those details exist. If the backend is needed to serve the data and images, create the small API now and leave it ready for the later agent work.

## Question 4 — Create account and login

Build a working create-account and login flow. Ask for first name, last name, email, password, and confirmation. Save accounts in users with secure password hashes. Confirm the supplied test account can log in.

Do not send password hashes to the browser or expose them through chatbot responses. Handle duplicate emails and incorrect passwords clearly. Test both the supplied account and a newly created account, and explain in the harness how the user identity is represented after login.

### Question 4 Follow Up Prompt 1

I can't seem to log in. Is there something I'm doing wrong? The assignment says to use `test@campuscustoms.yale.edu` with the password `password`, and I want to confirm that the supplied test account and a new account both work.

The issue turned out to have two parts: the backend was initially being started with the Lecture 2 virtual environment instead of the Homework 4 environment, and the supplied seed account used a legacy password-hash format that the login check did not recognize. Use `hw4/.venv`, install the Homework 4 requirements, and make the backend accept the documented seed login while migrating it to the current secure hash format after successful login. Confirm the login works and keep the fix documented.

## Question 5 — PydanticAI agent backend

Build the chatbot as a real PydanticAI agent behind FastAPI and connect it to the front-end chat widget. Use backend/main.py, prompts/prompt.md, agent.py, tools.py, and models.py.

Keep the agent setup organized so the system prompt is loaded from the prompt file, the structured response types are defined in models.py, and the tools are kept separate from the route code. Add the chat endpoint, document the model configuration, and make sure the command `uvicorn main:app --reload --port 8000` works when run from the backend folder.

## Question 6 — Tools for product information and stock

Give the agent tools that look up real descriptions, prices, stock quantities, and stock by size in campus_customs.db. Never invent prices or inventory.

The tools should return enough structured information for both a helpful written answer and a product card. If a product or size cannot be identified, ask a useful follow-up question. Clearly say when something is out of stock, and check several answers against the database before moving on.

## Question 7 — Chat search that updates the page

Make the chatbot update the website with matching products. Return structured product matches and show working product cards on the page.

For a question such as “What hoodies do you have?”, search the real catalogue, return a capped list of matching products, and have the front end update the visible product area instead of only printing a text list in chat. Make sure cards returned by chat use the same click behavior and product detail page as cards on the regular Products page. Document the API contract in output/harness.md.

## Question 8 — Customer memory

When a customer is logged in, save chat history in the database and reload it when they return. Keep users isolated, support guests, and pass current product page context.

Pass the authenticated customer identity to the agent through a clear dependency or context object, including the customer's name and email when appropriate. A customer must only be able to read their own history. Guests can still chat without persistence. When the customer is on a product page, include that product context so questions such as “Do you have this in pink?” refer to the correct item.

## Question 9 — Usability improvements

Choose and implement two front-end usability improvements and two agent or backend usability improvements. Explain what you chose and why.

Choose improvements that add something beyond the required catalogue, login, chat search, and history features. Write output/usability.md before or during the work, keep each explanation short and concrete, and verify that all four improvements are visible or testable in the running application.

## Question 10 — Style the website

Give the website a creative, polished design that feels like a real Campus Customs storefront. Explain the concrete design choices.

Think about typography, Yale-inspired colors, spacing, visual hierarchy, product photography, responsive behavior, hover states, motion, and the chat interface. Keep the result easy to browse and readable on a smaller screen. Record specific examples from the implemented design in output/design.md.

## Question 11 — Site testing and app check

Test the running website and create output/app_check.html with real screenshots and captions for inventory, dynamic product cards, and one usability improvement.

Use screenshots from the actual running app, not placeholder images or invented evidence. Save them in output/app_check_images/ and use relative paths so app_check.html works when opened by double-clicking. Include a clear heading and one or two sentences explaining what each screenshot proves. If I need to capture a browser screenshot myself, give me the exact action and filename.

## Question 12 — Audit trail, safety, and finish the harness

Keep an append-only record of agent-loop activity in output/audit_trail.json. Add practical safety rules and finish output/harness.md so someone can understand how the system works.

Keep existing audit entries when adding new ones, preserve valid JSON, and record the time, tool name, short argument summary, short result summary, and stop reason. Never log passwords, password hashes, API keys, or other secrets. Make sure the harness describes the real models, tools, prompt loading, result limits, authentication, history, page context, run commands, and safety behavior.

## Question 13 — Push to GitHub and submit the URL

Finish the project in the hw4 folder and prepare it for a public GitHub repository. Keep the database and supplied product images local, don't commit secrets, document setup, check the requirements, and ask for approval before publishing.

Confirm that the required files and folders are present, that the app can be started, and that the database and image paths work after the supplied data pack is placed locally. Check that no real `.env` file, API key, database, or product images would be committed. Do not publish or push anything until I approve it, and then give me the final repository status and public URL if access is available.
