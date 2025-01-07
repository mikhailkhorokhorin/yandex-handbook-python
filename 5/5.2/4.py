# Дроби v0.1
class Fraction:
    def __try_reduce(self) -> None:
        numerator, denominator = self.__numerator, self.__denominator
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        self.__numerator, self.__denominator = self.__numerator // numerator, self.__denominator // numerator

    def __init__(self, *args) -> None:
        args = tuple(map(int, args[0].split("/"))) if isinstance(args[0], str) else args
        self.__numerator, self.__denominator = map(abs, (args[0], args[1]))
        self.__try_reduce()

    def numerator(self, number: int = 0) -> int:
        self.__init__(number, self.denominator()) if number else ...
        return abs(self.__numerator)

    def denominator(self, number: int = 0) -> int:
        self.__init__(self.numerator(), number) if number else ...
        return abs(self.__denominator)

    def __str__(self) -> str:
        return f"{self.numerator()}/{self.denominator()}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator()}, {self.denominator()})"
