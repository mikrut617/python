from flask import Flask, session

app = Flask(__name__)

app.secret_key = "I set the secret here"