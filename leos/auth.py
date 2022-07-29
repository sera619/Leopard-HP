from flask import Blueprint
from tinydb import Query, TinyDB
import os
import json
import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

auth = Blueprint('auth', __name__)


class AuthDB:
    def __init__(self, init_dummies = False):
        self.db = TinyDB('leos\data\db-user.json')
        self.user_table = self.db.table('user')
        self.User = Query()
        if init_dummies:
            self.__add_dummies__()

    def __add_dummies__(self):
        User = Query()
        if (not self.user_table.contains(User.mail == "sera")):
            self.user_table.insert({
                "mail": "seraphinus619@gmail.com",
                "password": os.environ.get('AUTH_SERA'),
                "is_admin": "True" 
            })
    
    def get_users(self):
        db = {}
        with open('./leos/data/user.json') as f:
            db = json.load(f)
        return db