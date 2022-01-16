import requests
player_ID = "35742"
url_to_send = "http://95.217.177.249/casino/createacc?id=" + player_ID
print(url_to_send)
res = requests.get(url_to_send)
print(res)
print(res.text)