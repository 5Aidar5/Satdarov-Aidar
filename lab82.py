n=int(input("Введте размер квадрата"))
print("Введите элементы построчно от 1 до n^2")
a=[]
for i in range(n):
    row = []
    for j in range(n):
        print("Строка", i+1, "Столбец", j+1)
        num=int(input())
        row.append(num)
    a.append(row)
print()
print("Квадрат:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
print()

ism=True
for k in range(1, n*n +1):
    count=0
    for i in range(n):
        for j in range(n):
            if a[i][j]==k:
                count+=1
    if count!=1:
        ism=False
tar=0 #Сумма первой строки
for j in range(n):
    tar+=a[0][j]
for i in range(n):
    s=0
    for j in range(n):
        s+=a[i][j]
    if s!=tar:
        ism=False
for j in range(n):
    s=0
    for i in range(n):
        s+=a[i][j]
    if s!=tar:
        ism=False
if ism:
    print("Магический")
else: print("Не магический")