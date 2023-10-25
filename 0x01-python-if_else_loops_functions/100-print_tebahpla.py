#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    print("{:c}".format(alphabet if alphabet % 2 == 0
          else alphabet - 32), end="")
