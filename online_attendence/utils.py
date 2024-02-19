import pyotp
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.conf import settings

def send_otp(request,username):
     totp=pyotp.TOTP(pyotp.random_base32(),interval=60)
     otp=totp.now()
     request.session['secrete_key']=totp.secret
     valid_date=datetime.now()+timedelta(minutes=1)
     request.session['valid_until']=str(valid_date)
     r=username+'@rguktong.ac.in'
     reciver=[r]
     msg='THIS IS A AUTO GENERATED MAIL IF YOU NOT WANT TO CHANGE PASSWORD PLEASE CONTACT EXAM CELL FOR HELP \n YOUR OTP IS '+otp+'\n\n DON\'T SHARE THIS OTP WITH ANY ONE'
     send_mail('OTP SENT BY ATTENDENCE SYSTEM ',msg,'settings.EMAIL_HOST_USER',reciver,fail_silently=False) 
