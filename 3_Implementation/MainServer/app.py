import flask
from flask import request, jsonify,render_template,flash,redirect,session
from flask import Flask
import requests
import hashlib
import json
import datetime
import os

app = Flask(__name__)
app.secret_key = 'xjkhksaghksahgk'

@app.route('/')
def initialRoute():
    return render_template('index.html')

@app.route('/candidate_login',methods = ['GET','POST'])
def candidate_login():
    if 'user' in session and session['user']['usertype']=='candidate':
        return redirect('/candidate_dashboard')
    else:
        if request.method=='GET':
            return render_template('candidate/candidate_login.html')
        else:
            email = request.form.get('email')
            password = request.form.get('password')
            password = hashlib.sha256(password.encode()).hexdigest() 
            # check already existence of user
            params = {
                'usertype':'candidate',
                'email':email,
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/credentials', params=params)
            try:
                if response.json()['verification']==0:
                    response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'candidate','email':email})
                    flash('Account already exist but not verified! Verification link has been sent to your mail','danger')
                    return redirect('/candidate_login')
                elif password == response.json()['password']:
                    response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'candidate','email':email})
                    try:
                        if response.json()['status'] == -1:
                            return "Some internal Error Occured"
                    except:
                        session['user'] = {
                            'usertype':'candidate',
                            'email':email,
                            'name':response.json()['name'],
                        }
                        # TODO 
                        # route to candidate dashboard
                        return redirect('/candidate_dashboard')
                else:
                    flash('Login Credential are wrong!!','danger')
                    return redirect('/candidate_login')
            except:
                flash('It seems your account does not exist!!','danger')
                return redirect('/candidate_login')

@app.route('/recruiter_login',methods = ['GET','POST'])
def recruiter_login():
    if 'user' in session:
        return redirect('/recruiter_dashboard')
    else:
        if request.method=='GET':
            return render_template('recruiter/recruiter_login.html')
        else:
            email = request.form.get('email')
            password = request.form.get('password')
            password = hashlib.sha256(password.encode()).hexdigest() 
            # check already existence of user
            params = {
                'usertype':'recruiter',
                'email':email,
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/credentials', params=params)
            try:
                if response.json()['verification']==0:
                    response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'recruiter','email':email})
                    flash('Account already exist but not verified! Verification link has been sent to your mail','danger')
                    return redirect('/recruiter_login')
                elif password == response.json()['password']:
                    response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'recruiter','email':email})
                    try:
                        if response.json()['status'] == -1:
                            return "Some internal Error Occured"
                    except:
                        session['user'] = {
                            'usertype':'recruiter',
                            'email':email,
                            'name':response.json()['name'],
                        }
                        return redirect('/recruiter_dashboard')
                else:
                    flash('Login Credential are wrong!!','danger')
                    return redirect('/recruiter_login')
            except:
                flash('It seems your account does not exist!!','danger')
                return redirect('/recruiter_login')

@app.route('/candidate_signup', methods = ['GET','POST'])
def candidate_signup():
    if request.method == 'GET':
        return render_template('candidate/candidate_signup.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')
        if password != conf_password:
            flash("Passwords are not matching!!","danger")
            return redirect('/candidate_signup')
        elif len(mobile) != 10:
            flash("Enter Valid mobile number!!","danger")
            return redirect('/candidate_signup')
        else:
            # check already existence of user
            params = {
                'usertype':'candidate',
                'email':email,
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/credentials', params=params)
            try:
                if response.json()['verification']==0:
                    response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'candidate','email':email})
                    flash('Account already exist but not verified! Verification link has been sent to your mail','danger')
                    return redirect('/candidate_login')
                else:
                    flash('Account already exist!! Login with your credentials','danger')
                    return redirect('/candidate_login')
            except:
                pass


            '''
                Add credentials to database
            '''
            params = {
                'usertype':'candidate',
                'email':email,
                'password':hashlib.sha256(password.encode()).hexdigest() 
            }
            response = requests.post('http://172.17.0.1:8000/api/v1/credentials', params=params)

            '''
                Add details of user to database
            '''
            params = {
                'usertype':'candidate',
                'email':email,
                'name':name,
                'mobile':mobile,
            }
            response = requests.post('http://172.17.0.1:8000/api/v1/userinfo', params=params)
            if response.json()['status'] == -1:
                return "Some internal Error Occured"
            else:
                response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'candidate','email':email})
                flash("Verification link has been sent to you email!!","success")
                return redirect('/candidate_login')

