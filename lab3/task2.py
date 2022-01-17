import json
import time
import requests
from MT_generator import seed_mt, extract_number
import random

player_ID = random.randint(23421, 1234123)

url_bet1_num1 = "http://95.217.177.249/casino/playMt?id=" + str(player_ID) + "&bet=1&number=1"
url_bet100 = "http://95.217.177.249/casino/playMt?id=" + str(player_ID) + "&bet=100&number="
url_bet500 = "http://95.217.177.249/casino/playMt?id=" + str(player_ID) + "&bet=500&number="
url_bet1000 = "http://95.217.177.249/casino/playMt?id=" + str(player_ID) + "&bet=1000&number="


epoch_time = int(time.time())
reg = requests.get("http://95.217.177.249/casino/createacc?id=" + str(player_ID))
back_text = reg.text
res = requests.get(url_bet1_num1)
res_text = res.text
print("res text: ", res_text)
json_data = json.loads(res_text)
first_real_number = json_data["realNumber"]

for i in range(-100, 100):
    seed_mt(epoch_time + i)
    number_to_bet = extract_number()

    if (first_real_number == number_to_bet):
        print("YESSSSS")
        winning_number = extract_number()
        #print ("pos 11 winning number: ", winning_number)
        res = requests.get(url_bet100 + str(winning_number))
        res_text = res.text
        winning_number = extract_number()
        res = requests.get(url_bet500 + str(winning_number))
        res_text = res.text
        winning_number = extract_number()
        res = requests.get(url_bet1000 + str(winning_number))
        res_text = res.text
        print(res_text)
        break