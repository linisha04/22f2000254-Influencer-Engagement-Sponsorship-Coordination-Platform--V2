from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin , UserMixin

db= SQLAlchemy()

class Role(db.Model , RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer()  , nullable = False ,autoincrement=True  , primary_key=True)
    name=db.Column(db.String() , nullable=False)

class Influencer(db.Model):
    __tablename__ = "Influencer" 
    id=db.Column(db.Integer() ,autoincrement=True, primary_key=True , nullable=False)
    username=db.Column(db.String() , nullable=False , unique=True)
    password=db.Column(db.String() , nullable=False)
    followers=db.Column(db.Integer()  , default=5000)
    niche=db.Column(db.String(), nullable=False)
    contact=db.Column(db.String(), nullable=False)
    earnings=db.Column(db.Integer() , default=0 )
    flagged=db.Column(db.Boolean(), default=False)
    bio=db.Column(db.String(), default='Write Something....')
    fs_uniquifier= db.Column(db.String(), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'), nullable=False)
    role = db.relationship('Role', backref='influencer')
   
   
    

        
class Sponsor(db.Model):
    __tablename__ = "Sponsor" 
    id=db.Column(db.Integer() ,autoincrement=True, primary_key=True ,  nullable=False)
    company_name=db.Column(db.String(),unique=True, nullable=False )
    password=db.Column(db.String() , nullable=False)
    industry=db.Column(db.String())
    contact=db.Column(db.String(), nullable=False)
    flagged=db.Column(db.Boolean(), default=False)
    approved=db.Column(db.Boolean , default=False)
    budget=db.Column(db.Integer() , default=0)
    fs_uniquifier =db.Column(db.String(), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'), nullable=False)
    role = db.relationship('Role', backref='Sponsor')
   
    

class Admin(db.Model ):
    __tablename__ = "Admin"
    id=db.Column(db.Integer(), primary_key=True , autoincrement=True)
    username=db.Column(db.String(),unique=True, nullable=False )
    password=db.Column(db.String() , nullable=False)
    role = db.relationship('Role', backref='admin')
    fs_uniquifier=db.Column(db.String(), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'), nullable=False)

    