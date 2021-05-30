try:
  from MainServer.app import app
  import APIs.Database
  from APIs.main import app as app2
  import unittest
except Exception as e:
  print("Some modules are missing {}".format(e))
  
class FlaskTestCase(unittest.TestCase):
  # check for response 200
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get("/")
    statuscode = response.status_code
    self.assertEqual(statuscode,200)

  def test_role(self):
    tester = app.test_client(self)
    response = tester.get("/recruiter_login")
    statuscode = response.status_code
    self.assertEqual(statuscode,200)

  def test_rec_correct_login(self):
    tester = app.test_client(self)
    response = tester.post('/recruiter_login',data=dict(username="raghuchouhan06@gmail.com", password="abc123abc"),follow_redirects=True)
    statuscode = response.status_code
    self.assertEqual(statuscode,200)

  def test_rec_incorrect_login(self):
    tester = app.test_client(self)
    response = tester.post('/recruiter_login',data=dict(username="raghu06@gmail.com", password="ababc"),follow_redirects=True)
    statuscode = response.status_code
    self.assertEqual(statuscode,404)

    
    
if __name__=="__main__":
  unittest.main()
