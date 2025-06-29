import json


def main() -> None:
    file_in, file_out = [input() for _ in range(2)]
    numbers = []
    with open(file_in, "r") as file:
        for line in file:
            numbers.extend([int(x) for x in line.split()])
    data = {
        "count": len(numbers),
        "positive_count": len([x for x in numbers if x > 0]),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2)}
    with open(file_out, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
