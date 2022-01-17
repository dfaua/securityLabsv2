import requests
import math
import time
from uuid import uuid4

(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

lower_mask = (1 << 31) - 1
upper_mask = ~lower_mask

MT = [None] * 624
index = n + 1


# Initialize the generator from a seed
def seed_mt(seed):
    global index
    index = n
    MT[0] = int32(seed)
    for i in range(1, n):  # loop over each element
        MT[i] = int32(f * (MT[i - 1] ^ (MT[i - 1] >> (w - 2))) + i)


def state(arr):
    seed_mt(0)
    for i in range(0, n):  # loop over each element
        MT[i] = int32(untemper(arr[i]))


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index
    if index >= n:
        if index > n:
            print("Generator was never seeded")
            # Alternatively, seed with constant value; 5489 is used in reference C code[52]
        twist()

    y = temper(MT[index])

    index += 1
    return int32(y)


def temper(y):
    y ^= (y >> u)
    y ^= ((y << s) & b)
    y ^= ((y << t) & c)
    y ^= (y >> l)
    return y


def untemper(y):
    y ^= y >> l
    y ^= y << t & c
    for _ in range(7):
        y ^= y << s & b
    for _ in range(3):
        y ^= y >> u
    return y


def twist():
    global index
    for i in range(0, n):
        x = int32((MT[i] & upper_mask) + (MT[(i + 1) % n] & lower_mask))
        xA = x >> 1
        if ((x % 2) != 0): xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA
    index = 0


def int32(number):
    return int(0xFFFFFFFF & number)