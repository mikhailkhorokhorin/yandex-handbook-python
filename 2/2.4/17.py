def is_palindrome(s):
    return s == s[::-1]


def main():
    print(sum([is_palindrome(input()) for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
