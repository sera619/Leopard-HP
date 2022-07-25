import os
import logging
import json
import datetime
from flask import Blueprint, render_template, flash, request, send_file
from flask.helpers import url_for
from werkzeug.utils import redirect
from dotenv import load_dotenv

from .util import WebTexts, animal_list, team_list, img_story
from .models import GuestBookDB, MemoryDB


main = Blueprint('main', __name__)

SITETITLE = "Seniorenresidenz für Showtiere"
load_dotenv()
guestbook_data = GuestBookDB(init_dummies=True)
memory_data = MemoryDB(init_dummies=True)


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

    return render_template('entstehung.html', site_title=SITETITLE+" | Entstehung&Untersützer", storyimages = img_story)

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

@main.route("/team", methods=["POST","GET"])
def team():
    title = SITETITLE + " | Team"
    return render_template('team.html', site_title = title, teamdict = team_list)



# guestbook 

@main.route("/gästebuch", methods=["POST", "GET"])
def guestbook():
    title = SITETITLE + " | Gästebuch"
    guestbook_db = guestbook_data.get_messages()
    gb_dict = {}
    gb_dict = guestbook_db['messages']
    print(guestbook_db['messages'])

    for key, value in guestbook_db['messages'].items():
        print(key, value['message_name'])

    return render_template('guestbook.html', site_title= title, guestbook_dict = gb_dict)

@main.route("/guestbook/new-entry", methods=["POST", "GET"])
def new_guestbook_entry():
    
    firstname =request.form.get('firstname')
    if (firstname == ""):
        flash('Bitte gebe einen Vornamen ein!')
        return redirect('/gästebuch')

    lastname = request.form.get('lastname')
    if lastname == "":
        flash('Bitte gebe einen Nachnamen ein!')
        return redirect('/gästebuch')

    new_message_name = str(firstname) + " " + str(lastname)
    new_message_email = request.form.get('email')
    if new_message_email == "":
        flash('Bitte gebe eine gültige Email Addresse ein!')
        return redirect('/gästebuch')
   
    new_message = request.form.get('guestbookMessage')
    if new_message == "":
        flash('Bitte gebe eine Nachricht Addresse ein!')
        return redirect('/gästebuch')
   
    new_message_time = datetime.datetime.now().strftime("%d-%m-%Y | %H:%M:%S %p")

    # save into db 
    guestbook_data.new_message(
        new_message_name=new_message_name,
        new_message_email=new_message_email,
        new_message_time= new_message_time,
        new_message=new_message
    )
    return redirect('/gästebuch')
#######################################################

######### MEMORY ############

@main.route("/memory", methods=["POST", "GET"])
def memory():
    title = SITETITLE + " | Memory"
    memory_db = memory_data.get_memory()
    mem_dict = {}
    mem_dict = memory_db['memory']
    print(memory_db['memory'])

    for key, value in memory_db['memory'].items():
        print(key, value['memory_title'])

    return render_template('memory.html', site_title= title, memory_dict = mem_dict)

