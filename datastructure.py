# crud 
from user import User
users = {}

default_user = User(1, "brian", 22)
users[default_user.id] = default_user


def creating(user):
    users[user.id] = user

def updating():
    pass

def get_user_by(id):
    return users[id]
