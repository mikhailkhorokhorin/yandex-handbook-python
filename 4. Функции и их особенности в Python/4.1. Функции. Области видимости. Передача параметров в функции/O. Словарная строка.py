def get_dict(text: str) -> dict:
    return {
        k.strip(): (
            int(v.strip())
            if v.strip().lstrip("-").isdigit()
            else (
                float(v.strip())
                if "." in v.strip()
                and v.strip().lstrip("-").replace(".", "", 1).isdigit()
                else v.strip()
            )
        )
        for item in text.split(";")
        if item.strip()
        for k, v in [item.split("=", 1)]
        if "=" in item
    }
