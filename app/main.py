from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.google_auth import get_auth_url, exchange_code
from app.token_store import save_tokens
from app.scheduler import start_scheduler

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Life Admin Agent is running"}

@app.get("/auth/login", response_class=RedirectResponse)
def login():
    return RedirectResponse(get_auth_url())

@app.get("/auth/callback")
def callback(code: str = None):
    if not code:
        return {"error": "No code provided from Google"}
    try:
        tokens = exchange_code(code)
        save_tokens(tokens)
        return RedirectResponse("/welcome")
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/welcome")
def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

# ✅ Start background scheduler
start_scheduler(app)
