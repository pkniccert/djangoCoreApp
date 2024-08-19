from .models import Student
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def run_this_function():
    # Student.objects.create(name="Pavan Kumar1", email="pkniccert@gmail.com", phone=9536955038, age=31, address="Greater Noida", file="")
    print("Function Started")
    time.sleep(2)
    print("Funtion Executed")


def send_email_to_client():
  try:
    subject = "This is django test mail"
    message = "Hi Pavan, This is django test mail."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["pkumarrathor@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)
  except Exception as e:
     print(e)

def send_email_with_attachement(subject, message, recipient_list, file_path):
    try:
        mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
        mail.attach_file(file_path)
        mail.send()
    except Exception as e:
     print(e)
    

