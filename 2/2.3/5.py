def main():
    discount, full_coast = 0, 0
    while (s := float(input())) != 0:
        if s >= 500:
            discount += s
        else:
            full_coast += s
    print(full_coast + discount * 9 / 10)


if __name__ == "__main__":
    main()
