import os
import requests

# Load from environment
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(content: str):
    if not DISCORD_WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK_URL is not set in the environment variables.")
    
    # Truncate if message is too long (Discord limit is 2000 characters)
    if len(content) > 2000:
        content = content[:1997] + "..."

    payload = {
        "content": content
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code != 204:
        raise Exception(f"❌ Failed to send Discord message: {response.status_code} {response.text}")
