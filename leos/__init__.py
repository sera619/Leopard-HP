from flask import Flask, render_template, flash
from flask.helpers import url_for
import os
import logging
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


#DB = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('FS')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #logging.basicConfig(filename='website.log', format='%(asctime)s %(message)s', datefmt='%d|%m|%Y - %I:%M:%S %p', level=logging.DEBUG)

    #DB.init_app(app)
    from leos.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from leos.payment import payment as payment_blueprint
    app.register_blueprint(payment_blueprint)

    from leos.controls import controls as control_blueprint
    app.register_blueprint(control_blueprint) 

    #from leos.models import Payments

    return app

load_dotenv()
app = create_app()