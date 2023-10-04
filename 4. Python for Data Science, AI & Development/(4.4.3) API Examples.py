#!pip install randomuser
# Then, we will load the necessary libraries.
from randomuser import RandomUser
import pandas as pd
# First, we will create a random user object, r.
r = RandomUser()
# Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
some_list
# The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. 
# For example, to get full name, we call get_full_name() function.
name = r.get_full_name()
name
# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

#### Example 1: Generate photos of the random 10 users.
for user in some_list:
    print(user.get_picture())
####

# To generate a table with information about the users, we can write a function containing all desirable parameters. 
# For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. 
# We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
def get_users():
    users =[]
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)
get_users()
df1 = pd.DataFrame(get_users())
df1
# Now we have a pandas dataframe that can be used for any testing purposes that the tester might have.

##### Example 2: Fruitvice API
# Another, more common way to use APIs, is through requests library. The next lab, Requests and HTTP, will contain more information about requests.
# We will start by importing all required libraries.
import requests
import json
# We will obtain the fruitvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://fruityvice.com/api/fruit/all")
# We will retrieve results using json.loads() function.
results = json.loads(data.text)
# We will convert our json data into pandas data frame.
pd.DataFrame(results)
# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2
# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

##### Exercise 2: Find out how many calories are contained in a banana.

banana = df2.loc[df2["name"] == 'Banana']
banana.iloc[0]['nutritions.calories']

#####

##### Exercise 3: Using requests.get("url") function, load your data.

data2 = requests.get("https://cat-fact.herokuapp.com/facts")

# 2. Retrieve results using json.loads() function.
results=json.loads(data2.text)

# 3. Convert json data into pandas data frame.
df3 = pd.DataFrame(results)
df3
#####