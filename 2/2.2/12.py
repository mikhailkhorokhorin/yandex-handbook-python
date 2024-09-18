s1 = int(input())
s2 = int(input())
s3 = int(input())

if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print("YES")
else:
    print("NO")