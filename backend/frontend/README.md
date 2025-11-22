🩺 Health Monitoring App
A simple full‑stack application built with FastAPI (Python) for the backend and HTML + JavaScript for the frontend. It allows users to sign up, log in, add health readings (blood sugar & blood pressure), and view their readings.

🚀 Features
User Authentication: Signup & Login with email + password.

Health Data Tracking: Add blood sugar and blood pressure readings.

Data Storage: SQLite database with SQLAlchemy ORM.

Frontend UI: HTML forms with JavaScript fetch() calls.

Interactive Docs: Swagger UI available at /docs.

📂 Project Structure
Code
health-monitoring-app/
│
    README.md 
├── backend/                # FastAPI backend
│   ├── main.py              # API routes
│   ├── models.py            # SQLAlchemy models
│   ├── auth.py              # Authentication helpers
│   ├── schemas.py           # Pydantic schemas
│   ├── create_db.py         # Initialize database
│   ├── requirements.txt     # Dependencies
│   └── database.db          # SQLite database
│
├── frontend/               # Static frontend
│   ├── index.html           # Signup/Login/Add readings
│   ├── dashboard.html       # View readings (optional)
│   └── script.js            # JavaScript logic
│
└── .venv/                  # Virtual environment

⚙️ Installation & Setup

1. Clone the repo
bash
git clone https://github.com/yourusername/health-monitoring-app.git
cd health-monitoring-app/backend

2. Create virtual environment
bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
bash
python -m pip install -r requirements.txt

4. Initialize database
bash
python create_db.py

5. Run the server
bash
python -m uvicorn main:app --reload
Backend runs at: http://127.0.0.1:8000 Docs available at: http://127.0.0.1:8000/docs

🖥️ Frontend Usage
Open frontend/index.html in your browser.

Signup → Login → Add readings.

Click View Readings to see your health data in a table.

📦 Dependencies
FastAPI

Uvicorn

SQLAlchemy

Passlib[bcrypt]

Python‑Multipart

✨ Future Improvements
JWT authentication (instead of passing user_email manually).

Styling with CSS framework (Bootstrap/Tailwind).

Graphs for health trends.