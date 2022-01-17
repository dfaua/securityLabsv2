import warnings
from randomgen.entropy import random_entropy
from randomgen import Generator, MT19937
import time
import json
import random
import requests
from MT_generator import seed_mt, extract_number
warnings.filterwarnings("ignore", "Generator", FutureWarning)

player_ID = random.randint(1345, 1242415)
reg = requests.get("http://95.217.177.249/casino/createacc?id="+str(player_ID))
epoch_time = int(time.time())
url_base = "http://95.217.177.249/casino/playLcg?id=" + str(player_ID) + "&bet="
url_after_bet = "&number="
first_bet = requests.get(url_base + "1" + url_after_bet + "1")
json_data = json.loads(first_bet.text)
real_number = json_data['realNumber']
print("pos 228 realNumber: ", real_number)

for i in range (-100, 100):
    seed_mt(epoch_time + i)
    number_to_bet = extract_number()
    if real_number == number_to_bet:
        print("YESS")
        win_number = extract_number()
        bet = url_base + "250" + url_after_bet + str(win_number)
        res = requests.get(bet)
       






