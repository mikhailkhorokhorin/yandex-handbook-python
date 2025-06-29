class Fraction:
    def __try_reduce(self) -> None:
        numerator, denominator = self.__numerator, self.__denominator
        while denominator:
            numerator, denominator = denominator, numerator % denominator
        self.__numerator, self.__denominator = (
            self.__numerator // numerator,
            self.__denominator // numerator,
        )

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

    def reverse(self):
        return Fraction(self.sign * self.denominator(), self.numerator())

    def __neg__(self):
        return Fraction(self.sign * -self.numerator(), self.denominator())

    def __add__(self, other):
        numerator = (
            self.sign * self.numerator() * other.denominator()
            + other.sign * other.numerator() * self.denominator()
        )
        denominator = self.denominator() * other.denominator()
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        self.__dict__ = self.__add__(other).__dict__
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self.__dict__ = self.__sub__(other).__dict__
        return self

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        numerator = self.sign * self.numerator() * other.sign * other.numerator()
        denominator = self.denominator() * other.denominator()
        return Fraction(numerator, denominator)

    def __imul__(self, other):
        self.__dict__ = self.__mul__(other).__dict__
        return self

    def __truediv__(self, other):
        return self.__mul__(other.reverse())

    def __itruediv__(self, other):
        self.__dict__ = self.__truediv__(other).__dict__
        return self

    def __eq__(self, other):
        return self.__sub__(other).numerator() == 0

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__sub__(other).sign == -1

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self) -> str:
        return f"{self.sign * self.numerator()}/{self.denominator()}"

    def __repr__(self) -> str:
        return f"Fraction('{self.sign * self.numerator()}/{self.denominator()}')"
