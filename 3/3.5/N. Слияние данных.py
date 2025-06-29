import json


def main() -> None:
    files = [input() for _ in range(2)]
    data = [{}, {}]
    for i in range(2):
        with open(files[i], "r") as file:
            data[i] = json.load(file)

    data[0] = {
        i["name"]: {key: value for key, value in i.items() if key != "name"}
        for i in data[0]
    }
    for param in data[1]:
        if param["name"] in data[0]:
            for key in param:
                if (
                    key not in data[0][param["name"]]
                    or param[key] > data[0][param["name"]][key]
                ) and key != "name":
                    data[0][param["name"]][key] = param[key]
        else:
            data[0][param["name"]] = {
                key: value for key, value in param.items() if key != "name"
            }

    with open(files[0], "w") as file:
        json.dump(data[0], file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
