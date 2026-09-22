import math
a=-0.9
b=-0.1
h=0.05
print("x|y")
for i in range(int((b-a)/h)+1):
    x=round(a + i*h, 2)
    
    y = (math.exp(-x) * (x**3 + math.sqrt(x+2)))/(2**x - math.sqrt(abs(math.exp(x)/2-2*math.log(abs(x)))))
    print("x=",x,"y=",y)