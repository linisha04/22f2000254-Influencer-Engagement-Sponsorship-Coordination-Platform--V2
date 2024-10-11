from flask import Blueprint, request 
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash 
from flask_security import login_user
from .models import Influencer, Sponsor, db, Admin
from flask_login import current_user

api=Blueprint("api",__name__)


@api.route("/")
def index():
    return "Hello, World!"

@api.route("/influencerRegister")
def influencerRegister():
    return 'InfluencerRegister'

@api.route("/sponsorRegister")
def sponsorRegister():
    return 'sponsorRegister'


@api.route("/login")
def login():
    return 'logged'

