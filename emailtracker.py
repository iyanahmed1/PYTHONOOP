#python program to create email accounts across services
#install holehe
import subprocess
def check_email(email):
    results=subprocess.run(['holehe',email],capture_output=True,text=True)
    return results.stdout

email=input('Enter Your Email: ')
response= check_email(email)
print(response)
