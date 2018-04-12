class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))

    def simplify(self):
        a = self.__numerator
        b = self.__denominator
        self.__numerator = a // greatest_common_divisor(a, b)
        self.__denominator = b // greatest_common_divisor(a, b)

    def complement(self):
        complement = Fraction(self.__numerator, self.__denominator)
        complement.__numerator = self.__numerator * (-1)
        complement.__denominator = self.__denominator
        return complement

    def reciprocal(self):
        reciprocal = Fraction(self.__numerator, self.__denominator)
        reciprocal.__numerator = self.__denominator
        reciprocal.__denominator = self.__numerator
        return reciprocal

    def multiply(self, frac2):
        product = Fraction(self.__numerator, self.__denominator)
        product.__numerator = self.__numerator * frac2.__numerator
        product.__denominator = self.__denominator * frac2.__denominator
        return product

    def divide(self, frac2):
        quotient = Fraction(self.__numerator, self.__denominator)
        quotient = quotient.multiply(frac2.reciprocal())
        return quotient

    def add(self, frac2):
        result = Fraction(self.__numerator, self.__denominator)
        result.__denominator = self.__denominator * frac2.__denominator
        result.__numerator = self.__numerator * frac2.__denominator + self.__denominator * frac2.__numerator
        return result

    def deduct(self, frac2):
        difference = Fraction(self.__numerator, self.__denominator)
        difference = difference.add(frac2.complement())
        return difference

    def __lt__(self, frac2):
        a = float(self.__numerator / self.__denominator)
        b = float(frac2.__numerator / frac2.__denominator)
        return a < b

    def __gt__(self, frac2):
        a = float(self.__numerator / self.__denominator)
        b = float(frac2.__numerator / frac2.__denominator)
        return a > b

    def __str__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def main():
    calculator = {}
    arithmetic_operations = {"+": (lambda frac1, frac2: frac1.add(frac2)),
                             "-": (lambda frac1, frac2: frac1.deduct(frac2)),
                             "*": (lambda frac1, frac2: frac1.multiply(frac2)),
                             "/": (lambda frac1, frac2: frac1.divide(frac2))}

    while True:
        print(">", end=" ")
        command = input().strip()

        if command == "add":
            frac_inp = input("Enter a fraction in the form integer/integer: ")
            frac_inp = frac_inp.split("/")
            frac = Fraction(int(frac_inp[0]), int(frac_inp[1]))
            name = input("Enter a name: ")
            calculator[name] = frac

        elif command == "print":
            find_name = input("Enter a name: ")
            if find_name in calculator:
                print(f"{find_name} = ", end="")
                print(calculator[find_name])
            else:
                print(f"Name {find_name} was not found")

        elif command == "list":
            for i, v in sorted(calculator.items()):
                print(f"{i} = ", end="")
                print(v)

        elif command in arithmetic_operations:
            first = input("1st operand: ")
            if first not in calculator:
                print(f"Name {first} was not found")
                continue
            second = input("2nd operand: ")
            if second not in calculator:
                print(f"Name {second} was not found")
                continue
            print(calculator[first], command, calculator[second], "= ", end="")
            result = arithmetic_operations[command](calculator[first], calculator[second])
            print(result)
            result.simplify()
            print(f"simplified {result}")

        elif command == "file":
            try:
                file_name = input("Enter the name of the file: ")
                with open(file_name, mode="r") as file:
                    for line in file:
                        line_parts = line.split("=")
                        name = line_parts[0]
                        frac = line_parts[1]
                        frac_parts = frac.split("/")
                        frac = Fraction(int(frac_parts[0]), int(frac_parts[1]))
                        calculator[name] = frac
            except:
                print("Error: the file cannot be read.")

        elif command == "quit":
            print("Bye bye!")
            break

        else:
            print("Unknown command!")

main()
