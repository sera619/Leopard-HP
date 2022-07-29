import os
import logging
import json
import datetime
from flask import Blueprint, render_template, flash, request, redirect
from flask.helpers import url_for

from .main import memory_data, guestbook_data,SITETITLE
from .auth import AuthDB
controls = Blueprint('controls', __name__)

auth_db = AuthDB(init_dummies=True)

@controls.route('/controls/home', methods=["POST", "GET"])
def control_site():

    mail = request.form.get('input_mail')
    password = request.form.get('input_password')
    
    if not auth_db.user_table.contains(auth_db.User.mail == mail) or not auth_db.user_table.contains(auth_db.User.password == password):
        flash('Dieser Benutzer ist nicht bekannt.')
        return redirect('/controls')



    gb_db = guestbook_data.get_messages()
    gb_dict = {}
    gb_dict = gb_db['messages']
    title = SITETITLE + " | Controls"

    logging.info("User auf der Controllseite")
    return render_template('control.html', site_title = title , messages_dict = gb_dict)



@controls.route('/controls/change_message', methods=["POST", "GET"])
def change_message():
    


    pass


@controls.route('/controls', methods=["POST", "GET"])
def control_auth():
    title = SITETITLE + " | Controls"
    gb_db = guestbook_data.get_messages()
    gb_dict = {}
    gb_dict = gb_db['messages']


    return render_template('control-login.html',
    site_title = title,
    messages_dict = gb_dict)