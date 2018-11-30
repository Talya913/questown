import sqlite3

import us
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return render_template('page1.html')


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = us.get_users_by_name(q)
    return render_template("search_results.html", q=q, users=users)


# @app.route('/user/<username>')
# def username(username):
# user_data = username
# return render_template('page 2.html', user=user_data)


@app.route('/')
def hello_world():
    conn = sqlite3.connect('db.py')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM LIKE '{q}'".format(q=q))
    _users = list(c.fetchall())

    conn.close()
    #users = db.get_users_by_name(q)
    return render_template("search_results.html", q=q, users=_users)


app.run()
