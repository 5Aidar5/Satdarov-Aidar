import math 
n = int(input("Введите N чисел"))
a=[]
for i in range(n):
    x=int(input("Введите число: "))
    a.append(x)
p=1
k1=0
k2=0
for x in a:
    if x > 0 and x <= 100:
        p=p*x
        k1+=1
    if x < 0 and abs(x) > 50:
        k2+=1

if k1 > 0:
    pavarage = p**(1/k1)
    print("Сднее геометрическое: ", pavarage)
else:
    print("Подходящих положительных элементов нет")
print("Кол-во отрицательных элементов с модулем больше 50: ", k2)
