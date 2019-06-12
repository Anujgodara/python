#!/usr/bin/python3

import time
name=input("enter your name")
age=int(input("enter your age"))

years=95-age
print(f"your name is {name} and age {age}, you will turn 95 in year ",time.localtime().tm_year+years)
