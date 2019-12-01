## B5) Test a website for its availability. Send mail if the site is down.

## Please install requests.
## Please fill in sender's email ID and password in place of "username@gmail.com" and "password".

website = input("Website: ") # Enter full URL.
receiver = input("Email: ")

import requests
if requests.get(website).status_code == 200:
	quit()
	
import smtplib
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls()

# Authentication 
session.login("username@gmail.com", "password") 
 
# sending the mail 
session.sendmail("username@gmail.com", receiver, "Website Down.") # For some reason, including the website in the message didn't work--the email sent would be completely empty.
  
# terminating the session 
session.quit() 
