import requests

GOOGLE_TASKS_API_URL = "https://tasks.googleapis.com/tasks/v1/lists/@default/tasks"

def fetch_tasks(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "showCompleted": False,
        "maxResults": 10  # You can increase or customize this
    }

    response = requests.get(GOOGLE_TASKS_API_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Google Tasks API error: {response.status_code} - {response.text}")

    data = response.json()
    tasks = data.get("items", [])

    task_titles = [task["title"] for task in tasks if not task.get("status") == "completed"]

    return task_titles
