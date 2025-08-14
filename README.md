
# Vextro Racing — Flask (Render-ready)

## Local dev (VS Code)
1) python3 -m venv .venv && source .venv/bin/activate
2) pip install -r requirements.txt
3) python app.py
4) Open http://127.0.0.1:5000

## Deploy on Render
1) Push this folder to a GitHub repo.
2) On https://render.com -> New -> Web Service.
3) Connect your GitHub repo and select it.
4) Start command: gunicorn app:app
5) Deploy — you'll get a public URL.
