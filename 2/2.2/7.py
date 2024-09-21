def main():
    s = input()
    is_palindrome = s[0] == s[3] and s[1] == s[2]
    if (is_palindrome):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
