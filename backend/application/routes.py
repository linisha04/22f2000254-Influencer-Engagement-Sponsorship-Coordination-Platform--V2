from flask import Blueprint, request , redirect, url_for
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash 
from flask_security import login_user
from .models import Influencer, Sponsor, User, db,   Role
from flask_login import current_user ,login_user, logout_user, login_required

api=Blueprint("api",__name__)


@api.route("/")
def index():
    return "Hello, World!"


@api.route("/signin" , methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    role=request.json.get("role")

    if not username:
        return {"message":"Check Username" }, 400
    if not password:
        return {"message":"Check password" }, 400
    if not role:
        return {"message":"Check role" }, 400

    if role=='admin':
        user=app.security.admin_Datastore.find_user(username=username)
        
    if role=='sponsor':
        user=app.security.sponsor_Datastore.find_user(company_name=username)

    if role=='influencer':
        user=app.security.sponsor_Datastore.find_user(username=username)

    if not user:
        return {"message": "User not found"} , 404
    if not check_password_hash(user.password , password):
        return {"message": "password wrong"} , 404
        
    login_user(user)  
    return {"token": user.get_auth_token(),"roles": user.get_roles()}
            


@api.route("/influencerRegister" , methods=['POST'])
def influencer_register():
    username=request.json.get("username")
    password=request.json.get("password")
    email=request.json.get("email")
    niche=request.json.get("niche")

    if not username:
        return {"message":"Check Username" }, 400
    if not password:
        return {"message":"Check password" }, 400
    if not email:
        return {"message":"Check email" }, 400
    if not niche:
        return {"message":"Check niche" }, 400
    
    if app.security.datastore.find_user(username=username):
        return {"message" : "Username already exists"}, 409

    
    user = app.security.datastore.create_user(username=username , password=generate_password_hash(password) , email=email )
    user_role=app.security.datastore.find_role(name='infuencer')
    app.security.datastore.add_role_to_user(user , user_role)

    influencer = Influencer(id=user.id, niche=niche)
    db.session.add(influencer)
    
    db.session.commit()
    

    return {"message" : "Created  influencer sucessfully"} ,201
    

@api.route("/sponsorRegister" , methods=['POST'])
def sponsor_register():
    username=request.json.get("username")
    password=request.json.get("password")
    email=request.json.get("email")
    industry=request.json.get("industry")

    if not username:
        return {"message":"Check Username" }, 400
    if not password:
        return {"message":"Check password" }, 400
    if not email:
        return {"message":"Check email" }, 400
    if not industry:
        return {"message":"Check industry" }, 400

    user = app.security.datastore.create_user(username=username , password=generate_password_hash(password) , email=email )
    user_role=app.security.datastore.find_role(name='sponsor')
    
    app.security.datastore.add_role_to_user(user , user_role)
    
    sponsor = Sponsor(id=user.id, industry=industry)
    db.session.add(sponsor)
    
    db.session.commit()

    
    

   
    
    
    