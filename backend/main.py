# backend/run.py
from flask import Flask
from backend.app.api.routes import api
import os

app = Flask(__name__)
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(f'backend.config.{env.capitalize()}Config')
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
