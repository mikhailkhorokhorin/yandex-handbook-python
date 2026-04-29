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
