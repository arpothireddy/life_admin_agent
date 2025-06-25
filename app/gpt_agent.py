# app/gpt_agent.py

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_life_admin(tasks):
    try:
        task_summary = "\n".join([f"- {task}" for task in tasks]) if tasks else "No tasks found."

        prompt = f"""
        You are a helpful assistant. Analyze these Google Tasks and summarize them for the user. Prioritize urgent or time-sensitive ones, and suggest what to tackle next.

        Tasks:
        {task_summary}

        Response format:
        - Summary of tasks
        - Top 3 priorities
        - Suggested schedule
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a productivity assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"OpenAI error: {str(e)}"
