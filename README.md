# 🤖 Life Admin Agent

This project connects your Google Tasks, OpenAI (ChatGPT), and Discord to help you automate your life admin work.

### Features
- ✅ Pulls your Google Tasks
- 🧠 Summarizes them with GPT-3.5
- 📢 Sends digest to your Discord inbox every 5 minutes

### Setup
1. Clone this repo and create a `.env` file from the example.
2. Create a Google OAuth Client (web type) and set the redirect URI to `http://localhost:8000/auth/callback`.
3. Enable Google Tasks API in your Google Cloud Console.
4. Add your OpenAI API Key.
5. Add your Discord bot token and user ID.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Go to [http://localhost:8000/auth/login](http://localhost:8000/auth/login) to authenticate with Google.