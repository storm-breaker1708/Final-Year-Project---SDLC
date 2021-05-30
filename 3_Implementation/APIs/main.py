import flask
from flask import request, jsonify
from flask import Flask
from Database import database
from Mail import mailhandler

app = Flask(__name__)
app.secret_key = 'my-secret-key'

@app.route('/api/v1/credentials',methods=['GET','POST'])
def credentials():
    if request.method=="GET":
        parameters = request.args
        usertype = parameters.get('usertype')
        email = parameters.get('email')
        output = database.Database().getCredentials(usertype,email)
        return jsonify(output)
    elif request.method=="POST":
        parameters = request.args
        usertype = parameters.get('usertype')
        email = parameters.get('email')
        password = parameters.get('password')
        output = database.Database().putCredentials(email=email,usertype=usertype,password = password)
        return jsonify(output)


@app.route('/api/v1/userinfo',methods=['GET','POST'])
def userinfo():
    if request.method=="GET":
        parameters = request.args
        usertype = parameters.get('usertype')
        email = parameters.get('email')
        output = database.Database().getInfo(usertype,email)
        return jsonify(output)
    elif request.method=="POST":
        parameters = request.args
        usertype = parameters.get('usertype')
        if usertype=='recruiter':
            email = parameters.get('email')
            name = parameters.get('name')
            companyname = parameters.get('companyname')
            mobile = parameters.get('mobile')
            output = database.Database().putRecruiterInfo(email=email,name=name,companyname=companyname,contact_no=mobile)
            return jsonify(output)
        else:
            email = parameters.get('email')
            name = parameters.get('name')
            mobile = parameters.get('mobile')
            output = database.Database().putCandidateInfo(email=email,name=name,contact_no=mobile)
            return jsonify(output)


@app.route('/api/v1/updateprofile',methods=['POST'])
def updateprofile():
    if request.method=="POST":
        parameters = request.args
        usertype = parameters.get('usertype')
        if usertype=='recruiter':
            data = {}
            data['name'] = request.args.get("name")
            data['description'] = request.args.get("description")
            data['contact_no'] = request.args.get("contact_no")
            data['experience'] = request.args.get("experience")
            data['address'] = request.args.get("address")
            data['linkedin'] = request.args.get("linkedin")
            data['companyname'] = request.args.get("companyname")
            data['email'] = request.args.get("email")
            output = database.Database().updateRecruiterProfile(data)
            return jsonify(output)
        else:
            data = {}
            data['name'] = request.args.get("name")
            data['description'] = request.args.get("description")
            data['contact_no'] = request.args.get("contact_no")
            data['experience'] = request.args.get("experience")
            data['address'] = request.args.get("address")
            data['linkedin'] = request.args.get("linkedin")
            data['github'] = request.args.get("github")
            data['email'] = request.args.get("email")
            output = database.Database().updateCandidateProfile(data)
            return jsonify(output)
        
@app.route('/api/v1/updatephoto',methods=['POST'])
def updatephoto():
    if request.method=="POST":
        parameters = request.args
        usertype = parameters.get('usertype')
        email = parameters.get('email')
        filename = parameters.get('filename')
        output = database.Database().updatePhoto(usertype,email,filename)
        return jsonify(output)

# Account verification through email
@app.route('/api/v1/verificationmail',methods=['GET','POST'])
def accountVerification():
    if request.method=='POST':
        usertype = request.args.get('usertype')
        email = request.args.get('email')
        response  = mailhandler.verification_email(email=email,usertype=usertype)
        return jsonify(response)
    elif request.method=='GET':
        usertype = request.args.get('usertype')
        email = request.args.get('email')
        output = database.Database().verification(email=email,usertype=usertype)
        return jsonify(output)

@app.route('/api/v1/passwordreset',methods = ['GET','POST'])
def resetPassword():
    if request.method == 'GET':
        usertype = request.args.get('usertype')
        email = request.args.get('email')
        response  = mailhandler.password_reset_email(email=email,usertype=usertype)
        return jsonify(response)
    else:
        return "Request type is not correct"


