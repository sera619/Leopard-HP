from flask import Flask, render_template, flash, url_for
import os
import logging
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('FS')
    #logging.basicConfig(filename='website.log', format='%(asctime)s %(message)s', datefmt='%d|%m|%Y - %I:%M:%S %p', level=logging.DEBUG)

    from leos.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

load_dotenv()
app = create_app()