start = int(input())
end = int(input())
step = 1 if start < end else -1
for i in range(start, end + step, step):
    print(i, end=" ")
