def main() -> None:
    discount = full_coast = 0
    while (s := float(input())) != 0:
        discount += s * (s >= 500)
        full_coast += s * (s < 500)
    print(full_coast + discount * 9 / 10)


if __name__ == "__main__":
    main()