@app.route('/api/v1/updatecredentials',methods=['GET','POST'])
def updatecredentials():
    if request.method == 'POST':
        parameters = request.args
        usertype = parameters.get('usertype')
        email = parameters.get('email')
        password = parameters.get('password')
        output = database.Database().updateCredentials(email=email,usertype=usertype,password=password)
        return jsonify(output)

# to get the posted jobs of the recruiter
@app.route('/api/v1/get_notappliedjobs',methods=['GET','POST'])
def get_notappliedjobs():
    if request.method == 'GET':
        parameters = request.args
        email = parameters.get('email')
        output = database.Database().get_notappliedjobs(email)
        print(output)
        return jsonify(output)

# to get the posted jobs of the recruiter
@app.route('/api/v1/get_postedjobs',methods=['GET','POST'])
def get_postedjobs():
    if request.method == 'GET':
        parameters = request.args
        email = parameters.get('email')
        output = database.Database().get_postedjobs(email)
        return jsonify(output)

@app.route('/api/v1/postjob',methods=['POST'])
def postjob():
    if request.method == 'POST':
        data = {}
        data['title'] = request.args.get('title')
        data['location'] = request.args.get('location')
        data['opening_date'] = request.args.get('opening_date')
        data['closing_date'] = request.args.get('closing_date')
        data['details'] = request.args.get('details')
        data['skills'] = request.args.get('skills')
        data['postedby'] = request.args.get('postedby')
        data['job_id'] = request.args.get('job_id')
        output = database.Database().post_job(data)
        return jsonify(output)

@app.route('/api/v1/updatejob',methods=['POST'])
def updatejob():
    if request.method == 'POST':
        data = {}
        data['title'] = request.args.get('title')
        data['location'] = request.args.get('location')
        data['opening_date'] = request.args.get('opening_date')
        data['closing_date'] = request.args.get('closing_date')
        data['details'] = request.args.get('details')
        data['skills'] = request.args.get('skills')
        data['job_id'] = request.args.get('job_id')
        output = database.Database().update_job(data)
        return jsonify(output)

@app.route('/api/v1/getjob',methods=['GET'])
def getjob():
    if request.method == 'GET':
        parameters = request.args
        job_id = parameters.get('job_id')
        output = database.Database().getjobDetails(job_id)
        return jsonify(output)

@app.route('/api/v1/closejob',methods=['POST'])
def closejob():
    if request.method == 'POST':
        parameters = request.args
        job_id = parameters.get('job_id')
        output = database.Database().close_job(job_id)
        return jsonify(output)

@app.route('/api/v1/getapplicants',methods=['GET'])
def getapplicants():
    if request.method == 'GET':
        parameters = request.args
        job_id = parameters.get('job_id')
        output = database.Database().getapplicants(job_id)
        return jsonify(output)


@app.route('/api/v1/withdraw_application',methods=['POST'])
def withdraw_application():
    if request.method == 'POST':
        parameters = request.args
        job_id = parameters.get('job_id')
        email = parameters.get('email')
        output = database.Database().withdraw_application(job_id,email)
        return jsonify(output)

@app.route('/api/v1/applyjob',methods=['POST'])
def applyjob():
    if request.method == 'POST':
        parameters = request.args
        job_id = parameters.get('job_id')
        email = parameters.get('email')
        output = database.Database().applyjob(job_id,email)
        return jsonify(output)


@app.route('/api/v1/get_appliedjobs',methods=['GET'])
def get_appliedjob():
    if request.method == 'GET':
        parameters = request.args
        email = parameters.get('email')
        output = database.Database().get_appliedjobs(email)
        print(output)
        return jsonify(output)

#to automatically detecting changes and debugging
if __name__ == "__main__":
    app.debug=True
    app.run(host="172.17.0.1",port=8000)
