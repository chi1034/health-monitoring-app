# Health Monitoring App

A full-stack health monitoring application built with **FastAPI** on the backend and **HTML + JavaScript** on the frontend. Users can sign up, log in, record health readings, and view their data in a dashboard. Data is stored in **SQLite** using **SQLAlchemy ORM**.

---

## 🚀 Live Demo

- **Frontend**: [https://health-monitoring-app-p8nt.vercel.app](https://health-monitoring-app-p8nt.vercel.app)
- **Backend**: [https://health-monitoring-backend.up.railway.app](https://health-monitoring-backend.up.railway.app)

---

## 🧩 Project Structure
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


---

## 🖥️ Frontend Features

- Signup and login forms
- Dashboard to view health readings
- Responsive design
- LocalStorage token handling

---

## ⚙️ Backend Features

- FastAPI endpoints for auth and data
- JWT-based authentication
- SQLite database with SQLAlchemy models
- CORS enabled for frontend integration

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI, Python, SQLAlchemy, SQLite
- **Deployment**: Vercel (frontend), Railway (backend)

---

## 📦 Setup Instructions

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload

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

Frontend
Just open index.html in your browser or deploy via Vercel.

📁 Deployment Artifacts
Procfile for Railway

.gitignore for clean repo

requirements.txt for backend dependencies

🏷️ Tags
#fastapi #vercel #railway #sqlite #fullstack #health-app

🙌 Author
Made with ❤️ by Odii Chinenye Gift GitHub: github.com/chi1034

✨ Future Improvements
JWT authentication (instead of passing user_email manually).

Styling with CSS framework (Bootstrap/Tailwind).

Graphs for health trends.