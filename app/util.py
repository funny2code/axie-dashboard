# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
""" 
from flask   import json, url_for, jsonify, render_template
from jinja2  import TemplateNotFound
from app     import app

from . models import User
from app    import app,db,bc,mail
from . common import *
from sqlalchemy import desc,or_
import hashlib
from flask_mail  import Message
import re
from flask       import render_template """


""" 
import      os, datetime, time, random

# build a Json response
def response( data ):
    return app.response_class( response=json.dumps(data),
                               status=200,
                               mimetype='application/json' )

def g_db_commit( ):

    db.session.commit( );    

def g_db_add( obj ):

    if obj:
        db.session.add ( obj )

def g_db_del( obj ):

    if obj:
        db.session.delete ( obj )
"""


from urllib.request import urlopen
import json

#Uses coingecko to get the current value in json and parse it.
#Default currency is PHP which is what the scholars use, but you can change it to whatever you need.
def getRateForSLP(currency="gbp"):
    currency=currency.lower() #avoinds keyerror if given in caps

    slp_token = "0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25" #Token for the crypto we're using. Don't change this.

    url = f"https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses={slp_token}&vs_currencies={currency}"

    with urlopen(url) as url:
        statsData = json.loads(url.read().decode())
        value = statsData[slp_token][currency]

    return(value)

