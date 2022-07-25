import os
import logging
import json
import datetime
from flask import Blueprint, render_template, flash, request, redirect
from flask.helpers import url_for

from .main import memory_data, guestbook_data,SITETITLE

controls = Blueprint('controls', __name__)

@controls.route('/controls', methods=["POST", "GET"])
def control_site():

    gb_db = guestbook_data.get_messages()
    gb_dict = {}
    gb_dict = gb_db['messages']


    logging.info("User auf der Controllseite")
    return render_template('control.html', site_title = SITETITLE + " | Controls", messages_dict = gb_dict)
