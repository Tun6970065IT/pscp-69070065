"""inflation"""
import math
n = float(input())
k = int(input())

total = n * (1+3.81/100)**k
print(math.floor(total * 100)/100)