@app.route('/recruiter_signup', methods = ['GET','POST'])
def recruiter_signup():
    if request.method == 'GET':
        return render_template('recruiter/recruiter_signup.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        companyname = request.form.get('companyname')
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')
        if password != conf_password:
            flash("Passwords are not matching!!","danger")
            return redirect('/recruiter_signup')
        elif len(mobile) !=10:
            flash("Enter Valid mobile number!!","danger")
            return redirect('/recruiter_signup')
        else:
            # check already existence of user
            params = {
                'usertype':'recruiter',
                'email':email,
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/credentials', params=params)
            try:
                if response.json()['verification']==0:
                    response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'recruiter','email':email})
                    flash('Account already exist but not verified! Verification link has been sent to your mail','danger')
                    return redirect('/recruiter_login')
                else:
                    flash('Account already exist!! Login with your credentials','danger')
                    return redirect('/recruiter_login')
            except:
                pass

            '''
                Add credentials to database
            '''
            params = {
                'usertype':'recruiter',
                'email':email,
                'password':hashlib.sha256(password.encode()).hexdigest() 
            }
            response = requests.post('http://172.17.0.1:8000/api/v1/credentials', params=params)

            '''
                Add details of user to database
            '''
            params = {
                'usertype':'recruiter',
                'email':email,
                'name':name,
                'companyname':companyname,
                'mobile':mobile,
            }
            response = requests.post('http://172.17.0.1:8000/api/v1/userinfo', params=params)
            if response.json()['status'] == -1:
                return "Some internal Error Occured"
            else:
                response = requests.post('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':'recruiter','email':email})
                flash("Verification link has been sent to you email!!","success")
                return redirect('/recruiter_login')
@app.route("/accountverification")
def accountverification():
    usertype = request.args.get('usertype')
    email = request.args.get('email')
    response = requests.get('http://172.17.0.1:8000/api/v1/verificationmail', params={'usertype':usertype,'email':email})
    if response.json()['status'] ==-1:
        return "Some internel Error occured"
    else:
        return "Your Account verified Successfully"

@app.route("/forget_password/<usertype>",methods = ['GET','POST'])
def forget_password(usertype):
    if request.method == 'GET':
        return render_template('forget_password.html',usertype=usertype)
    elif request.method=='POST':
        email = request.form.get('email')
        response = requests.get('http://172.17.0.1:8000/api/v1/credentials', params={'usertype':usertype,'email':email})
        print(response.json())
        try:
            if response.json()['status']==-1:
                flash('Email is not registered with portal!','danger')
                return redirect(f'/forget_password/{usertype}')
        except:
            response = requests.get('http://172.17.0.1:8000/api/v1/passwordreset',params={'usertype':usertype,'email':email})
            if response.json()['status'] == -1:
                return "Internal Error Occured"
            else:
                flash('Password Reset Mail sent successfully','success')
                return redirect(f'/{usertype}_login')
    else:
        return "Some internal error occured"

@app.route("/reset_password/<usertype>/<email>",methods=['GET','POST'])
def reset_password(usertype,email):
    if request.method=='GET':
        return render_template('reset_password.html',email=email,usertype=usertype) 
    else:
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')
        if password != conf_password:
            flash("Passwords are not matching!!","danger")
            return redirect(f'/reset_password/{usertype}/{email}')
        else:
            params = {
                'usertype':usertype,
                'email':email,
                'password':hashlib.sha256(password.encode()).hexdigest() 
            }
            response = requests.post('http://172.17.0.1:8000/api/v1/updatecredentials', params=params)
            if response.json()['status']==-1:
                return "Internal Error Occured"
            else:
                flash("Password changed successfully!!","success")
                return redirect(f"/{usertype}_login")

