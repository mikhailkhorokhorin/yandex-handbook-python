def main():
    n = input()
    print(*[f"{n.split().index(s) + 1}. {s}" for s in n.split()], sep="\n")


if __name__ == "__main__":
    main()
