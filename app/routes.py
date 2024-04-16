#!/usr/bin/python
"""routes Module."""

from app import app


@app.route('/')
@app.route('/index')
def index():
    """Returning the index page."""
    return "Hello, World!"
