from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash
from application.utils import celery_init_app
from application.worker import daily_reminders , monthlyReport
from celery.schedules import crontab


def create_app():
    from application.models import db , Sponsor , Influencer  , Role , User  
    from application.routes import api
    from application.cache import cache

    app=Flask(__name__)
    app.config['SECRET_KEY']='qwertyui'
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project_iESCP.db"
    app.config["CELERY"] = {"broker_url": "redis://localhost",
                            # "result_backend": "redis://localhost",
                             "result_backend": "redis://localhost",
                            "broker_connection_retry_on_startup": True}
    
   
    db.init_app(app)
   
    CORS(app, resources={r"/*": {"origins": "*"}}) 
    cache.init_app(app)
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security=Security(app,datastore)  
   
   
    with app.app_context():
        db.create_all()


        if not Role.query.filter_by(name="admin").first():
            role_admin=app.security.datastore.create_role(name="admin")
            user_admin=app.security.datastore.create_user(email="admin@gmail.com", username="admin" , password=generate_password_hash("admin"))
            app.security.datastore.add_role_to_user(user_admin,role_admin)
            
       
            app.security.datastore.create_role(name="sponsor")
    
            app.security.datastore.create_role(name="influencer")
            db.session.commit()
                            
      

    app.register_blueprint(api)      

  


    return app

app = create_app()
celery = celery_init_app(app)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from application.worker import daily_reminders

    sender.add_periodic_task(crontab(minute="*"), daily_reminders.s(), name="say hello")
    sender.add_periodic_task(crontab(minute="*"), monthlyReport.s(), name="montly hello")
    # sender.add_periodic_task(crontab(day_of_month="*"), monthlyReport.s(), name="montly hello")

if __name__ == "__main__":
    # app=create_app()
    # celery=celery_init_app(app)  

    app.run(debug=True)