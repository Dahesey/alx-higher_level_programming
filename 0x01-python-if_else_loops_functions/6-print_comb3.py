#!/usr/bin/python3
for a in range(9):
    for b in range(a + 1, 10):
        print("{}{}".format(a, b), end="\n" if a == 8 else ", ")
