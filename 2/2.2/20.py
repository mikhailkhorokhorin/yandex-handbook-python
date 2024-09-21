def main():
    s1, s2, s3 = [input() for _ in range(3)]
    d = [i for i in (s1, s2, s3) if "зайка" in i]
    res = min(d)
    print(res, len(res))


if __name__ == "__main__":
    main()
