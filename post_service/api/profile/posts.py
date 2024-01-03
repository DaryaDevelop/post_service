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


# @api.post("/new_posts")
# def create_new_posts():
#     title = request.json.get("title")
#     body = request.json.get("body")
#     if not title or not body:
#         return {
#             "status": 1,
#             "description": "Fail",
#             "data": {}
#         }, 400
#     check_name = Posts.query.filter_by(title=title).first()
#     if check_name:
#         return {
#             "status": 2,
#             "description": "Title already exist",
#             "data": {}
#             }, 400
#     item = Posts(title=title, body=body)
#     db.session.add(item)
#     db.session.commit()
#     return {
#         "status": 0,
#         "description": "OK",
#         "data": {
#             "posts": {
#                 "id": item.id,
#                 "title": item.title,
#                 "body": item.body
#             }
#         }
#     }, 200
    
    
# @api.put("/posts/<int:id>")
# def update_posts(id):
#     item = Posts.query.get(id)
#     if not item:
#         return {
#             "status": 3,
#             "description": "Fail",
#             "data": {}
#         }, 400
#     title = request.json.get("title")
#     body = request.json.get("body")
#     item.title = title if title else item.title
#     item.body = body if body else item.body
#     db.session.commit()
#     return {
#         "status": 0,
#         "description": "OK",
#         "data": {
#             "posts": {
#                 "id": item.id,
#                 "title": item.title,
#                 "body": item.body
#             }
#         }
#     }, 200
    

# @api.delete("/delete_posts/<int:id>")
# def delete_posts(id):
#     item = Posts.query.get(id)
#     if not item:
#         return {
#             "status": 3,
#             "description": "Fail",
#             "data": {}
#         }, 400
#     db.session.delete(item)
#     db.session.commit()
#     return {
#         "status": 0,
#         "description": "OK",
#         "data": {
#             "posts": {
#                 "id": item.id,
#                 "title": item.title,
#                 "body": item.body
#             }
#         }
#     }, 200
    