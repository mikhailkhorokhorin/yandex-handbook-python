# Ключевой секрет
def secret_replace(text: str, **replaces) -> str:
    result, replaces = "", {d: (v, 0) for d, v in replaces.items()}
    print(replaces)
    for i in text:
        if i in replaces:
            result += replaces[i][0][replaces[i][1] % len(replaces[i][0])]
            replaces[i] = replaces[i][0], replaces[i][1] + 1
        else:
            result += i
    return result
