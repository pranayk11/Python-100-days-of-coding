import requests
import datetime
import os

USER_NAME = "flash"
TOKEN = os.environ['TOKEN']
GRAPH_ID = "graph1"

# Create an user account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph of habit tracker
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config={
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"   # ajisai --> purple color
}

headers ={
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add pixel to habit tracker
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kms did you cycle today?: "),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Update the pixel in habit tracker
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "10"
}
# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

# Delete pixel in habit tracker
delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
