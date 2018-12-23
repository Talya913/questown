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
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(2), default='')
    age = db.Column(db.Integer, default='')
    groups = db.relationship('Groups', backref='initiator', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.gender}', '{self.age}', '{self.preferences}', '{self.current_groups})"


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    quest_name = db.Column(db.String(20), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quests.id'), nullable=False)
    pref_party = db.Column(db.Boolean)
    pref_drunk = db.Column(db.Boolean)
    pref_afterparty = db.Column(db.Boolean)
    pref_sociable = db.Column(db.Boolean)
    pref_crazy = db.Column(db.Boolean)
    inviter = db.Column(db.String(20), db.ForeignKey('users.id'), nullable='False')


class Quests(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    groups = db.Column(db.String(120))
