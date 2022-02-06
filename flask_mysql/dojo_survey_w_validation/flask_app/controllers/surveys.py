from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create/survey',methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        results = Survey.save(request.form)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:id>')
def get_one(id):
    data = {
        "id" : id
    }
    return render_template('results.html', survey = Survey.get_last_survey(data))