import os
import requests

from post_service.api import api
from flask import request
from dotenv import load_dotenv

load_dotenv()


@api.get("/all_posts")
def get_all_posts():
    responce = requests.get(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/all_posts")
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200


@api.post("/new_posts")
def create_new_posts():
    title = request.json.get("title")
    body = request.json.get("body")
    if not title or not body:
        return {
            "status": 1,
            "description": "Fail",
            "data": {}
        }, 400
    responce = requests.post(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/new_posts",
                             json=request.json, headers={"Content-Type": "application/json"})
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200
    
    
@api.put("/posts/<int:id>")
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
    
    
@api.delete("/delete_posts/<int:id>")
def delete_posts(id):
    responce = requests.delete(f"http://{os.getenv('DB_SERVICE_HOST')}:{os.getenv('DB_SERVICE_PORT')}/delete_posts/{id}",
                            json=request.json, headers={"Content-Type": "application/json"})
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "posts": responce.json().get("posts")
        }
    }, 200
