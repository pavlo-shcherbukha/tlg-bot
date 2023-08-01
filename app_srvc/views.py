from datetime import datetime,timedelta
import flask 
from flask import Flask, render_template, request, jsonify, make_response
import json
import logging
import datetime
import sys
import traceback
import os
import time

import telebot
from app_srvc.Errors import AppError, AppValidationError, InvalidAPIUsage


application = Flask(__name__)
app_title="Сервіс Flask "




@application.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    """
        Rest Api Error  handler
    """
    r=e.to_dict()
    return json.dumps(r), e.status_code, {'Content-Type':'application/json'}

"""
    Simple logger
"""
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
def log( a_msg='NoMessage', a_label='logger' ):
	dttm = datetime.datetime.now()
	ls_dttm = dttm.strftime('%d-%m-%y %I:%M:%S %p')
	logging.info(' ['+ls_dttm+'] '+ a_label + ': '+ a_msg)
	print(' ['+ls_dttm+'] '+ a_label + ': '+ a_msg)

def add_cors_headers(response):
    """
        CORSA headers
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Content-Type"] = "applicaion/json"
    response.headers["Accept"] = "applicaion/json"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "DELETE,GET,POST"
    return response

@application.route("/")
def home():
    """
        Render main page
    """
    log("render home.html" )
    return render_template("home.html")

@application.route("/about/")
def about():
    """
        Render about pager
    """
    return render_template("about.html")



    






    


"""
   ===========================================================================
    *********** Rest API ******************************
    ===========================================================================
"""

@application.route("/api/health", methods=["GET"])
def health():
    """
        health check
    """
    label="health"
    log('Health check', label)
    result={ "ok": True,"app_title":app_title}
    log('Health check return result '+ json.dumps( result ), label)
    return json.dumps( result ), 200, {'Content-Type':'application/json'}

