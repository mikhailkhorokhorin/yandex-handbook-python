def main():
    result = []
    for i in [bin(x)[2:] for x in map(int, input().split())]:
        result.append({"digits": len(i),
                       "units": i.count("1"),
                       "zeros": i.count("0")})
    print(result)


if __name__ == "__main__":
    main()
