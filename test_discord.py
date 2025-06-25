import os
import asyncio
from discord import Client, Intents
from dotenv import load_dotenv

load_dotenv()

DISCORD_USER_ID = int(os.getenv("DISCORD_USER_ID"))
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class QuickDM(Client):
    async def on_ready(self):
        print(f"✅ Logged in as {self.user}")
        user = await self.fetch_user(DISCORD_USER_ID)
        await user.send("✅ Hello from your Life Admin Agent! This is a test message.")
        await self.close()

intents = Intents.default()
client = QuickDM(intents=intents)

asyncio.run(client.start(DISCORD_BOT_TOKEN))
