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
    gender = db.Column(db.String(10), default='Not answered')
    age = db.Column(db.Integer, default='')
    about = db.Column(db.String(5000), default='I am new at this app and will write something here soon.')
    groups = db.relationship('Groups', backref='participates', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.gender}', '{self.age}', '{self.preferences}', '{self.current_groups})"


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    quest_name = db.Column(db.String(20), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quests.id'), nullable=False)
    pref_party = db.Column(db.String(5))
    pref_drunk = db.Column(db.String(5))
    pref_afterparty = db.Column(db.String(5))
    pref_sociable = db.Column(db.String(5))
    pref_crazy = db.Column(db.String(5))
    pref_age_min = db.Column(db.Integer)
    pref_age_max = db.Column(db.Integer)
    participants = db.Column(db.String(120), db.ForeignKey('users.id'), nullable='False')


class Quests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    feat_adventure = db.column(db.String(20))
    feat_horror = db.column(db.String(20))
    feat_logic = db.column(db.String(20))
    feat_intelligent = db.column(db.String(20))
    feat_silly = db.column(db.String(20))
    feat_dirty = db.column(db.String(20))
    feat_romantic = db.column(db.String(20))
    feat_drama = db.column(db.String(20))


#class Choice(db.model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(20))
