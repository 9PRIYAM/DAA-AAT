#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRI
def stringConstruction(s):
    return len(set(s))

# Reading input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Processing each string
for s in strings:
    print(stringConstruction(s))
