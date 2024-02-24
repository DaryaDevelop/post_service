import os
import requests

from flask import request
from functools import wraps


def is_owner(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        uuid = request.headers.get("Token")
        uuid = uuid.split(" ")
        responce = requests.get(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/is_owner/{kwargs["id"]}",
                                json=request.json, 
                                headers={"Content-Type": "application/json"})
        if responce.status_code >= 400:
            return {
                "status": responce.json()["status"],
                "description": responce.json()["description"],
                "data": responce.json()["data"]
            }, responce.status_code
        elif responce.json()["data"]["user_id"]["uuid"] == uuid[1]:
            return func(*args, **kwargs)
        else:
            return {
                "status": 9,
                "description": "User is not the owner",
                "data": {}
            }, 400
    return wrapper
