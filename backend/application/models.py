from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin , UserMixin

db= SQLAlchemy()

class Role(db.Model , RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer()  , nullable = False ,autoincrement=True  , primary_key=True)
    name=db.Column(db.String() , nullable=False , unique=True)
    def get_roles(self):
        return [role.name for role in self.roles]

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
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='RoleVsUser',
                         backref=db.backref('users', lazy='dynamic'))
    

    influencer = db.relationship('Influencer', backref='user',uselist=False)
    sponsor=db.relationship('Sponsor', backref='user', uselist=False)

    

class Influencer(db.Model ,UserMixin):
    __tablename__ = "Influencer" 
    id=db.Column(db.Integer(),db.ForeignKey('User.id') , primary_key=True , nullable=False )
   
    followers=db.Column(db.Integer()  , default=5000)
    niche=db.Column(db.String(), nullable=True)
    earnings=db.Column(db.Integer() , default=0,nullable=True)
    flagged=db.Column(db.Boolean(), default=False,nullable=True)
    bio=db.Column(db.String(), default='Write Something....')
   
   
   
    

        
class Sponsor(db.Model , UserMixin):
    __tablename__ = "Sponsor" 
    id=db.Column(db.Integer(),db.ForeignKey('User.id') ,autoincrement=True, primary_key=True ,  nullable=False)
   
    
    industry=db.Column(db.String())
    flagged=db.Column(db.Boolean(), default=False)
    approved=db.Column(db.Boolean , default=False)
    budget=db.Column(db.Integer() , default=0)
   
    

