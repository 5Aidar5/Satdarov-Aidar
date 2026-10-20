num = list(map(int, input("Перестановка").split()))
n = len(num)

i=n-2
while i>=0 and num[i]>=num[i+1]:
    i-=1
if i>=0:
    j=n-1
    while num[j]<=num[i]:
        j-=1
    num[i], num[j] = num[j], num[i]

left=i+1
right=n-1
while left<right:
    num[left], num[right] = num[right], num[left]
    left+=1
    right-=1
print("Результат:", num)