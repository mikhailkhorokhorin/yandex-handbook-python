def main():
    d = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_d = sorted(d.items(), key=lambda x: x[1])[::-1]

    for i in range(3):
        print(f"{i + 1}. {sorted_d[i][0]}")


if __name__ == "__main__":
    main()
