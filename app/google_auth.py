import os
import json
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

# ENV variables
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/auth/callback"
TOKEN_URL = "https://oauth2.googleapis.com/token"

# Google Tasks scope (update this if you need Gmail/Calendar)
SCOPES = [
    "https://www.googleapis.com/auth/tasks.readonly",
    "openid",
    "email",
    "profile"
]

def get_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

def exchange_code(code: str):
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code != 200:
        raise Exception(f"Token exchange failed: {response.text}")

    tokens = response.json()

    # Enrich with required fields for refreshing later
    tokens.update({
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "token_uri": TOKEN_URL
    })

    return tokens
