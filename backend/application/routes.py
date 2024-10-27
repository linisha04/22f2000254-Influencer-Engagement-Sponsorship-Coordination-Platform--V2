from flask import Blueprint, request , redirect, url_for ,jsonify
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash 
from flask_security import login_user , roles_required ,auth_required ,current_user
from .models import Influencer, Sponsor, User, db,   Role,Campaign,AdRequest
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request


api=Blueprint("api",__name__)


@api.route("/")
@cross_origin(origin='http://localhost:5173')
def index():
    return "Hello, World!"


@api.route("/signin" , methods=["POST"])
@cross_origin(origin='http://localhost:5173')
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    

    if not username:
        return {"message":"Check Username" }, 400
    if not password:
        return {"message":"Check password" }, 400
    
    user=app.security.datastore.find_user(username=username)

    if not user:
        return {"message": "User not found"} , 404
    if not check_password_hash(user.password , password):
        return {"message": "password wrong"} , 404
    
        
    login_user(user)  
    return {"token": user.get_auth_token(), "roles": user.get_roles()}

            


@api.route("/influencerRegister" , methods=['POST'])
@cross_origin(origin='http://localhost:5173')
def influencer_register():
    username=request.json.get("username")
    password=request.json.get("password")
    email=request.json.get("email")
    niche=request.json.get("niche")

    user=app.security.datastore.find_user(username=username)
    if user:
        return {"message" : "User already exists"} ,201
        

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
    user_role=app.security.datastore.find_role('infuencer')
    app.security.datastore.add_role_to_user(user , user_role)

    influencer = Influencer(id=user.id, niche=niche)
    db.session.add(influencer)
    
    db.session.commit()
    

    return {"message" : "Created  influencer sucessfully"} ,201
    

@api.route("/sponsorRegister" , methods=['POST'])
@cross_origin(origin='http://localhost:5173')
def sponsor_register():
    username=request.json.get("username")
    password=request.json.get("password")
    email=request.json.get("email")
    industry=request.json.get("industry")
    
    user=app.security.datastore.find_user(username=username)
    if user:
        return {"message" : "User already exists"} ,404
        

    if not username:
        return {"message":"Check Username" }, 400
    if not password:
        return {"message":"Check password" }, 400
    if not email:
        return {"message":"Check email" }, 400
    if not industry:
        return {"message":"Check industry" }, 400

    

    user = app.security.datastore.create_user(username=username , password=generate_password_hash(password) , email=email )
    user_role=app.security.datastore.find_role('sponsor')
    
    app.security.datastore.add_role_to_user(user , user_role)
    
    sponsor = Sponsor(id=user.id, industry=industry)
    db.session.add(sponsor)
    
    db.session.commit()
    return {"message": "Request successful , Sponsor created"}, 201

    
    
@api.route("/sponsorDashboard",methods=['GET' , 'POST'])
@cross_origin(origin='http://localhost:5173')
@roles_required('sponsor')
def sponsor_Dashboard():
    return {"message":"This is dashboard for sponsor"}, 201
    

    
@api.route("/createCampaign",methods=['POST'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_required("sponsor")
def createCampaign():
    print("Current User ID:", current_user.id)
    sponsor_id = current_user.id
    campaignName=request.json.get("campaignName")
    budget=request.json.get("budget")
    visibility=request.json.get("visibility")
    niche=request.json.get("niche")
    goals=request.json.get("goals")

    if( not campaignName or not  budget  or not visibility or not niche or not goals ):
        return {"message" : "Invalid Input"} , 400
    
    campaign = db.session.query(Campaign).filter_by(campaignName=campaignName).first()


   
    if campaign:
        return {"message" : "Enter new campaign name "} , 404

    campaign=Campaign(campaignName=campaignName,budget=budget  , visibility=visibility ,niche=niche , goals=goals ,sponsor_id=sponsor_id)
   
    db.session.add(campaign)
    db.session.commit()
    
    return {"message":"Campaign Created"}, 201

