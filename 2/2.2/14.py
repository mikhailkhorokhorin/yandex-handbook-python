def main():
    n = input()
    h = [n[i] + n[j] for i in range(len(n)) for j in range(len(n)) if i != j]
    m = [int(x) for x in h if x[0] != '0']
    print(min(m), max(m))


if __name__ == "__main__":
    main()
