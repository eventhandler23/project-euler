#!/usr/bin/python

max = 1000
total = 0

for i in range(max):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print total