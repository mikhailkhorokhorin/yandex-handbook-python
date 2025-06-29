def main() -> None:
    close_friends = {}
    while (string := input()) != "":
        surname1, surname2 = string.split()
        close_friends.setdefault(surname1, []).append(surname2)
        close_friends.setdefault(surname2, []).append(surname1)

    friends, pairs = {x: [] for x in set(close_friends.keys())}, []

    for key, value in close_friends.items():
        for friend_key in value:
            if (key, friend_key) not in pairs:
                pairs.extend([(key, friend_key), (friend_key, key)])
                friends[key].extend(close_friends[friend_key])
                friends[friend_key].extend(close_friends[key])

    for i in friends:
        friends[i] = [
            x for x in set(friends[i]) if x != i and x not in close_friends[i]
        ]

    for i in sorted(friends):
        print(f"{i}: {', '.join(sorted(friends[i]))}")


if __name__ == "__main__":
    main()
