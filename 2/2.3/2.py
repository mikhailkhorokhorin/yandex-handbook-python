def main():
    k = 0
    while (s := input()) != "Приехали!":
        if "зайка" in s:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
