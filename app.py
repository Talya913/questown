from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('page1.html')

@app.route('/user/<username>')
def username(username):
    user_data =
    return render_template('page 2.html', user=user_data)


app.run()
