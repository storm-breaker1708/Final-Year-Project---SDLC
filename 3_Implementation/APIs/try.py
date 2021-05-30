import requests 
import json
  
# Making a PUT request 
# r = requests.post('http://192.168.43.204:8000/api/v1/credentials', params={'usertype':'candidate','email':'udaramrdc@gmail.com','password':'123456789'}) 
# print(r.json())
# check status code for response recieved 
# success code - 200 
r = requests.get('http://192.168.43.204:8000/api/v1/credentials', params={'usertype':'candidate','email':'udaramrdc@gmail.com'}) 
print(r.json())