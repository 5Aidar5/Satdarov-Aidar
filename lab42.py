import math
P=1
for n in range(1,21):
    P*= (4.4**(3*n+1)/math.factorial(2*n)) * math.log(n + 1)
print(P)