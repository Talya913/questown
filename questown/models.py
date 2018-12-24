from questown import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(10), default='---')
    age = db.Column(db.Integer, default=1)
    about = db.Column(db.String(1000), default='I am new here and will write something here soon.')
    groups = db.relationship('Groups', backref='participates', lazy=True)


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    quest_name = db.Column(db.String(20), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quests.id'), nullable=False)
    pref_party = db.Column(db.String(10))
    pref_drunk = db.Column(db.String(10))
    pref_afterparty = db.Column(db.String(10))
    pref_sociable = db.Column(db.String(10))
    pref_crazy = db.Column(db.String(10))
    pref_age_min = db.Column(db.Integer, default=1)
    pref_age_max = db.Column(db.Integer, default=100)
    participants = db.Column(db.String(120), db.ForeignKey('users.id'), nullable='False')


class Quests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    feat_adventure = db.Column(db.String(20))
    feat_horror = db.Column(db.String(20))
    feat_logic = db.Column(db.String(20))
    feat_intelligent = db.Column(db.String(20))
    feat_silly = db.Column(db.String(20))
    feat_dirty = db.Column(db.String(20))
    feat_romantic = db.Column(db.String(20))
    feat_drama = db.Column(db.String(20))


