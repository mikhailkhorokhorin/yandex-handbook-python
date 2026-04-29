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
