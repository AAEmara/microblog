#!/usr/bin/python
"""routes Module."""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """Returning the index page."""
    user = {"username": "Emara"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        },
        {
            "author": {"username": "Emara"},
            "body": "I love Python <3"
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Returns a rendered template for the login page."""
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
