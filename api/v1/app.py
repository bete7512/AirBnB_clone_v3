#!/usr/bin/python3
""""flask app starter"""
from flask import Flask,make_response ,jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS,cross_origin

app=Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear(self):
    ''''''''
    storage.close()