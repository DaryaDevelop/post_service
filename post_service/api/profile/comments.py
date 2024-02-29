import os

import requests
from flask import request

from post_service.api import api
from post_service.api.profile.utils import is_owner_comment


@api.get("/comments/<int:id>")
def get_comments(id):
    responce = requests.get(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/comments/{id}")
    return {
        "status": responce.json()["status"],
        "description": responce.json()["description"],
        "data": responce.json()["data"]
    }, responce.status_code


@api.post("/comments/<int:id>")
def new_comment(id):
    body = request.json.get("body")
    if not body:
        return {
            "status": 1,
            "description": "No such data in request",
            "data": {}
        }, 400
    responce = requests.post(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/comments/{id}",
                             json=request.json,
                             headers={"Content-Type": "application/json", "Token": request.headers.get("Token")})
    return {
        "status": responce.json()["status"],
        "description": responce.json()["description"],
        "data": responce.json()["data"]
    }, responce.status_code


@api.put("/comments/<int:id>")
@is_owner_comment
def update_comment(id):
    responce = requests.put(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/comments/{id}",
                            json=request.json,
                            headers={"Content-Type": "application/json"})
    return {
        "status": responce.json()["status"],
        "description": responce.json()["description"],
        "data": responce.json()["data"]
    }, responce.status_code


@api.delete("/comments/<int:id>")
@is_owner_comment
def delete_comment(id):
    responce = requests.delete(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/comments/{id}",
                               json=request.json,
                               headers={"Content-Type": "application/json"})
    return {
        "status": responce.json()["status"],
        "description": responce.json()["description"],
        "data": responce.json()["data"]
    }, responce.status_code
