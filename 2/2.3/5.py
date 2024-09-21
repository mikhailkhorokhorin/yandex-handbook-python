discount = 0
full_coast = 0
while (s := float(input())) != 0:
    if s >= 500:
        discount += s
    else:
        full_coast += s
print(full_coast + discount * 9 / 10)
