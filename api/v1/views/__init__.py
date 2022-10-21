#!/usr/bin/python3
""""creating blue print for flask rest api routing"""
from flask import Blueprint

app_views = Blueprint('app_views', url_prefix='/api/v1')

if app_views is