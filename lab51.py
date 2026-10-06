n=int(input("Введите кол-во чисел: "))
a=[]
for i in range(n):
    x=int(input("Введите число: "))
    a.append(x)
k=0
for i in range(1, n-1):
    if a[i]>0 and a[i-1]<0 and a[i+1]<0:
        k+=1
    elif a[i]<0 and a[i-1]>0 and a[i+1]>0:
        k+=1
print("Кол-во троек:", k)