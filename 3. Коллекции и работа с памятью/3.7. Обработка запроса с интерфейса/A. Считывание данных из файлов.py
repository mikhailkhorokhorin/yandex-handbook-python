import csv


def main() -> None:
    files = [
        "user.csv",
        "class.csv",
        "class_user_link.csv",
        "task.csv",
        "test.csv",
        "test_task_link.csv",
        "test_class_user_link.csv",
        "test_attempt.csv",
        "task_attempt.csv",
    ]

    counts = [sum(1 for _ in csv.reader(open(f, encoding="utf-8"))) - 1 for f in files]
    print(" ".join(map(str, counts)))


if __name__ == "__main__":
    main()
