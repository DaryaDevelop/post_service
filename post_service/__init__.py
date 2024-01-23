from flask import Flask

app = Flask(__name__)

from post_service.api import api as a
app.register_blueprint(a)
