from urllib.request import urlopen
from itertools import permutations,combinations

ur = "https://geocoder.api.here.com/6.2/geocode.json?searchtext="
appid = "&app_id=UMuyYf4xchX1ZRWbGK4O&app_code=uAVLHGYMOx3wvnt16o_NDw"

def search(search_keyword):
    res = urlopen(url= ur+search_keyword+appid)

from math import ceil

def print_seq(n):
    prv = 1
    next = 1
    temp = 0
    i = 2
    print(prv,)
    print(next)
    while i < n:
        if i == n:
            break
        print(prv+next)
        i +=1
        if i == n:
            break
        i +=1
        print((prv+next)//next)
        temp = prv+next
        prv = temp
        next = temp//next


def print_seq(n):
    prv = 1
    nex = 1
    temp = 0
    i = 2
    print(prv,end=" ")
    print(nex,end=" ")
    while i < n:
        if i == n:
            break
        print(prv+nex,end=" ")
        i +=1
        if i == n:
            break
        i +=1
        print((prv+nex)//nex,end=" ")
        temp = prv+nex
        prv = temp
        nex = temp//nex


def print_seq(n):
    prv = 1
    nex = 1
    temp = 0
    i = 2
    print(prv,end=" ")
    print(nex,end=" ")
    while i < n:
        if i == n:
            break
        print(prv+nex,end=" ")
        i +=1
        if i == n:
            break
        i +=1
        print((prv+nex)//nex,end=" ")
        temp = prv+nex
        prv = temp
        nex = temp//nex

def en(letter):
    return chr(ord(letter) + 2)

def dec(letter):
    return chr(ord(letter) - 2)

a = 3

com_index = list(permutations([i for i in range(a)], 3))
print(com_index)

def good_ti():
    count = 0
