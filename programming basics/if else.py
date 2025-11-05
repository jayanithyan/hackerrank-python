""" Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird """


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if (n%2!=0):
    print("Weird")
elif((n%2==0)&(1<n<6)):
    print("Not Weird")
elif((n%2==0)&(5<n<21)):
    print("Weird")
else:
    if((n%2==0)&(n>20)):
        print("Not Weird")