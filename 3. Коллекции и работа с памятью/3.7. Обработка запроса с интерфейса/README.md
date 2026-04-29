# 3.7. Обработка запроса с интерфейса
### A. Считывание данных из файлов
```python
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
```
### B. Статус прохождения тестов учениками
```python
import pandas as pd


def main() -> None:
    user_id, class_id = map(int, input().split())

    cul = pd.read_csv("class_user_link.csv")
    tcul = pd.read_csv("test_class_user_link.csv")
    tests = pd.read_csv("test.csv")
    attempts = pd.read_csv("test_attempt.csv")

    cu_link_id = cul[(cul.user_id == user_id) & (cul.class_id == class_id)].id.iloc[0]
    user_tests = tcul[tcul.class_user_link_id == cu_link_id]

    result = []
    for _, test in user_tests.iterrows():
        title = tests[tests.id == test.test_id].title.iloc[0]

        datetime_started = str(test.datetime_started).split()[0].split(".")
        datetime_started[2] = datetime_started[2][2:]
        datetime_started = ".".join(datetime_started)

        attempt = attempts[attempts.test_class_user_link_id == test.id]
        flag = not attempt.empty and attempt.flag_is_finished.iloc[0]

        result.append((title, datetime_started, flag))

    result.sort(key=lambda x: pd.to_datetime(x[1]), reverse=True)

    passed = sum(flag for _, _, flag in result)
    print(f"{passed}/{len(result)}")
    for title, date_str, flag in result:
        print(title, date_str, "TRUE" if flag else "FALSE")


if __name__ == "__main__":
    main()
```
### C. Обработка тестов
```python
import pandas as pd


def main() -> None:
    user_id, class_id = map(int, input().split())

    class_user_link = pd.read_csv("class_user_link.csv")
    test_class_user_link = pd.read_csv("test_class_user_link.csv")
    test_task_link = pd.read_csv("test_task_link.csv")
    test_attempt = pd.read_csv("test_attempt.csv")
    tasks = pd.read_csv("task.csv")
    task_attempt = pd.read_csv("task_attempt.csv")

    cu_link_id = class_user_link[
        (class_user_link.user_id == user_id) & (class_user_link.class_id == class_id)
    ].id.iloc[0]

    user_tests = test_class_user_link[
        test_class_user_link.class_user_link_id == cu_link_id
    ]
    test = user_tests.iloc[-1]

    user_test_id = test_attempt[
        test_attempt.test_class_user_link_id == test.id
    ].id.iloc[0]
    tasks_ids = test_task_link[test_task_link.test_id == test.test_id].task_id
    test_tasks = pd.merge(tasks_ids, tasks, left_on="task_id", right_on="id")

    opened_tasks = 0
    solved_tasks = 0
    time_spent = 0
    results = []

    for i, task in test_tasks.iterrows():
        task_id, correct = task.id, task.correct_answer
        ut = task_attempt[
            (task_attempt.test_attempt_id == user_test_id)
            & (task_attempt.task_id == task_id)
        ]
        answer = "?"
        if not ut.empty and ut.time_spent.iloc[0] > 0.0:
            opened_tasks += 1
            time_spent += ut.time_spent.iloc[0]
            if ut.answer.iloc[0] == correct:
                solved_tasks += 1
                answer = "TRUE"
            else:
                answer = "FALSE"
        results.append((i + 1, answer, task_id))

    opened_pct = opened_tasks / len(test_tasks) * 100
    solved_pct = solved_tasks / opened_tasks * 100 if opened_tasks else 0.0
    print(f"{opened_pct:.01f}% {solved_pct:.01f}%")

    for a, b, c in results:
        print(a, b, c)

    h, rem = divmod(int(time_spent), 3600)
    m, s = divmod(rem, 60)
    print(f"{h:02d}:{m:02d}:{s:02d}")


if __name__ == "__main__":
    main()
```
### D. Подготовка JSON для передачи
```python
import pandas as pd
import json


def main() -> None:
    user_id, class_id = map(int, input().split())

    cul = pd.read_csv("class_user_link.csv")
    tcul = pd.read_csv("test_class_user_link.csv")
    tests = pd.read_csv("test.csv")
    test_task_link = pd.read_csv("test_task_link.csv")
    test_attempt = pd.read_csv("test_attempt.csv")
    tasks = pd.read_csv("task.csv")
    task_attempt = pd.read_csv("task_attempt.csv")
    users = pd.read_csv("user.csv")

    user_row = users[users.id == user_id].iloc[0]
    user_info = {
        "user_id": user_id,
        "full_name": f"{user_row.last_name} {user_row.first_name}",
        "class_id": class_id,
    }

    cu_link_id = cul[(cul.user_id == user_id) & (cul.class_id == class_id)].id.iloc[0]
    user_tests = tcul[tcul.class_user_link_id == cu_link_id]

    tests_completed = 0
    test_accuracy = []
    tests_dict = []

    for _, test in user_tests.iloc[::-1].iterrows():
        attempt = test_attempt[test_attempt.test_class_user_link_id == test.id]
        flag = not attempt.empty and attempt.flag_is_finished.iloc[0]
        if flag:
            tests_completed += 1

        user_test_id = test_attempt[
            test_attempt.test_class_user_link_id == test.id
        ].id.iloc[0]
        tasks_ids = test_task_link[test_task_link.test_id == test.test_id].task_id
        test_tasks = pd.merge(tasks_ids, tasks, left_on="task_id", right_on="id")

        date_str = str(test.datetime_started).split()[0].split(".")
        date_str[2] = date_str[2][2:]
        date_str = ".".join(date_str)

        opened = 0
        solved = 0
        time_spent = 0
        results = []

        for i, task in test_tasks.iterrows():
            task_id, correct = task.id, task.correct_answer
            ut = task_attempt[
                (task_attempt.test_attempt_id == user_test_id)
                & (task_attempt.task_id == task_id)
            ]
            answer = "?"
            if not ut.empty and ut.time_spent.iloc[0] > 0.0:
                opened += 1
                time_spent += ut.time_spent.iloc[0]
                answer = "TRUE" if ut.answer.iloc[0] == correct else "FALSE"
                solved += answer == "TRUE"
            results.append((i + 1, answer, task_id))

        h, rem = divmod(int(time_spent), 3600)
        m, s = divmod(rem, 60)
        time_str = f"{h:02d}:{m:02d}:{s:02d}"

        if opened:
            test_accuracy.append(solved / opened * 100)

        tests_dict.append(
            {
                "test_id": test.test_id,
                "title": tests[tests.id == test.test_id].title.iloc[0],
                "tasks": [
                    {"order_number": a, "task_id": c, "is_correct": b}
                    for a, b, c in results
                ],
                "progress_percent": round(opened / len(test_tasks) * 100, 1),
                "correct_percent": (
                    0.0 if opened == 0 else round(solved / opened * 100, 1)
                ),
                "time": time_str,
                "date_assigned": date_str,
            }
        )

    result = {
        "user": user_info,
        "progress": {
            "tests_completed": tests_completed,
            "tests_total": len(user_tests),
            "accuracy_average_percent": round(
                sum(test_accuracy) / len(test_accuracy), 1
            ),
        },
        "tests": tests_dict,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
```
