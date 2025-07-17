lambda item: (
    "".join(c for c in item[0].lower() if c.isalpha()),
    (
        sum(item[1])
        if hasattr(item[1], "__iter__")
        and not isinstance(item[1], (str, bytes))
        else item[1]
    ),
)
