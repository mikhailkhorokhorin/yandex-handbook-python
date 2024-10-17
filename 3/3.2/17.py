def main():
    friends = {}
    while (s := input()) != "":
        n1, n2 = s.split()
        if n1 not in friends:
            friends[n1] = [n2]
        else:
            friends[n1].extend([n2])
        if n2 not in friends:
            friends[n2] = [n1]
        else:
            friends[n2].extend([n1])

    friends2 = {x: [] for x in set(friends.keys())}
    pairs = []
    for i, j in friends.items():
        for k in j:
            if (i, k) not in pairs:
                pairs.append((i, k))
                pairs.append((k, i))
                friends2[i].extend(friends[k])
                friends2[k].extend(friends[i])

    for i in friends2:
        friends2[i] = [x for x in set(friends2[i]) if x != i and x not in friends[i]]

    for i in sorted(friends2):
        print(f"{i}: ", end="")
        print(*(sorted(friends2[i])), sep=", ")


if __name__ == "__main__":
    main()
