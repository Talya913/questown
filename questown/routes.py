from flask import flash, redirect, url_for, render_template, request, abort
from questown.forms import RegistrationForm, LoginForm, UpdateAccountForm, QuestSearchForm, GroupForm
from questown.models import Users, Quests, Search, Groups
from questown import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import numpy as np
import secrets
import os


#db.drop_all()
db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    searchform = QuestSearchForm()
    if request.method == 'POST':
        return search_results()
    return render_template('page1(1).html', form=searchform)


# @app.route('/results')
# def search_results():
#     searchform = QuestSearchForm()
#
#     Search.name = Quests.name
#     Search.description = Quests.description
#     Search.feat_adventure = Quests.feat_adventure
#     Search.feat_dirty = Quests.feat_dirty
#     Search.feat_drama = Quests.feat_drama
#     Search.feat_horror = Quests.feat_horror
#     Search.feat_intelligent = Quests.feat_intelligent
#     Search.feat_logic = Quests.feat_logic
#     Search.feat_silly = Quests.feat_silly
#     Search.feat_romantic = Quests.feat_romantic
#     Search.pref_adventure = searchform.adventure.data
#     Search.pref_dirty = searchform.dirty.data
#     Search.pref_drama = searchform.drama.data
#     Search.pref_horror = searchform.horror.data
#     Search.pref_intelligent = searchform.intelligent.data
#     Search.pref_logic = searchform.logic.data
#     Search.pref_silly = searchform.silly
#     Search.pref_romantic = searchform.romantic
#     Search.rating = np.where(
#         np.array(Search.pref_adventure) == 1, np.array(Search.rating) + np.array(Search.feat_adventure) * (-10), np.where(
#             np.array(Search.pref_adventure) == 2, np.array(Search.rating) + np.array(Search.feat_adventure) * (-5), np.where(
#                 np.array(Search.pref_adventure) == 3, np.array(Search.rating) + np.array(Search.feat_adventure) * 1, np.where(
#                     np.array(Search.pref_adventure) == 4, np.array(Search.rating) + np.array(Search.feat_adventure) * 4, np.where(
#                         np.array(Search.pref_adventure) == 5, np.array(Search.rating) + np.array(Search.feat_adventure) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_dirty) == 1, np.array(Search.rating) + np.array(Search.feat_dirty) * (-10), np.where(
#             np.array(Search.pref_dirty) == 2, np.array(Search.rating) + np.array(Search.feat_dirty) * (-5), np.where(
#                 np.array(Search.pref_dirty) == 3, np.array(Search.rating) + np.array(Search.feat_dirty) * 1, np.where(
#                     np.array(Search.pref_dirty) == 4, np.array(Search.rating) + np.array(Search.feat_dirty) * 4, np.where(
#                         np.array(Search.pref_dirty) == 5, np.array(Search.rating) + np.array(Search.feat_dirty) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_drama) == 1, np.array(Search.rating) + np.array(Search.feat_drama) * (-10), np.where(
#             np.array(Search.pref_drama) == 2, np.array(Search.rating) + np.array(Search.feat_drama) * (-5), np.where(
#                 np.array(Search.pref_drama) == 3, np.array(Search.rating) + np.array(Search.feat_drama) * 1, np.where(
#                     np.array(Search.pref_drama) == 4, np.array(Search.rating) + np.array(Search.feat_drama) * 4, np.where(
#                         np.array(Search.pref_drama) == 5, np.array(Search.rating) + np.array(Search.feat_drama) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_horror) == 1, np.array(Search.rating) + np.array(Search.feat_horror) * (-10), np.where(
#             np.array(Search.pref_horror) == 2, np.array(Search.rating) + np.array(Search.feat_horror) * (-5), np.where(
#                 np.array(Search.pref_horror) == 3, np.array(Search.rating) + np.array(Search.feat_horror) * 1, np.where(
#                     np.array(Search.pref_horror) == 4, np.array(Search.rating) + np.array(Search.feat_horror) * 4, np.where(
#                         np.array(Search.pref_horror) == 5, np.array(Search.rating) + np.array(Search.feat_horror) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_intelligent) == 1, np.array(Search.rating) + np.array(Search.feat_intelligent) * (-10), np.where(
#             np.array(Search.pref_intelligent) == 2, np.array(Search.rating) + np.array(Search.feat_intelligent) * (-5), np.where(
#                 np.array(Search.pref_intelligent) == 3, np.array(Search.rating) + np.array(Search.feat_intelligent) * 1, np.where(
#                     np.array(Search.pref_intelligent) == 4, np.array(Search.rating) + np.array(Search.feat_intelligent) * 4, np.where(
#                         np.array(Search.pref_intelligent) == 5, np.array(Search.rating) + np.array(Search.feat_intelligent) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_logic) == 1, np.array(Search.rating) + np.array(Search.feat_logic) * (-10), np.where(
#             np.array(Search.pref_logic) == 2, np.array(Search.rating) + np.array(Search.feat_logic) * (-5), np.where(
#                 np.array(Search.pref_logic) == 3, np.array(Search.rating) + np.array(Search.feat_logic) * 1, np.where(
#                     np.array(Search.pref_logic) == 4, np.array(Search.rating) + np.array(Search.feat_logic) * 4, np.where(
#                         np.array(Search.pref_logic) == 5, np.array(Search.rating) + np.array(Search.feat_logic) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_silly) == 1, np.array(Search.rating) + np.array(Search.feat_silly) * (-10), np.where(
#             np.array(Search.pref_silly) == 2, np.array(Search.rating) + np.array(Search.feat_silly) * (-5), np.where(
#                 np.array(Search.pref_silly) == 3, np.array(Search.rating) + np.array(Search.feat_silly) * 1, np.where(
#                     np.array(Search.pref_silly) == 4, np.array(Search.rating) + np.array(Search.feat_silly) * 4, np.where(
#                         np.array(Search.pref_silly) == 5, np.array(Search.rating) + np.array(Search.feat_silly) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     Search.rating = np.where(
#         np.array(Search.pref_romantic) == 1, np.array(Search.rating) + np.array(Search.feat_romantic) * (-10), np.where(
#             np.array(Search.pref_romantic) == 2, np.array(Search.rating) + np.array(Search.feat_romantic) * (-5), np.where(
#                 np.array(Search.pref_romantic) == 3, np.array(Search.rating) + np.array(Search.feat_romantic) * 1, np.where(
#                     np.array(Search.pref_romantic) == 4, np.array(Search.rating) + np.array(Search.feat_romantic) * 4, np.where(
#                         np.array(Search.pref_romantic) == 5, np.array(Search.rating) + np.array(Search.feat_romantic) * 7, np.array(Search.rating)
#                     )
#                 )
#             )
#         )
#     )
#     quests = Search.query
#     if searchform.search.data != '':
#         quests = quests.filter(Search.name.like('%' + searchform.search.data + '%')
#                                .order_by(Search.rating.tostring()))
#     quests = quests.order_by(Search.rating.tostring()).all()
#     return render_template('search_results.html', quests=quests)


