k=float(input("Введите коэффицент (0<k<1)"))
n=int(input("Введите количество частиц"))
print("Сейчас ввод масс")
m=[]
for i in range(n):
    print("Масса частицы", i+1)
    num=float(input())
    m.append(num)
alive=[]
for i in range(n):
    alive.append(True)

count=n
step=1

print()
while count>1:
    first=-1
    for i in range(n):
        if alive[i]:
            if first==-1 or m[i] < m[first]:
                first=i
        
    second=-1
    for i in range(n):
        if alive[i] and i!=first:
            if second == -1 or m[i]<m[second]:
                second=i
    
    if m[first] == m[second]:
        big=first
        small=second
    else:
        big=second
        small=first
    total = m[first]+m[second]
    ener=k*total
    new_m = total - ener
    print("Шаг", step)
    print("Частица", first+1, "с массой", round(m[first],3))
    print("Частица", second+1, "с массой", round(m[second],3))
    print("Затраченная энергия:", second+1, "с массой", round(ener,3))
    print("Новая Частица", big+1, "с массой", round(new_m,3))
    print()

    m[big]=new_m
    alive[small]=False
    count=count-1
    step=step+1
    
print("Осталась одна частица")