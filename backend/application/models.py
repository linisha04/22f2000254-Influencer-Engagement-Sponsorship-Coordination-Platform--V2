from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin , UserMixin

db= SQLAlchemy()

class Role(db.Model , RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer()  , nullable = False ,autoincrement=True  , primary_key=True)
    name=db.Column(db.String() , nullable=False , unique=True)
   
class RoleVsUser(db.Model):
    __tablename__ = 'RoleVsUser'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('User.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('Role.id'))

    

class User(db.Model, UserMixin):
    __tablename__ ='User'
    id=db.Column(db.Integer() ,autoincrement=True, primary_key=True , nullable=False)
    username=db.Column(db.String() , nullable=False , unique=True)
    password=db.Column(db.String() , nullable=False)
    email=db.Column(db.String() , nullable=False)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    active = db.Column(db.Boolean(),default=True)
    roles = db.relationship('Role', secondary='RoleVsUser',backref=db.backref('users', lazy='dynamic'))
    flagged=db.Column(db.Boolean(),default=False)
   
    

    influencer = db.relationship('Influencer', backref='user',uselist=False)
    sponsor=db.relationship('Sponsor', backref='user', lazy=True)

    def get_roles(self):
        return [role.name for role in self.roles]


    

class Influencer(db.Model ,UserMixin):
    __tablename__ = "Influencer" 
    id=db.Column(db.Integer(),db.ForeignKey('User.id') , primary_key=True , nullable=False )
   
    followers=db.Column(db.Integer()  , default=5000)
    niche=db.Column(db.String(), nullable=True)
    earnings=db.Column(db.Integer() , default=0,nullable=True)
    flagged=db.Column(db.Boolean(), default=False,nullable=True)
    bio=db.Column(db.String(), default='Write Something....')

    adRequest = db.relationship('AdRequest', backref='influencer', lazy=True)
    
   
   
   
    

        
class Sponsor(db.Model , UserMixin):
    __tablename__ = "Sponsor" 
    id=db.Column(db.Integer(),db.ForeignKey('User.id') ,autoincrement=True, primary_key=True ,  nullable=False)
    name=db.Column(db.String(), default='Name your company')
    industry=db.Column(db.String())
    approved=db.Column(db.Boolean , default=False)
    budget=db.Column(db.Integer() , default=0)
    campaign=db.relationship('Campaign', backref='sponsor', lazy=True)
   
    

class Campaign(db.Model):
    __tablename__ = "Campaign"
    id=db.Column(db.Integer() , primary_key=True , autoincrement=True , nullable=False)
    campaignName=db.Column(db.String(),nullable=False , unique=True)
    sponsor_id = db.Column(db.Integer(), db.ForeignKey('Sponsor.id') , nullable=False)
    visibility=db.Column(db.String() , nullable=False)

    # start_date=db.Column(db.Date(), nullable=False)
    # end_date=db.Column(db.Date(), nullable=False)
    budget=db.Column(db.Integer(),nullable=False)
    niche=db.Column(db.String() , nullable=False )
    goals=db.Column(db.String(), default='Not Enough Details. Contact Sponsor')
   

    adRequest=db.relationship('AdRequest', backref='campaign',lazy=True)
  

class AdRequest(db.Model):
    __tablename__ = "AdRequest" 
    id=db.Column(db.Integer() , primary_key=True , autoincrement=True,nullable=False)
    campaign_id=db.Column(db.Integer(), db.ForeignKey('Campaign.id') , nullable=False)
    name=db.Column(db.String(),nullable=False, unique=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey('Influencer.id'),nullable=True)
    messages=db.Column(db.String(),default='Not Enough Details. Contact Sponsor')
    requirements=db.Column(db.String(),default='Not Enough Details. Contact Sponsor')
    amount=db.Column(db.Integer(),default=0)
    status=db.Column(db.String(),default="pending")
    created_by=db.Column(db.Integer(), nullable=False)
    sent_to=db.Column(db.Integer(),nullable=False)
    
    
    
   
    
 
 
    
    