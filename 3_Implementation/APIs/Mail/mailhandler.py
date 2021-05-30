import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

with open('Mail/config.json','r') as cc:
    params = json.load(cc)["params"]

def verification_email(email,usertype):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(params["SENDER_EMAIL"],params["SENDER_PASS"]) 
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Email verification Recruitment Portal"
        message["From"] = params["SENDER_EMAIL"]
        message["To"] = email
        link = "http://"+params["ip"]+":8088/accountverification?email="+email+"&usertype="+usertype
        html = '''
            <html>
            <head>
                <style>
                .button {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                }

                .button1 {
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
                }
            </style>
            </head>
            <body>
                <p>Congratulations!!!<br>
                Dear '''+usertype +'''<br>
                Your account has been created succesfully on Recruitment Portal</p>
                <p> <b>Click on below to verify your account</b> </p>
                <a href="'''+link+'''"><button class="button button1">Verify Account</button></a> 
                <br>
                <p>---<br>Thanks and Regards <br>Recruitment Portal <br>IIT Jammu</p> 
            </body>
            </html>
            '''
        part = MIMEText(html, "html")
        message.attach(part)
        s.sendmail(params["SENDER_EMAIL"], email, message.as_string()) 
            # terminating the session 
        s.quit()
        return {'status':1}
    except:
        #provided mail is not valid
        # terminating the session 
        s.quit()
        return {'status':-1}   


def password_reset_email(email,usertype):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls()
    # Authentication 
    s.login(params["SENDER_EMAIL"],params["SENDER_PASS"]) 
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Reset Password Recruitment Portal"
        message["From"] = params["SENDER_EMAIL"]
        message["To"] = email
        link = "http://"+params["ip"]+":8088/reset_password/"+usertype+"/"+email
        html = '''
            <html>
            <head>
                <style>
                .button {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                -webkit-transition-duration: 0.4s; /* Safari */
                transition-duration: 0.4s;
                }

                .button1 {
                box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
                }
            </style>
            </head>
            <body>
                <p>Dear '''+usertype +'''!!!<br>
                Click on below link to reset your password on Shiva Canteen</p>
                <p> <b>Click Here</b> </p>
                <a href="'''+link+'''"><button class="button button1">Reset Account Password</button></a> 
                <br>
                <p>---<br>Thanks and Regards <br>Recruitment Portal <br>IIT Jammu</p> 
            </body>
            </html>
            '''
        part = MIMEText(html, "html")
        message.attach(part)
            
        s.sendmail(params["SENDER_EMAIL"], email, message.as_string()) 
            # terminating the session 
        s.quit()
        return {'status':1}
    except:
        # provided mail is not valid
        # terminating the session 
        s.quit()
        return {'status':-1}  