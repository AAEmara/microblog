#!/usr/bin/python3
"""config Module"""


import os


basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    """Defines the configuration of a flask application."""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
