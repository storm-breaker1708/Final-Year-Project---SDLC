import MySQLdb

class Database:
    # Constructor for database cursor
    def __init__(self):
        self.db = MySQLdb.connect("localhost",
        "btpdatabase",
        "Abc@12345",
        "recruitment")
        self.cursor = self.db.cursor()
    
    def getCredentials(self,usertype,email):
        try:
            if usertype == 'candidate':
                query  = f"SELECT * FROM CandidateCredentials where email = '{email}'"
                self.cursor.execute(query)
                results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
                return results[0]
            elif usertype == 'recruiter':
                # getting credentials of recruiter
                query  = f"SELECT * FROM RecruiterCredentials where email = '{email}'"
                self.cursor.execute(query)
                results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
                return results[0]
        except:
            # for invalid request
            return {'status':-1}
    
    def putCredentials(self,email,usertype,password):
        try:
            if usertype == 'candidate':
                query = f"INSERT INTO CandidateCredentials(email,password) VALUES('{email}','{password}')"
                self.cursor.execute(query)
                self.db.commit()
            elif usertype == 'recruiter':
                query = f"INSERT INTO RecruiterCredentials(email,password) VALUES('{email}','{password}')"
                self.cursor.execute(query)
                self.db.commit()
            else:
                print('else')
                return {'status':-1}
            return {'status':1}
        except:
            print('except')
            return {'status':-1}
    
    def getInfo(self,usertype,email):
        try:
            if usertype == 'candidate':
                query  = f"SELECT * FROM Candidate where email = '{email}'"
                self.cursor.execute(query)
                results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
                return results[0]
            elif usertype == 'recruiter':
                # getting credentials of recruiter
                query  = f"SELECT * FROM Recruiter where email = '{email}'"
                self.cursor.execute(query)
                results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
                return results[0]
            else:
                # for invalid request
                return {'status':-1}
        except:
            return {'status':-1}
    def putCandidateInfo(self,email,name,contact_no):
        try:
            query = f"INSERT INTO Candidate(email,name,contact_no) VALUES('{email}','{name}','{contact_no}')"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    def putRecruiterInfo(self,email,name,companyname,contact_no):
        try:
            query = f"INSERT INTO Recruiter(email,name,company,contact_no) VALUES('{email}','{name}','{companyname}','{contact_no}')"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}
    
    def updateRecruiterProfile(self,data):
        try:
            query = f"UPDATE Recruiter SET name='{data['name']}',company='{data['companyname']}',contact_no='{data['contact_no']}',experience='{data['experience']}',address='{data['address']}',description = '{data['description']}',linkedin='{data['linkedin']}' WHERE email = '{data['email']}' "
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # TODO
    def updateCandidateProfile(self,data):
        try:
            query = f"UPDATE Candidate SET name='{data['name']}',github='{data['github']}',contact_no='{data['contact_no']}',experience='{data['experience']}',address='{data['address']}',description = '{data['description']}',linkedin='{data['linkedin']}' WHERE email = '{data['email']}' "
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    #update the photo of user
    def updatePhoto(self,usertype,email,filename):
        try:
            if usertype=='recruiter':
                query = f"UPDATE Recruiter SET photo='{filename}' WHERE email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            elif usertype=='candidate':
                query = f"UPDATE Candidate SET photo='{filename}' WHERE email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            else:
                return {'status' :-1}
            return {'status' :1}
        except:
            return {'status' :-1}

    # for the account verification of the user
    def verification(self,email,usertype):
        try:
            if usertype=='recruiter':
                query = f"UPDATE RecruiterCredentials SET verification = 1 where email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            elif usertype=='candidate':
                query = f"UPDATE CandidateCredentials SET verification = 1 where email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            else:
                return {'status' :-1}
            return {'status' :1}
        except:
            return {'status' :-1}

    def updateCredentials(self,email,usertype,password):
        try:
            if usertype=='recruiter':
                query = f"UPDATE RecruiterCredentials SET password = '{password}' where email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            elif usertype=='candidate':
                query = f"UPDATE CandidateCredentials SET password = '{password}' where email = '{email}'"
                self.cursor.execute(query)
                self.db.commit()
            else:
                return {'status' :-1}
            return {'status' :1}
        except:
            return {'status' :-1}

    def get_notappliedjobs(self,email):
        try:
            query = f"SELECT *FROM PostedJobs as R NATURAL JOIN (SELECT name,job_id,postedby,jobstatus FROM JobDetails,Recruiter WHERE postedby=email and jobstatus=1 AND job_id NOT IN (SELECT job_id FROM AppliedJobs WHERE applicant='{email}')) as S"
            self.cursor.execute(query)
            results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
            return results
        except:
            return {'status':-1}

    # get posted jobs of particular recruiter
    def get_postedjobs(self,email):
        try:
            query = f"SELECT *FROM PostedJobs as R NATURAL JOIN (SELECT name,job_id,postedby,jobstatus,applicantscount FROM JobDetails,Recruiter WHERE postedby='{email}' AND email='{email}') as S"
            self.cursor.execute(query)
            results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
            return results
        except:
            return {'status':-1}

    # post job
    def post_job(self,data):
        try:
            query1 = f"INSERT INTO JobDetails (job_id,jobstatus,postedby) VALUES ('{data['job_id']}',1,'{data['postedby']}')"
            self.cursor.execute(query1)
            query2 = f"INSERT INTO PostedJobs (job_id,title,location,open_date,close_date,details,skills) VALUES ('{data['job_id']}','{data['title']}','{data['location']}','{data['opening_date']}','{data['closing_date']}','{data['details']}','{data['skills']}')"
            self.cursor.execute(query2)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # update job
    def update_job(self,data):
        try:
            query = f"UPDATE PostedJobs SET title='{data['title']}',location='{data['location']}',open_date='{data['opening_date']}',close_date='{data['closing_date']}',details='{data['details']}',skills='{data['skills']}' WHERE job_id='{data['job_id']}'"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # close job
    def close_job(self,job_id):
        try:
            query = f"UPDATE JobDetails SET jobstatus=0 WHERE job_id='{job_id}'"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # get the details of a job
    def getjobDetails(self,job_id):
        try:
            query = f"SELECT *FROM PostedJobs as R NATURAL JOIN (SELECT name,job_id,postedby,jobstatus FROM JobDetails,Recruiter WHERE postedby=email AND job_id='{job_id}') as S"
            self.cursor.execute(query)
            results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
            return results[0]
        except:
            return {'status':-1}
        
    # getapplicants
    def getapplicants(self,job_id):
        try:
            query = f"SELECT name,email FROM AppliedJobs,Candidate WHERE job_id='{job_id}' AND applicant=email"
            self.cursor.execute(query)
            results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
            return results
        except:
            return {'status':-1}

    # withdraw_application
    def withdraw_application(self,job_id,email):
        try:
            query =f"DELETE FROM AppliedJobs WHERE job_id='{job_id}' AND applicant='{email}'"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # apply job
    def applyjob(self,job_id,email):
        try:
            query =f"INSERT INTO AppliedJobs VALUES('{job_id}','{email}')"
            self.cursor.execute(query)
            self.db.commit()
            return {'status':1}
        except:
            return {'status':-1}

    # apply job
    def get_appliedjobs(self,email):
        try:
            query =f"SELECT *FROM PostedJobs NATURAL JOIN (SELECT name,job_id,postedby FROM JobDetails, Recruiter WHERE postedby=email and job_id IN (SELECT job_id FROM AppliedJobs WHERE applicant='{email}')) as S"
            self.cursor.execute(query)
            results =  self.data_description(self.cursor.fetchall(),self.cursor.description)
            return results
        except:
            return {'status':-1}

    # create json form of every query data
    def data_description(self,result,des):
        field_name = [field[0] for field in des]
        data = []
        for d in result:
            temp = {}
            for i in range(len(d)):
                temp[field_name[i]]=d[i] 
            data.append(temp)
        return data
