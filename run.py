from flask import Flask
from flask_restful import Api
from google.cloud import firestore
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()

db = firestore.Client(project=os.environ.get("GCP_PROJECT_ID"))

app = Flask(__name__)
jwt = JWTManager(app)
api = Api(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET')
app.config['JWT_TOKEN_LOCATION'] = 'headers'
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'
app.config["JWT_ALGORITHM"] = "HS256"

import resources

api.add_resource(resources.ChatBot, '/api/chat')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 8080))
