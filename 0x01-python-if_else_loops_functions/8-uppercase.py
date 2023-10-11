#!/usr/bin/python3
islower = __import__('7-islower').islower

def uppercase(str):
    for char in str:
        print("{}".format(char if not islower(char) else chr(ord(char)-32)), end="")
    print(end="\n")
