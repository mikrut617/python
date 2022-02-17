from flask import Flask

app = Flask(__name__)

app.secret_key = "Any password will do....just not this one."