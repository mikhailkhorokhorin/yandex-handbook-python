def main():
    n = int(input())
    max_length, number, line = 0, 0, 1
    while number < n:
        length = ""
        for i in range(line):
            if number < n:
                number += 1
                length += str(number) + " "
            else:
                break
        line += 1
        max_length = max(len(length[:-1]), max_length)
    number, line = 0, 1
    while number < n:
        answer = ""
        for i in range(line):
            if number < n:
                number += 1
                answer += str(number) + " "
            else:
                break
        line += 1
        print(f"{answer[:-1]:^{max_length}}")


if __name__ == "__main__":
    main()
