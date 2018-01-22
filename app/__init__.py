from flask import Flask
app = Flask(__name__)

from app import views

import config
app.config.from_object(config)

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

