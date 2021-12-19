from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' :'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'Kobe', 'last_name' : 'Bryant'},
        {'first_name' : 'LeBron', 'last_name' : 'James'},
        {'first_name' : 'Stephen', 'last_name' : 'Curry'}
    ]
    return render_template("index.html", users=users)

if __name__=="__main__":
    app.run(debug=True)

