def main():
    d = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_d = sorted(d.items(), key=lambda x: x[1])[::-1]
    print(sorted_d[0][0])


if __name__ == "__main__":
    main()
