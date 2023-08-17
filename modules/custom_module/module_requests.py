## Custom modules

## Apart from the modules provided as part of python installation
## python developer community makes release of custom modules
## to https://pypi.org/.

## as an example install requests from pypi
## https://pypi.org/project/requests/

## pip install requests

import requests

# print(dir(requests))
# https://dummy.restapiexample.com/

## Self- Read
## https://realpython.com/api-integration-in-python/

# get
# put
# post
# delete

response = requests.get(url="https://cat-fact.herokuapp.com/facts/")
print(response)
print(response.content)
