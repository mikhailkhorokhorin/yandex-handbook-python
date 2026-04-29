from json import loads


def main() -> None:
    with open("app.log", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines_dict = map(lambda line: loads(line), lines)

    unique_users = set()
    popularity_tasks = dict()

    for data in lines_dict:
        if data["handler"] == "attempt_handler" and data["response"][0] == 200:
            params = data["params"]
            unique_users.add(params["name"])
            popularity_tasks[params["task"]] = (
                popularity_tasks.get(params["task"], 0) + 1
            )

    sorted_pop_tasks = sorted(popularity_tasks.items())
    max_populatity_taks = max(popularity_tasks.items(), key=lambda x: x[1])
    print("Analytics Results:")
    print(f"Unique users who solved tasks: {len(unique_users)}")
    print(f"Unique users list: {', '.join(sorted([*unique_users]))}")
    print(f"Task popularity: { {key: val for key, val in sorted_pop_tasks} }")
    print(
        f"Most popular task: '{max_populatity_taks[0]}' with {max_populatity_taks[1]} attempts"
    )


if __name__ == "__main__":
    main()
