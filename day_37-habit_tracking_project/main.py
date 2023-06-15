import requests
from datetime import datetime


USERNAME = "azetxxx"
TOKEN = ""
GRAPH_ID = "graph-python"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"


# ⚠️ STEP 1: Creating a new user

### CREATING A NEW USER ###
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
### END CREATING A NEW USER ###


# ⚠️ STEP 2: Creating a new graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph-python",
    "name": "Python Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu" # see colors below
}

### SUPPORTED COLORS ###
# shibafu (green),
# momiji (red),
# sora (blue),
# ichou (yellow),
# ajisai (purple)
# kuro (black)
### END SUPPORTED COLORS ###


### CREATING A NEW GRAPH ###
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
### END CREATING A NEW GRAPH ###


# ⚠️ STEP 3: Browse Graph, using the url:

# https://pixe.la/v1/users/azetxxx/graphs/graph-running.html


# ⚠️ STEP 4: Post a pixel

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

post_params = {
    "date": today,
    "quantity": "2"
}

# response = requests.post(url=post_endpoint, json=post_params, headers=headers)
# print(response.text)


# ⚠️ STEP 5: Edit pixel by PUT request
update_pixel_date = "20230615"
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_pixel_date}"

update_pixel_params = {
    "quantity": "1"
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(update_pixel_response.text)


# ⚠️ STEP 6: Delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response.text)
