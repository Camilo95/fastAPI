import requests
from datetime import datetime
from core.config import settings

def createTaskClickUp(name, description):
    list_id = settings.LIST_ID
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"

    payload = {
        "name": name,
        "description": description,
        "assignees": [
            183
        ],
        "tags": [
            "contact"
        ],
        "status": "Open",
        "priority": 3,
        "due_date": 1681422701454,
        "due_date_time": False,
        "time_estimate": 8640000,
        "start_date": 1567780450202,
        "start_date_time": False,
        "notify_all": True,
        "parent": None,
        "links_to": None,
        "check_required_custom_fields": True,
        "custom_fields": [
            {
            "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
            "value": "This is a string of text added to a Custom Field."
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": settings.TOKEN_CLICK_UP
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    if data['err']:
        return None
    return True