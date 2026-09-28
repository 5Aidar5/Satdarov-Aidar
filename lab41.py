import math
S=0
for n in range(1,51):
    S += (math.factorial(n) / math.factorial(2*n)) * math.cos(n+1)
print(S)