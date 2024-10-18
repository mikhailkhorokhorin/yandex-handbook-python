def main():
    products = {x for _ in range(3) for x in input().split(", ")}
    for index, product in enumerate(sorted(products)):
        print(f"{index + 1}. {product}")


if __name__ == "__main__":
    main()
