# from celery import Celery, Task
from application.models import db , User , Influencer , Sponsor , AdRequest , Campaign
from celery import shared_task
import requests
import os
import time
import smtplib
from email.mime.text import MIMEText
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from csv import DictWriter
from io import StringIO
from sqlalchemy.sql import func

@shared_task
def hello():
   
    time.sleep(10)
   
    return "Hello"

@shared_task
def daily_reminders():
    smtpObject=smtplib.SMTP('localhost',1025)
    template_path = os.path.join(os.path.dirname(__file__), "templates", "dailyReminder.html")
    with open(template_path) as file:
        content = Template(file.read())
    for user in User.query.all():
        email=MIMEMultipart()
        email["TO"]=user.username
        email["FROM"]="admin@gmail.com"
        email["SUBJECT"]=f"Daily Reminder - Pending Adrequests - {user.username}"
        if  'influencer'  in user.get_roles():
            reqs=AdRequest.query.filter_by(sent_to=user.id , status="pending").count()
            if reqs>0:
                html=MIMEText(content.render(user=user, reqs_count=reqs),'html')
                email.attach(html)
                smtpObject.sendmail("admin@gmail.com" , user.username, email.as_string())
               
            
@shared_task
def monthlyReport():
    smtpObject=smtplib.SMTP('localhost',1025)
    template_path = os.path.join(os.path.dirname(__file__), "templates", "montlyReport.html")
    with open(template_path) as file:
        content = Template(file.read())
    for user in User.query.all():
        email=MIMEMultipart()
        email["TO"]=user.username
        email["FROM"]="admin@gmail.com"
        email["SUBJECT"]=f" Monthly Report - Information - {user.username}"
        
        if  'sponsor'  in user.get_roles():
            campaigns=[]
            camps=Campaign.query.filter_by(sponsor_id=user.id).all()
            if camps:
                for camp in camps:
                    campaigns.append(
                    {
                     "id":camp.id,
                     "campaignName":camp.campaignName,
                     "visibility":camp.visibility,
                     "visibility":camp.visibility,
                     "niche":camp.niche,
                     "goals":camp.goals})
                html=MIMEText(content.render(user=user, campaigns=campaigns),'html')    
                email.attach(html)
                smtpObject.sendmail("admin@gmail.com" , user.username, email.as_string())
                    
        
@shared_task
def export_csv(id):
    file=StringIO()
    writer=DictWriter(file , fieldnames=["campaignName","id","visibility","budget","niche","goals"])
    writer.writeheader()
    for camp in  Campaign.query.filter_by(sponsor_id=id).all():
        writer.writerow({
            "campaignName":camp.campaignName,
            "id":camp.id,
            "visibility":camp.visibility,
            "visibility":camp.visibility,
            "niche":camp.niche,
            "goals":camp.goals})
    file.seek(0)
    result=file.read()
    print(result)
    return result