# recruiter Dashboard
@app.route('/recruiter_dashboard', methods = ['GET','POST'])
def recruiter_dashboard():
    if 'user' in session and session['user']['usertype']=='recruiter':
        if request.method=='GET':
            params = {
                'email':session['user']['email'],
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/get_postedjobs', params=params)
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('recruiter/recruiter_dashboard.html',name=session['user']['name'],jobs=response.json(),jobcounts=len(response.json())) 

        else:
            return "Invalid request"
    else:
        return redirect("/")


# add job
@app.route('/addjob',methods= ['GET','POST'])
def addjob():
    if 'user' in session and session['user']['usertype']=='recruiter':
        if request.method=='GET':
                return render_template('recruiter/addjob.html',name=session['user']['name'])
        else:
            # add request
            data = {}
            data['title'] = request.form.get('title')
            data['location'] = request.form.get('location')
            data['opening_date'] = request.form.get('opening_date')
            data['closing_date'] = request.form.get('closing_date')
            data['details'] = request.form.get('details')
            data['skills'] = request.form.get('skills')
            data['postedby'] = session['user']['email']
            data['job_id'] = session['user']['email'].split('@')[0]+str(datetime.datetime.now())

            response = requests.post('http://172.17.0.1:8000/api/v1/postjob', params=data)
            if response.json()['status']==-1:
                return "Some internal error occured"
            else:
                return redirect('/recruiter_dashboard')
    else:
        return redirect("/")

@app.route('/viewjob',methods=['GET'])
def viewjob():
    if 'user' in session:
        if session['user']['usertype']=='candidate':
            job_id = request.args.get('job_id')
            response = requests.get('http://172.17.0.1:8000/api/v1/getjob', params={'job_id':job_id})
            try:
                if response.json()['status']==-1:
                    return "Some internal Error Occured"
            except:
                redirect = request.args.get('redirect')
                return render_template('candidate/viewjob.html',job=response.json(),redirect=int(redirect))
        else:
            job_id = request.args.get('job_id')
            response = requests.get('http://172.17.0.1:8000/api/v1/getjob', params={'job_id':job_id})
            try:
                if response.json()['status']==-1:
                    return "Some internal Error Occured"
            except:
                return render_template('recruiter/viewjob.html',job=response.json())
    else:
        redirect("/")

# add job
@app.route('/editjob',methods= ['GET','POST'])
def editjob():
    if 'user' in session and session['user']['usertype']=='recruiter':
        job_id = request.args.get('job_id')
        if request.method=='GET':
            response = requests.get('http://172.17.0.1:8000/api/v1/getjob', params={'job_id':job_id})
            try:
                if response.json()['status']==-1:
                    return "Some internal Error Occured"
            except:
                print(response.json()['details'])
                return render_template('recruiter/editjob.html',name=session['user']['name'],job = response.json())

        else:
            # add request
            data = {}
            data['title'] = request.form.get('title')
            data['location'] = request.form.get('location')
            data['opening_date'] = request.form.get('opening_date')
            data['closing_date'] = request.form.get('closing_date')
            data['details'] = request.form.get('details')
            data['skills'] = request.form.get('skills')
            data['job_id'] = job_id
            response = requests.post('http://172.17.0.1:8000/api/v1/updatejob', params=data)
            if response.json()['status'] == -1:
                return "Some internal error occured"
            else:
                return redirect('/recruiter_dashboard')
    else:
            return redirect("/")

@app.route('/userprofile',methods= ['GET','POST'])
def userprofile():
    email = request.args.get("email")
    if 'user' in session and email==None:
        if session['user']['usertype']=='candidate':
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'candidate','email':session['user']['email']})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('candidate/candidate_profile.html',profile = response.json())
        else:
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'recruiter','email':session['user']['email']})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('recruiter/recruiter_profile.html',profile = response.json())
    elif 'user' in session and email != None:
        if session['user']['usertype']=='recruiter':
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'candidate','email':email})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('recruiter/view_candidate_profile.html',profile = response.json())
        else:
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'recruiter','email':email})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('candidate/view_recruiter_profile.html',profile = response.json())
    else:
        return redirect("/")

@app.route('/editprofile',methods= ['GET','POST'])
def editprofile():
    if 'user' in session and session['user']['usertype']=='recruiter':
        if request.method=='GET':
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'recruiter','email':session['user']['email']})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('recruiter/edit_recruiter_profile.html',profile=response.json())
        else:
            data = {}
            data['name'] = request.form.get("name")
            data['description'] = request.form.get("description")
            data['contact_no'] = request.form.get("contact_no")
            data['experience'] = request.form.get("experience")
            data['address'] = request.form.get("address")
            data['linkedin'] = request.form.get("linkedin")
            data['companyname'] = request.form.get("companyname")
            data['email'] = session['user']['email']
            data['usertype'] = session['user']['usertype']
            response = requests.post('http://172.17.0.1:8000/api/v1/updateprofile', params=data)
            if response.json()['status']==-1:
                return "Some internal error occured"
            else:
                return redirect("/userprofile")
    elif 'user' in session and session['user']['usertype']=='candidate':
        if request.method=='GET':
            response = requests.get('http://172.17.0.1:8000/api/v1/userinfo', params={'usertype':'candidate','email':session['user']['email']})
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('candidate/edit_candidate_profile.html',profile=response.json())
        else:
            data = {}
            data['name'] = request.form.get("name")
            data['description'] = request.form.get("description")
            data['contact_no'] = request.form.get("contact_no")
            data['experience'] = request.form.get("experience")
            data['address'] = request.form.get("address")
            data['linkedin'] = request.form.get("linkedin")
            data['github'] = request.form.get("github")
            data['email'] = session['user']['email']
            data['usertype'] = session['user']['usertype']
            response = requests.post('http://172.17.0.1:8000/api/v1/updateprofile', params=data)
            if response.json()['status']==-1:
                return "Some internal error occured"
            else:
                return redirect("/userprofile")

