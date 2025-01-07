# На старт! Внимание! Марш!
def main() -> None:
    for i in range(int(input())):
        print('\n'.join(f"До старта {j} секунд(ы)" for j in range(3 + i, 0, -1)))
        print(f"Старт {i + 1}!!!")


if __name__ == "__main__":
    main()
