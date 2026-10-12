s = input("Введите слово: ")
new_s = ""
for char in s:
    if char not in new_s:
        new_s += char
print(new_s)