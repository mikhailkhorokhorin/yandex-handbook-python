def main():
    k = 0
    while (s := input()) != "Три!":
        k += 1
    for i in range(k):
        print("Режим ожидания...")
    print("Ёлочка, гори!")


if __name__ == "__main__":
    main()
