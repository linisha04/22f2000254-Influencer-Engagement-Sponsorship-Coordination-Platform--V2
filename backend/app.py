from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash

def create_app():
    from application.models import db , Sponsor , Influencer  , Role , User  
    from application.routes import api

    app=Flask(__name__)
    app.config['SECRET_KEY']='qwertyui'
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project_iESCP.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECURITY_PASSWORD_SALT'] = 'salty'

    CORS(app)  
   
    db.init_app(app)
    
    datastore = SQLAlchemyUserDatastore(db, User, Role)

    
    app.security=Security(app,datastore)
    with app.app_context():
        db.create_all()


        if not Role.query.filter_by(name="admin").first():
            role_admin=app.security.datastore.create_role(name="admin")
            user_admin=app.security.datastore.create_user(contact="admin@gmail.com", username="admin" , password=generate_password_hash("admin"))
            app.security.datastore.add_role_to_user(user_admin,role_admin)
            
       
            app.security.datastore.create_role(name="sponsor")
    
            app.security.datastore.create_role(name="influencer")
            db.session.commit()
                            
      

    app.register_blueprint(api)        


    return app

if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)