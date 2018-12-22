import sqlite3

import us
from flask import Flask, flash, redirect, url_for
from flask import render_template
from flask import request
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SedovianDog'


@app.route('/')
def home():
    return render_template('page1.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    #if form.validate_on_submit():
        #if
            #flash('Log in is successful!', 'success')
            #return redirect(url_for('home'))
        #else:
            #flash('Access is denied. Incorrect email or password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)


#@app.route('/search')
#def search_for_person():
    #q = request.args.get('query')
    #users = us.get_users_by_name(q)
    #return render_template("search_results.html", q=q, users=users)


# @app.route('/user/<username>')
# def username(username):
# user_data = username
# return render_template('page 2.html', user=user_data)


#def dict_factory(cursor, row):
    #d = {}
    #for idx, col in enumerate(cursor.description):
        #d[col[0]] = row[idx]
    #return d

#@app.route('/')
#def fun1():
    ## Connecting to DB
    #conn = sqlite3.connect('app.db')
    #conn.row_factory = dict_factory
    #c = conn.cursor()

    ## Handler logic here
    #c.execute("SELECT * FROM users")
    #users = list(c.fetchall())

    ## Close connection
    #conn.close()
    ## Return resulting HTML
    #return render_template('page 3.html', users=users)


#@app.route('/user/<login>/')
#def user_page(login):
    #conn = sqlite3.connect('app.db')
    #conn.row_factory = dict_factory
    #c = conn.cursor()

    ## Handler logic here
    #c.execute("SELECT * FROM users WHERE login='%s'" % login)
    #user_data = c.fetchone()

    ## Close connection
    #conn.close()
    #return render_template("userpage.html", user=user_data)


#@app.route('/add_user', methods=['GET', 'POST'])
#def add_user():

    #user_created = False
    #error_message = ""

    #if request.method == 'POST':
        ## add new user data
        #user = {}
        #user['login'] = request.form.get('login')
        #user['name'] = request.form.get('name')
        #user['gender'] = request.form.get('gender')
        #user['city'] = request.form.get('city')
        #user['preferences'] = request.form.get('preferences')
        #user['photo'] = request.form.get('photo')

        ## save to database
        #conn = sqlite3.connect('app.db')
        #c = conn.cursor()
        #c.execute("SELECT * FROM users where login='%s'" % user['login'])
        #if c.fetchone():
            ## user with this login is already in my database
            #error_message = "user_exists"
        #else:
            #c.execute("INSERT INTO users "
                      #"(login, name, gender, city, preferences, photo) "
                      #"VALUES "
                      #"('{login}','{name}','{gender}','{city}','{preferences}','{photo}')"
                      #"".format(**user))
            #conn.commit()
            #user_created = True
        #conn.close()
        ## redirect to user page
        ## return redirect('/user/%s/' % user['login'])


    #return render_template(
        #"add_user.html",
        #user_created=user_created,
        #error_message=error_message
    #)


#@app.route('/search')
#def search_for_person():
    #q = request.args.get('query')
    #users = us.get_users_by_name(q)
    #return render_template('search_results.html', q=q, users=users)



app.run()

