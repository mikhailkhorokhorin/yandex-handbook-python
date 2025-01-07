# Дроби v0.2
class Fraction:
    def __try_reduce(self) -> None:
        numerator, denominator = self.__numerator, self.__denominator
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        self.__numerator, self.__denominator = self.__numerator // numerator, self.__denominator // numerator

    def __init__(self, *args) -> None:
        args = tuple(map(int, args[0].split("/"))) if isinstance(args[0], str) else args
        self.sign = 1 if args[0] * args[1] >= 0 else -1
        self.__numerator, self.__denominator = map(abs, (args[0], args[1]))
        self.__try_reduce()

    def numerator(self, number: int = 0) -> int:
        self.__init__(self.sign * number, self.denominator()) if number else ...
        return abs(self.__numerator)

    def denominator(self, number: int = 0) -> int:
        self.__init__(self.sign * self.numerator(), number) if number else ...
        return abs(self.__denominator)

    def __neg__(self):
        return Fraction(self.sign * -self.numerator(), self.denominator())

    def __str__(self) -> str:
        return f"{self.sign * self.numerator()}/{self.denominator()}"

    def __repr__(self) -> str:
        return f"Fraction('{self.sign * self.numerator()}/{self.denominator()}')"
