import os
import logging
from flask import Blueprint, render_template, flash, request, send_file
from flask.helpers import url_for
from werkzeug.utils import redirect
from dotenv import load_dotenv


load_dotenv()
main = Blueprint('main', __name__)


@main.route('/', methods=["POST", "GET"])
def home():
    logging.info("Besucher auf Homeseite")
    return render_template('home.html', site_title="Seniorenresidenz für Showtiere")


@main.route("/home", methods=["POST", "GET"])
def index():
    logging.info("Besucher auf Startseite")
    return render_template("index.html", site_title="Seniorenresidenz für Showtiere | Home")


@main.route('/entstehung', methods=["GET","POST"])
def entstehung():
    logging.info("Besucher auf Entstehung & Unterstützer")
    return render_template('entstehung.html', site_title="Seniorenresidenz für Showtiere | Entstehung&Untersützer")

@main.route("/spenden", methods=["GET", "POST"])
def spend():
    logging.info("Besucher auf Spenden-Seite")
    return render_template("spends.html", site_title="Seniorenresidenz für Showtiere | Spenen & Patenschaft")

@main.route("/tiere", methods=["POST", "GET"])
def unsere_tiere():
    pass