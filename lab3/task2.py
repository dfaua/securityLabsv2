import warnings
from randomgen.entropy import random_entropy
from randomgen import Generator, MT19937
import time
import json
import math
import requests
from MT_generator import mt_seed, extract_number
warnings.filterwarnings("ignore", "Generator", FutureWarning)


player_ID = "35742"
url_base = "http://95.217.177.249/casino/playMt?id=" + player_ID + "&bet="
url_after_bet = "&number="


def send_request(number_to_bet, delay):
    bet = "1"
    number_to_bet = str(number_to_bet)
    url_to_send = url_base + bet + url_after_bet + number_to_bet
    #print(url_to_send)
    res = requests.get(url_to_send)
    #print(res)
    #print("time delay: ", delay, "\nnumber_to_bet: ", number_to_bet, "\n", res.text)
    print(res.text)

def try_to_find_the_correct_delay():
    epoch_time = int(time.time())
    #print("original epoch time: ", epoch_time)
    for i in range(-2, 2):
        epoch_time += i
        #print("modified epoch time: ", epoch_time)
        mt_seed(epoch_time)
        number_to_bet = extract_number()
        print("number to bet: ", number_to_bet)
        send_request(number_to_bet, i)

try_to_find_the_correct_delay()




