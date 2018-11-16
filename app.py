from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('page1.html')

@app.route('/about')
def about():
    return 'The about page'


app.run()
