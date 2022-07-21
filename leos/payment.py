import email
from email import message
import os
import json
import logging
from unicodedata import name
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, Blueprint, request
from flask.helpers import url_for

from leos.models import Payments
from .main import main
from datetime import date, datetime
from . import DB

load_dotenv()

payment = Blueprint('payment', __name__)

@payment.route('/spend-confirm', methods=["POST", "GET"])
def spend_confirm():
    payment_time = datetime.now()
    user_name = request.form.get('inputName')
    user_mail = request.form.get('inputEmail',type=str)
    pay_value = request.form.getlist('pay-value')
    message_user = request.form.get('inputMessage')
    if message_user == "":
        message_user = "NO MESSAGE"
    payment_data = {
        
        "User-Name": user_name,
        "User-Mail": user_mail,
        "Payment-Value":pay_value,
        "Payment-Message": message_user,
        "Payment-Time": str(payment_time)
        #TODO: add payment method to save 
        }
    save_payment_data(payment_data)

    # add payment data to DB
    new_payment = Payments(name = user_name,
    email = user_mail,
    payment_value = int(pay_value[0]),
    message = message_user,
    paytime = str(payment_time)
    )
    DB.session.add(new_payment)
    DB.session.commit()

    flash(f'Spende von "{user_name}" über {pay_value},00 € ist erfolgreich abgeschlossen\nVielen herzlichen Dank im Namen aller Tiere und dem Team!')

    return redirect('/spenden')







def save_payment_data(paymentdata):
    with open("logs/payment-log.log", "a") as f:
        f.writelines(json.dumps(paymentdata))
