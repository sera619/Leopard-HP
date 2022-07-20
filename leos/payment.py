import os
import logging
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, Blueprint
from flask.helpers import url_for

load_dotenv()

payment = Blueprint('payment', __name__)

@payment.route('/spend-confirm', methods=["POST", "GET"])
def spend_confirm():
    pass
