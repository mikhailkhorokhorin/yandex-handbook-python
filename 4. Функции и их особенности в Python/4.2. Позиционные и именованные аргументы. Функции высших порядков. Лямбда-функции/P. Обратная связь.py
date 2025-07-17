def login(username, password, success, error):
    total = sum(ord(i) for i in username) * len(username)
    hex_str = hex(total)[2:]

    if hex_str[::-1].lower() == password.lower():
        success(username)
    else:
        error(username)
