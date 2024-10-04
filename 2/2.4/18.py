def main():
    number = 1
    n = int(input())
    tree = []
    for i in range(1, n + 1):
        line = []
        for j in range(i):
            if number - 1 < n:
                line.append(number)
                number += 1
        tree.append(line)
    tree = [x for x in tree if x != []]
    print(tree)

if __name__ == "__main__":
    main()
