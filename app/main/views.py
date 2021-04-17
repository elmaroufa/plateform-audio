from datetime import datetime
from flask import Flask, render_template,url_for,session,redirect
from ..models import User
from . import main
from .. import db

@main.route('/')
def index():
    return render_template('index.html')