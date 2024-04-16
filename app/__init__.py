#!/usr/bin/python3
"""app Module."""


from flask import Flask

app = Flask(__name__)

from app import routes
