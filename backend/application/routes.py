from flask import Blueprint, request , redirect, url_for ,jsonify
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash 
from flask_security import Security, login_user , roles_required ,auth_required ,roles_accepted ,login_required,current_user
from .models import Influencer, Sponsor, User, db,   Role,Campaign,AdRequest
from flask_cors import cross_origin


api=Blueprint("api",__name__)


@api.route("/")
@cross_origin(origin='http://localhost:5173')
def index():
    return "Hello, World!"




@api.route("/signin", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username:
        return {"message": "Check Username"}, 400
    if not password:
        return {"message": "Check password"}, 400

    user = app.security.datastore.find_user(username=username)
    
    if not user:
        return {"message": "User not found"}, 404
    login_user(user, remember=True)
    
     
    return {"token": user.get_auth_token(),
            "roles": user.get_roles()}
            


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
    user_role=app.security.datastore.find_role('influencer')
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

    
@api.route("/userInfo" , methods=['GET'])
@cross_origin(origin='http://localhost:5173')
@auth_required('token')
def userInfo():
    userRoles=[role for role in current_user.get_roles()]
    user_info = {
        "username": current_user.username,
        "email": current_user.email,
        "roles": userRoles
    }
    user_=db.session.query(User).filter_by(username=current_user.username).first()
    if 'sponsor' in userRoles:
        curr_sponsor = db.session.query(Sponsor).filter_by(id=user_.id).first()
        user_info['id']=curr_sponsor.id
        user_info['industry']=curr_sponsor.industry
        user_info['name']=curr_sponsor.name
        user_info['budget']=curr_sponsor.budget
    if 'influencer' in userRoles:
        curr_sponsor = db.session.query(Influencer).filter_by(id=user_.id).first()
        user_info['id']=curr_sponsor.id
        user_info['followers']=curr_sponsor.followers
        user_info['niche']=curr_sponsor.niche
        user_info['bio']=curr_sponsor.bio
    return jsonify(user_info)
   


    
@api.route("/sponsorDashboard",methods=['GET' , 'POST'])
@cross_origin(origin='http://localhost:5173')
@roles_required('sponsor')
def sponsor_Dashboard():
    return {"message":"This is dashboard for sponsor"}, 201
    

    
@api.route("/createCampaign",methods=['POST'])
@cross_origin(origin='http://localhost:5173/createCampaign')
@login_required
@auth_required('token')
@roles_required("sponsor")
def createCampaign():
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


@api.route("/viewCampaign")
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted('sponsor', 'influencer')
def viewCampaign():
    userRoles=[role for role in current_user.get_roles()]
    if 'sponsor' in userRoles:
        id=current_user.id
        campaigns=db.session.query(Campaign).filter_by(sponsor_id=id).all()
        return campaigns , 201
    elif 'influencer' in userRoles:
        campaigns=db.session.query(Campaign).filter_by(visibility="public").all()
        return campaigns , 201
    else:
        result={}
        campaigns=db.session.query(Campaign).all()
        number_of_camp=len(campaigns)
        result['number_of_camp']=number_of_camp
        public_camp=db.session.query(Campaign).filter_by(visibility="public").all()
        number_of_public_camp=len(public_camp)
        result['number_of_public_camp']=number_of_public_camp
        private_camp=db.session.query(Campaign).filter_by(visibility="private").all()
        number_of_private_camp=len(private_camp)
        result['number_of_private_camp']=number_of_private_camp
        return result , 201
    
    return {"message" : "Some Problem may be "} , 404
        
    



@api.route("/dashboardInfluencer")
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted("influencer")
def dashboardInfluencer():
    return {"message":"Influencer Dashboard"}, 201