@app.route("/changephoto",methods= ['GET','POST'])
def changephoto():
    if 'user' in session:
        if request.method=="GET":
            return render_template("uploadphoto.html")
        else:

            file = request.files['img']
            filename=str(hashlib.sha256((session['user']['email']+str(datetime.datetime.now())).encode()).hexdigest()) +".jpg"
            file.save(os.path.join("./static/profile_images", filename))
            response = requests.post('http://172.17.0.1:8000/api/v1/updatephoto', params={'usertype':session['user']['usertype'],'email':session['user']['email'],'filename':filename})
            if response.json()['status']==-1:
                return "Some internal error occured"
            else:
                return redirect("/userprofile")
    else:
        return redirect("/")

# Candidate Dashboard
@app.route('/candidate_dashboard', methods = ['GET','POST'])
def candidate_dashboard():
    if 'user' in session and session['user']['usertype']=='candidate':
        if request.method=='GET':
            params = {
                'email':session['user']['email']
            }
            response = requests.get('http://172.17.0.1:8000/api/v1/get_notappliedjobs', params=params)
            try:
                if response.json()['status']==-1:
                    return "Some internal error occured"
            except:
                return render_template('candidate/candidate_dashboard.html',name=session['user']['name'],jobs=response.json(),jobcounts=len(response.json())) 

        else:
            return "Invalid request"
    else:
        return redirect("/")

@app.route("/withdraw_application",methods = ['GET','POST'])
def withdraw_application():
    if 'user' in session and session['user']['usertype']=="candidate":
        job_id=request.args.get("job_id")
        response = requests.post('http://172.17.0.1:8000/api/v1/withdraw_application', params={'email':session['user']['email'],'job_id':job_id})
        if response.json()['status']==-1:
            return "Some internal error occured"
        else:
            return redirect('/appliedjobs')
    else:
        return redirect("/")

@app.route("/applyjob",methods = ['GET','POST'])
def applyjob():
    if 'user' in session and session['user']['usertype']=="candidate":
        job_id=request.args.get("job_id")
        response = requests.post('http://172.17.0.1:8000/api/v1/applyjob', params={'email':session['user']['email'],'job_id':job_id})
        if response.json()['status']==-1:
            return "Some internal error occured"
        else:
            return redirect('/appliedjobs')
    else:
        return redirect("/")

@app.route("/appliedjobs",methods = ['GET'])
def appliedjobs():
    if 'user' in session and session['user']['usertype']=="candidate":
        response = requests.get('http://172.17.0.1:8000/api/v1/get_appliedjobs', params={'email':session['user']['email']})
        try:
            if response.json()['status']==-1:
                return "Some internal error occured"
        except:
            print(response.json())
            return render_template("candidate/applied_jobs.html",jobs=response.json(),jobcounts=len(response.json()))
    else:
        return redirect("/")

@app.route("/closejob",methods = ['GET','POST'])
def closejob():
    if 'user' in session and session['user']['usertype']=="recruiter":
        job_id=request.args.get("job_id")
        response = requests.post('http://172.17.0.1:8000/api/v1/closejob', params={'job_id':job_id})
        if response.json()['status']==-1:
            return "Some internal error occured"
        else:
            return redirect('/recruiter_dashboard')
    else:
        return redirect("/")

@app.route("/applicants")
def get_applicants():
    if 'user' in session and session['user']['usertype']=="recruiter":
        job_id=request.args.get("job_id")
        response1 = requests.get('http://172.17.0.1:8000/api/v1/getapplicants', params={'job_id':job_id})
        response2 = requests.get('http://172.17.0.1:8000/api/v1/getjob', params={'job_id':job_id})
        try:
            if response1.json()['status']==-1 or response2.json()['status']==-1:
                return "Some internal error occured"
        except:

            return render_template("/recruiter/applicants.html",applicants=enumerate(response1.json()),applicantcounts=len(response1.json()),job=response2.json())
    else:
        return redirect("/")

# logout route for all type of users
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect("/")

#to automatically detecting changes and debugging
if __name__ == "__main__":
    app.debug=True
    app.run(host="172.17.0.1",port=8088)




