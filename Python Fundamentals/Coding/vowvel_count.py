string = "Haseeb Tariq"
count = 0
for ch in string:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print(count)

sum = lambda a,b:a+b
print(sum(5,6))