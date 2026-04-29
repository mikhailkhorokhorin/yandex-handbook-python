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
