from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.discord_sender import send_discord_message
from app.token_store import load_tokens
from app.gpt_agent import analyze_life_admin
from app.google_tasks_service import fetch_tasks
# from app.google_tasks_service import fetch_tasks  # <- You'll add this soon

import time
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

def admin_agent_job():
    print(f"[Agent] Running Life Admin check at {time.ctime()}")
    
    try:
        tokens = load_tokens()
        if not tokens:
            raise ValueError("No tokens found for accessing Google Tasks")

        # 📋 Fetch Google Tasks (stub until we add actual code)
        print("🗒️ Fetching Google Tasks...")
        tasks = fetch_tasks(tokens["access_token"])  # Replace with: fetch_tasks(tokens["access_token"])

        # 🧠 Analyze with OpenAI
        print("🧠 Analyzing tasks with OpenAI...")
        digest = analyze_life_admin(tasks)

        # 📤 Send to Discord
        print("📤 Sending digest to Discord...")
        send_discord_message(f"🧠 Life Digest:\n{digest[:1900]}")  # Discord limit: 2000 chars

    except Exception as e:
        print(f"❌ Error during agent run: {e}")

def start_scheduler(app=None):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=admin_agent_job,
        trigger=IntervalTrigger(minutes=1),  # every 5 mins; adjust as needed
        id='life_admin_agent',
        name='Runs AI agent to check Google Tasks and send digest',
        replace_existing=True
    )
    scheduler.start()
    print("✅ Scheduler started")
