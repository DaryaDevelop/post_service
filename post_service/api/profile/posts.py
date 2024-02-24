import os
import requests

from post_service.api import api
from flask import request
from dotenv import load_dotenv
from post_service.api.profile.utils import is_owner

load_dotenv()


@api.get("/posts")
def get_all_posts():
    responce = requests.get(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/posts")
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200


@api.post("/posts")
def create_new_posts():
    title = request.json.get("title")
    body = request.json.get("body")
    if not title or not body:
        return {
            "status": 1,
            "description": "No such data in request",
            "data": {}
        }, 400
    responce = requests.post(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/posts",
                             json=request.json,
                             headers={"Content-Type": "application/json", "Token": request.headers.get("Token")})
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200
    
    
@api.put("/posts/<int:id>")
@is_owner
def update_posts(id):
    responce = requests.put(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/posts/{id}",
                            json=request.json, headers={"Content-Type": "application/json"})
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200
    
    
@api.delete("/posts/<int:id>")
@is_owner
def delete_posts(id):
    responce = requests.delete(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/posts/{id}",
                            json=request.json, headers={"Content-Type": "application/json"})
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200
