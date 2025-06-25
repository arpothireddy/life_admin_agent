# 🧠 Life Admin Agent

Do you keep forgetting your reminders?  
This is the reminder **for your reminders**.

**Life Admin Agent** is a smart automation bot that connects your **Google Tasks**, **OpenAI**, and **Discord** to help you manage your life effortlessly.  
It pulls your pending to-dos, runs them through OpenAI to create a smart summary, and delivers that summary to you via Discord every few minutes — no more mental clutter.

---

## ✨ Features

- ✅ Pulls your tasks from **Google Tasks**
- 🧠 Summarizes them using **OpenAI GPT-3.5**
- 📬 Sends a **digest message to your Discord DMs**
- 🔁 Runs automatically on a schedule (every 5 minutes by default)

---

## 🚀 Setup Instructions

### 1. Clone the repo and set up the virtual environment

```bash
git clone https://github.com/YOUR_USERNAME/life_admin_agent.git
cd life_admin_agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt