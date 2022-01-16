import json
import math
import requests

player_ID = "23456"
url_base = "http://95.217.177.249/casino/playLcg?id=" + player_ID + "&bet="
url_after_bet = "&number="
m = 4294967296

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def first_3_numbers():
    list_random_bet_three_times = []
    for i in range (3):
        bet = "1"
        number_to_bet = "10000"
        url_to_send = url_base + bet + url_after_bet + number_to_bet
        #print(url_to_send)
        res = requests.get(url_to_send)
        res_text = res.text
        #print(res.text)
        json_data = json.loads(res_text)
        #print("realNumber: ", json_data["realNumber"])
        int_number = json_data["realNumber"]
        print("type: ", type(int_number), " value: ", int_number)

        list_random_bet_three_times.append(int_number)
    return list_random_bet_three_times

def searching_a (list_of_3):
    print("searching a")
    s0 = int(list_of_3[0])
    print("type: ", type(s0), " value: ", s0)
    s1 = int(list_of_3[1])
    print("type: ", type(s1), " value: ", s1)
    s2 = int(list_of_3[2])
    print("type: ", type(s2), " value: ", s2)
    a = (s2 - s1)*modinv(s1 - s0, m) % m
    return a

def searching_c (list_a_s0_s1):
    s1 = int(list_a_s0_s1[2])
    s0 = int(list_a_s0_s1[1])
    a = int(list_a_s0_s1[0])
    c = (s1 - s0 * a) % m
    return c

def playing_hard_game (a, c, list_of_3):
    last = list_of_3[2]
    last_int = int(last)
    number_to_bet = (last_int*a + c) % m
    number_to_bet_str = str(number_to_bet)
    bet = "150"
    url_to_send = url_base + bet + url_after_bet + number_to_bet_str
    res = requests.get(url_to_send)
    print(res.text)

#first_3_numbers()
list_of_first_3 = first_3_numbers()
a = searching_a(list_of_first_3)
print("a: ", a)
#c = searching_c(a)
#print("3 first: ", list_of_first_3, " a: ", a, " c: ", c)
#playing_hard_game(a, c, list_of_first_3)

