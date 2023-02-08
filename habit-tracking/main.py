import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jr309rj0",
    "username": "kentonhuang",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

USERNAME = "kentonhuang"
token = "jr309rj0"

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": token
}

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "mile",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

todays_date = datetime.now()

graph_post_config = {
    "date": todays_date.strftime("%Y%m%d"),
    "quantity": input("How many miles did you cycle today?"),
}

response = requests.post(url=graph_endpoint, json=graph_post_config, headers=headers)
print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230208"

graph_update_config = {
    "quantity": "6.75",
}

# response = requests.put(url=graph_update_endpoint, headers=headers, json=graph_update_config)
# print(response.text)
#
# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230208"
# response = requests.delete(url=graph_update_endpoint, headers=headers)