@app.route('/results')
def search_results():
    searchform = QuestSearchForm()
    quests = Quests.query

    if searchform.validate_on_submit():
        quests = quests.filter(Quests.name.like('%' + searchform.search.data + '%'))

    quests = quests.order_by(Quests.name).all()
    return render_template('search_results.html', quests=quests)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, name=form.name.data, age=form.age.data, gender=form.gender.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Access is denied. Incorrect email or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.gender = form.gender.data
        current_user.age = form.age.data
        current_user.about = form.about.data
        db.session.commit()
        flash('Your account information has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.name.data = current_user.name
        form.email.data = current_user.email
        form.gender.data = current_user.gender
        form.age.data = current_user.age
        form.about.data = current_user.about
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route('/user/<int:user_id>')
def user(user_id):
    user = Users.query.get_or_404(user_id)
    group = Groups.query
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('userpage.html', title=user.name, user=user, image_file=image_file, group=group)


@app.route('/quest/<int:quest_id>')
def quest(quest_id):
    quest = Quests.query.get_or_404(quest_id)
    image_file = url_for('static', filename='quest_pics/' + quest.image_file)
    return render_template('questpage.html', title=quest.name, quest=quest, image_file=image_file, quest_id=quest.id)


@app.route('/quest/<int:quest_id>/befound', methods=['GET', 'POST'])
@login_required
def find_a_partner(quest_id):
    quest = Quests.query.get_or_404(quest_id)
    form = GroupForm()
    if form.validate_on_submit():
        group = Groups(gender=form.gender.data, agemin=form.agemin.data, agemax=form.agemax.data,
                       initiator=current_user, quest_name=quest.name, quest_id=quest.id,
                       init_age=current_user.age, init_gender=current_user.gender, init_name=current_user.name)
        db.session.add(group)
        db.session.commit()
        flash('You successfully created a beacon, now chill out and wait for messages from others. Or try to find a party yourself', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.agemin.data = 1
        form.agemax.data = 100
    return render_template('create_beacon.html', title='Create a Beacon', form=form, quest=quest)


@app.route('/quest/<int:quest_id>/find', methods=['GET', 'POST'])
@login_required
def find_party(quest_id):
    quest = Quests.query
    form = GroupForm()
    if request.method == 'POST':
        return beacon_results(quest_id)
    return render_template('find_beacon.html', form=form, quest=quest)


@app.route('/quest/<int:quest_id>/behold')
@login_required
def beacon_results(quest_id):
    quest = Quests.query
    form = GroupForm()
    groups = Groups.query
    if form.validate_on_submit():
        groups = groups.filter(groups.quest_id == quest.id and
                               form.gender.data == groups.init_gender and
                               form.agemin.data <= groups.init_age and
                               form.agemax.data >= groups.init_age and
                               groups.gender == current_user.gender and
                               groups.agemin <= current_user.age and
                               groups.agemax >= current_user.age and
                               current_user.id != groups.participants)

    groups = groups.order_by(groups.id)
    return render_template('beacon_results.html', groups=groups, form=form, quest=quest)


@app.route('/beacon<int:group_id>/update', methods=['GET', 'POST'])
@login_required
def update_beacon(group_id):
    form = GroupForm()
    group = Groups.query.get_or_404(group_id)
    if group.initiator != current_user:
        abort(403)
    if form.validate_on_submit():
        group.gender = form.gender.data
        group.agemin = form.agemin.data
        group.agemax = form.agemax.data
        db.session.commit()
        flash('Changes have been saved', 'success')
        return redirect(url_for('account', group_id=group.id))
    elif request.method == 'GET':
        form.gender.data = group.gender
        form.agemin.data = group.agemin
        form.agemax.data = group.agemax
    return render_template('update_beacon.html', title='Beacon Update', form=form, group=group)


@app.route('/beacon<int:group_id>/delete', methods=['POST'])
@login_required
def delete_beacon(group_id):
    group = Groups.query.get_or_404(group_id)
    if group.initiator != current_user:
        abort(403)
    db.session.delete(group)
    db.session.commit()
    flash('The beacon has been deleted', 'info')
    return redirect(url_for('account'))
