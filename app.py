
#!/bin/python3

import math
import os
import random
import re
import sys

# Task
# Given an integer,
# , perform the following conditional actions:
#     If 
# is odd, print Weird
# If
# is even and in the inclusive range of to
# , print Not Weird
# If
# is even and in the inclusive range of to
# , print Weird
# If
# is even and greater than
#     , print Not Weird
# Input Format
# A single line containing a positive integer,
# .
# Constraints
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 == 1:
#         print('Weird')
#     elif n % 2 == 0 and n in range(2, 6):
#         print('Not Weird')
#     elif n % 2 == 0 and n in range(6, 21):
#         print('Weird')    
#     elif n % 2 == 0 and n > 20:
#         print('Not Weird')    


# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print . 

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)