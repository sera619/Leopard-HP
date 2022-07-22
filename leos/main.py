import os
import logging
from flask import Blueprint, render_template, flash, request, send_file
from flask.helpers import url_for
from werkzeug.utils import redirect
from dotenv import load_dotenv
from .util import WebTexts, animal_list

SITETITLE = "Seniorenresidenz für Showtiere"
load_dotenv()
main = Blueprint('main', __name__)


@main.route('/', methods=["POST", "GET"])
def home():
    logging.info("Besucher auf Homeseite")
    return render_template('home.html', site_title=SITETITLE)


@main.route("/home", methods=["POST", "GET"])
def index():
    logging.info("Besucher auf Startseite")
    return render_template("index.html", site_title= SITETITLE+" | Home")


@main.route('/entstehung', methods=["GET","POST"])
def entstehung():
    logging.info("Besucher auf Entstehung & Unterstützer")
    return render_template('entstehung.html', site_title=SITETITLE+" | Entstehung&Untersützer")

@main.route("/spenden", methods=["GET", "POST"])
def spend():
    card1_title = WebTexts.OWLTITLE
    card1_text = WebTexts.OWLTEXT
    card1_image_url = WebTexts.OWLIMAGEURL

    card2_title = WebTexts.DOGTITLE
    card2_text = WebTexts.DOGTEXT
    card2_image_url = WebTexts.DOGIMAGEURL
    logging.info("Besucher auf Spenden-Seite")
    return render_template("spends.html",
     site_title=SITETITLE +" | Spenen & Patenschaft",
     card_1_text = card1_text,
     card_1_title = card1_title,
     card_1_imageURL = card1_image_url,
     card_2_title = card2_title,
     card_2_text = card2_text,
     card_2_imageURL = card2_image_url
     )

@main.route("/tiere", methods=["POST", "GET"])
def tiere():
    title = SITETITLE+ " | Tiere"
    
    return render_template('animals.html', site_title= title, animaldict = animal_list)
    
