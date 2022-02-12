from urllib.parse import quote_plus
from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.quote import Quote


@app.route('/quotes')
def index():
    quotes=Quote.get_all_with_users()
    return render_template(quote_dashboard.html, )

