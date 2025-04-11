import requests
from datetime import datetime

USERNAME = "parveen7207"
TOKEN = "387tr74yfgcbi3gfcub3w"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

craete_user_endpoint = "https://pixe.la/v1/users"

data = {
    "token" : TOKEN,
    "username" :USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",
}

#response = requests.post(craete_user_endpoint, json=data)
#print(response.text)


create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_data = {
    "id" : GRAPH_ID,
    "name" :"Study Graph",
    "unit" : "Min",
    "type" : "int",
    "color" : "ajisai"
}

req_header = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(create_graph_endpoint, json=graph_data, headers=req_header)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%y%m%d"),
    "quantity" : "84",
}

#response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=req_header)
#print(response.text)

update_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": "59"
}

#response = requests.put(update_endpoint, json=update_pixel_data, headers=req_header)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


#response = requests.delete(url=delete_endpoint, headers=req_header)
#print(response.text)


