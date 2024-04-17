#!/usr/bin/python3
"""config Module"""


import os


class Config:
    """Defines the configuration of a flask application."""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
