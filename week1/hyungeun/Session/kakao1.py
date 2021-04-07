import re

def step1(arr):
    return arr.lower()


def step2(arr):
    string2 = arr
    characters = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in range(len(characters)):
        string2 = string2.replace(characters[i],"")
    return string2


def step3(arr):
    string3 = arr
    for i in range(len(string3)):
        string3 = string3.replace("..", ".")
    return string3


def step4(arr):
    string4 = arr
    if string4[0] == ".":
        string4 = string4[1:]
    
    if string4:
        if string4[-1] == ".":
            string4 = string4[:-1]
        
    return string4


def step5(arr):
    string5 = arr
    if not string5:
        string5 = "a"
    
    return string5

def step6(arr):
    string6 = arr
    if len(string6) >= 16:
        string6 = string6[:15]
    
    if string6[-1] == ".":
        string6 = string6[:-1]
    return string6

def step7(arr):
    string7 = arr
    while len(string7) <= 2:
        string7 += string7[-1]
    
    return string7

def solution(new_id):
    
    answer = ''
    
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)
    answer = new_id
    return answer

    