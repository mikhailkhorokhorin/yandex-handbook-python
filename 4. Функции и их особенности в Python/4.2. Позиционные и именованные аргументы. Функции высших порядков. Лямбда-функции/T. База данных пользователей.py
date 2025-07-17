import re
from datetime import datetime

db = []


def insert(*users):
    db.extend(users)


def select(condition=None):
    result = db

    if condition:
        field, op, value = re.split(r"\s*(<=|>=|==|!=|<|>)\s*", condition)

        def convert(val, field_name):
            if field_name == "birth":
                return datetime.strptime(val, "%d.%m.%Y")
            elif field_name == "id":
                return int(val)
            else:
                return val

        value = convert(value, field)
        ops = {
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
        }

        result = list(
            filter(
                lambda user: ops[op](convert(user[field], field), value), db
            )
        )

    return sorted(result, key=lambda user: user["id"])
