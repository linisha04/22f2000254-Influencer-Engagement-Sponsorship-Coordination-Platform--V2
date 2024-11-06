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
        user_info['approved']=curr_sponsor.approved
        
    if 'influencer' in userRoles:
        curr_sponsor = db.session.query(Influencer).filter_by(id=user_.id).first()
        user_info['id']=curr_sponsor.id
        user_info['followers']=curr_sponsor.followers
        user_info['niche']=curr_sponsor.niche
        user_info['bio']=curr_sponsor.bio
        user_info['earnings']=curr_sponsor.earnings
    return jsonify(user_info)
   


    
@api.route("/sponsorDashboard",methods=['GET' , 'POST'])
@cross_origin(origin='http://localhost:5173')
@roles_required('sponsor')
def sponsor_Dashboard():
    # curr_user=db.session.query(User).filter_by(username=current_user.username).first()
    sponsor=db.session.query(Sponsor).filter_by(id=current_user.id).first()
    if not sponsor:
        return{"message":"Sponsor Not Exists"} , 404
    if sponsor.approved==False:
        return {"message":"Not Approved Yet"}, 403
    return {"message":"Approved"}, 201
    

    
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
@roles_accepted('sponsor')
def viewCampaign():
    userRoles=[role for role in current_user.get_roles()]
    if 'sponsor' in userRoles:
        all_campaigns=[]
        id=current_user.id
        campaigns=db.session.query(Campaign).filter_by(sponsor_id=id).all()
        for camp in campaigns:
            all_campaigns.append({"id":camp.id  , "campaignName":camp.campaignName ,
                                  "sponsor_id":camp.sponsor_id , "visibility":camp.visibility ,
                                  "budget":camp.budget ,"niche":camp.niche,
                                  "goals":camp.goals})
            
        return all_campaigns , 200
    return {"message":"Influencer Dashboard"}, 400
   
       
    

@api.route('/deleteCampaign/<int:id>',methods=['DELETE'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted("sponsor")
def deleteCampagin(id):
    campaign=db.session.query(Campaign).filter_by(id=id).first()
    if not campaign:
        return {"message":"campaign not found"} , 404
    db.session.delete(campaign)
    db.session.commit()
    return {"message":"deleted"} ,200

@api.route("/dashboardInfluencer")
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted("influencer")
def dashboardInfluencer():
    return {"message":"Influencer Dashboard"}, 201


@api.route("/campaignsPublic",methods=['GET'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_required("influencer")
def publicCampaigns():
    userRoles=[role for role in current_user.get_roles()]
    if 'influencer' in userRoles:
        campaigns=db.session.query(Campaign).filter_by(visibility="public").all()
        all_public_campaigns=[]
        for camp in campaigns:
            all_public_campaigns.append({"id":camp.id  , "campaignName":camp.campaignName ,
                                  "sponsor_id":camp.sponsor_id , "visibility":camp.visibility ,
                                  "budget":camp.budget ,"niche":camp.niche,
                                  "goals":camp.goals})
        return all_public_campaigns , 200
    return {"message":"Influencer Dashboard"}, 400
        
    



@api.route("/adminDashboard")
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted("admin")
def adminDashboard():
    result={}
    sponsors=db.session.query(Sponsor).filter_by(approved=False).all()
    sponsors_to_approve=[]
    for i in sponsors:
        sponsors_to_approve.append({
            "id":i.id, "name":i.name , "industry":i.industry , "budget":i.budget , "approved":i.approved
            })
        
    result['sponsors_to_approve']=sponsors_to_approve
    campaigns=db.session.query(Campaign).all()
    number_of_camp=len(campaigns)
    result['number_of_camp']=number_of_camp
    public_camp=db.session.query(Campaign).filter_by(visibility="public").all()
    number_of_public_camp=len(public_camp)
    result['number_of_public_camp']=number_of_public_camp
    private_camp=db.session.query(Campaign).filter_by(visibility="private").all()
    number_of_private_camp=len(private_camp)
    result['number_of_private_camp']=number_of_private_camp
    return result , 200
    
    
        
@api.route("/approve_status/<int:sponsor_id>" , methods=[ 'POST'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted("admin")
def change_status(sponsor_id):
    new_status=request.json.get("approved")
    sponsor=db.session.query(Sponsor).filter_by(id=sponsor_id).first()
    if sponsor:
        sponsor.approved=new_status
        db.session.commit()
        return {"message":"change happened", "approved now is":new_status} , 201
    return {"message":"Sponsor not found"} , 404
    
    
@api.route("/getInfluencers")
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted('sponsor' or 'admin')
def getInfluencers():
    all_influencers=[]
    influencers=db.session.query(Influencer).all()
    for i in influencers:
        curr_user=db.session.query(User).filter_by(id=i.id).first()
        
        all_influencers.append({

            "id":i.id,
            "followers":i.followers,
            "niche":i.niche,
            "earnings":i.earnings,
            "bio":i.bio,
            "username":curr_user.username
            })
    return     all_influencers , 200
    
    
@api.route("/createAdrequest" , methods=['POST'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted('sponsor' or 'influencer')
def createAdrequest():
    role=[role for role in current_user.get_roles()]
    if 'sponsor' in role:   
        ad_name=request.json.get('name')
        amount=request.json.get('amount')
        requirements=request.json.get('requirements')
        influencer_id=request.json.get('influencer_id')
        campaign_id=request.json.get('campaign_id')
        created_by=current_user.id
        sent_to=influencer_id

        is_created=db.session.query(AdRequest).filter_by(created_by=created_by ,sent_to=sent_to,campaign_id=campaign_id ).first()
        if is_created:
            return {"message":"Request Already exists. Choose new influencer"} , 409
        else:
            adRequest=AdRequest(name=ad_name,amount=amount,requirements=requirements,influencer_id=influencer_id ,
                            campaign_id=campaign_id , created_by=created_by,sent_to=sent_to)
            db.session.add(adRequest)
            db.session.commit()
            return {"message":"Adrequest successfully created"} , 201
        
     
        
@api.route("/viewAdRequests/campaign_id/<int:id>" , methods=['GET'])
@cross_origin(origin='http://localhost:5173')
@auth_required("token")
@roles_accepted('sponsor' )
def getAdRequest(id):
    role=[role for role in current_user.get_roles()]
    if 'sponsor' in role:
        reqs=db.session.query(AdRequest).filter_by(campaign_id=id ).all()
        result_reqs=[]
        if reqs:
            print(reqs)
            for req in reqs:
                result_reqs.append({"id":req.id , "campaign_id":id , "name":req.name ,
                                    "influencer_id":req.influencer_id , "messages":req.messages ,
                                    "requirements":req.requirements,"amount":req.amount,
                                    "status":req.status ,"created_by":req.created_by,"sent_to":req.sent_to
                    })
            return     result_reqs , 200
        return {"message":" No Adrequest "} , 404
    return {"message":" You r not sponsor "} , 404
        
                

        

