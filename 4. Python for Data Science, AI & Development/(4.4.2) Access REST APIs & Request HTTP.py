 ### Requests in Python

# Requests is a Python Library that allows you to send HTTP/1.1 requests easily. We can import the library as follows:
import requests
# We will also use the following libraries:
import os 
from PIL import Image
from IPython.display import IFrame
# You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)
# We have the response object r, this has information about the request, like the status of the request. We can view the status code using the attribute status_code.
r.status_code
# You can view the request headers:
print(r.request.headers)
# You can view the request body, in the following line, as there is no body for a get request we get a None:
print("request body:", r.request.body)
# You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)
# We can obtain the date the request was sent using the key Date.
header['date']
# Content-Type indicates the type of data:
header['Content-Type']
# You can also check the encoding:
r.encoding
# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]
# You can load other types of data for non-text requests, like images. Consider the URL of the following image:
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# We can make a get request:
r=requests.get(url)
# We can look at the response header:
print(r.headers)
# We can see the 'Content-Type'
r.headers['Content-Type']
# An image is a response object that contains the image as a bytes-like object. 
# As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
path
# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
    f.write(r.content)
# We can view the image:
Image.open(path)

##### Question 1: write wget
# In the previous section, we used the wget function to retrieve content from the web server as shown below. 
# Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'Example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
#####

### Get Requests with URL Parameters

# The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service. The URL in Python is given by:
url_get='http://httpbin.org/get'
# To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
payload={"name":"Joseph","ID":"123"}
# Then passing the dictionary payload to the params parameter of the get() function:
r=requests.get(url_get,params=payload)
# We can print out the URL and see the name and values.
r.url
# There is no request body.
print("request body:", r.request.body)
# We can print out the status code.
print(r.status_code)
# We can view the response as text:
print(r.text)
# We can look at the 'Content-Type'
r.headers['Content-Type']
# As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
r.json()
# The key args has the name and values:
r.json()['args']

### Post Requests

# Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. 
# In order to send the Post Request in Python, in the URL we change the route to POST:
url_post='http://httpbin.org/post'
# This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.

# To make a POST request we use the post() function, the variable payload is passed to the parameter data :
r_post=requests.post(url_post,data=payload)
# Comparing the URL from the response object of the GET and POST request we see the POST request has no name or value pairs.
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
# We can compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
# We can view the form as well:
r_post.json()['form']