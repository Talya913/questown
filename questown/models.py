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
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    about = db.Column(db.String(1000), default='I am new here and will write something about me soon.')
    groups = db.relationship('Groups', backref='initiator', lazy=True)


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    quest_name = db.Column(db.String(20), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quests.id'), nullable=False)
    gender = db.Column(db.String(10))
    agemin = db.Column(db.Integer)
    agemax = db.Column(db.Integer)
    init_age = db.Column(db.String(10))
    init_gender = db.Column(db.Integer)
    init_name = db.Column(db.String(20))
    participants = db.Column(db.Integer, db.ForeignKey('users.id'), nullable='False')


class Quests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='1.jpg')
    address = db.Column(db.String(50))
    feat_adventure = db.Column(db.Integer)
    feat_horror = db.Column(db.Integer)
    feat_logic = db.Column(db.Integer)
    feat_intelligent = db.Column(db.Integer)
    feat_silly = db.Column(db.Integer)
    feat_dirty = db.Column(db.Integer)
    feat_romantic = db.Column(db.Integer)
    feat_drama = db.Column(db.Integer)
    link = db.Column(db.String(50))


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    feat_adventure = db.Column(db.Integer)
    feat_horror = db.Column(db.Integer)
    feat_logic = db.Column(db.Integer)
    feat_intelligent = db.Column(db.Integer)
    feat_silly = db.Column(db.Integer)
    feat_dirty = db.Column(db.Integer)
    feat_romantic = db.Column(db.Integer)
    feat_drama = db.Column(db.Integer)
    pref_adventure = db.Column(db.Integer)
    pref_horror = db.Column(db.Integer)
    pref_logic = db.Column(db.Integer)
    pref_intelligent = db.Column(db.Integer)
    pref_silly = db.Column(db.Integer)
    pref_dirty = db.Column(db.Integer)
    pref_romantic = db.Column(db.Integer)
    pref_drama = db.Column(db.Integer)
    rating = db.Column(db.Integer)
