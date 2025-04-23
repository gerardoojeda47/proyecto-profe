from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'gerardo'

load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gerardozapatos@gmail.com' 
app.config['MAIL_PASSWORD'] = 'ktyvkqnowaoytjnm'    
app.config['MAIL_DEFAULT_SENDER'] = 'gerardozapatos@gmail.com'

mail = Mail(app)

CORS(app)
app.config["UPLOAD_FOLDER"] = "./static/img"

app.config["MONGODB_SETTINGS"] = [{
    "db": "examengerardo",
    "host": os.getenv("MONGO_URI"),
    "port": 27017
}]

db = MongoEngine(app)


from routers.sena import *
from routers.instructor import *
from routers.lasguias import *





if __name__ == "__main__":
    app.run(port=6510, host="0.0.0.0", debug=True)