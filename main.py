print("введите разные числа")
a=int(input("Введите число a:"))
b=int(input("Введите число b:"))
c=int(input("Введите число c:"))

if (a%2==0):
    print("Число", a, "четное")
else: print("Число", a, "нечетное")

if (a%7==0):
    print("Число", a, "кратно 7")
else: print("Число", a, "не кратно 7")

if (a>b) and (a>c): print("Число", a, "наибольшее")
elif (b>c) and (b>a): print("Число", b, "наибольшее")
elif (c>a) and (c>b): print("Число", c, "наибольшее")