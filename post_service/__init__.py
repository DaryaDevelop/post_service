from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

from post_service.api import api as a

app.register_blueprint(a)
