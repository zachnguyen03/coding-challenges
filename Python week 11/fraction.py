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


    def complement(self):
        """
        Returns the negative fraction of the given fraction
        """
        new_numerator = -self.__numerator
        return Fraction(new_numerator, self.__denominator)



    def reciprocal(self):
        """
        Returns a new fraction where the original numerator and denominator get swapped
        """
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        return Fraction(self.__numerator, self.__denominator)


    def multiply(self, fraction):
        """
        Multiply two fractions and return a new product fraction
        """
        new_numerator = self.__numerator * fraction.__numerator
        new_denominator = self.__denominator * fraction.__denominator
        return Fraction(new_numerator, new_denominator)



    def divide(self, fraction):
        """
        Divide two fractions and return a new fraction
        """
        new_numerator = self.__numerator * fraction.__denominator
        new_denominator = self.__denominator * fraction.__numerator
        return Fraction(new_numerator, new_denominator)


    def add(self, fraction):
        """
        Add two fractions and return a new fraction
        """
        new_denominator = self.__denominator * fraction.__denominator
        new_numerator = (self.__numerator * fraction.__denominator) + (self.__denominator * fraction.__numerator)
        return Fraction(new_numerator, new_denominator)


    def deduct(self, fraction):
        """
        Subtract one fraction to another
        """
        new_denominator = self.__denominator * fraction.__denominator
        new_numerator = (self.__numerator * fraction.__denominator) - (self.__denominator * fraction.__numerator)
        return Fraction(new_numerator, new_denominator)


    def simplify(self):
        """
        Simplify the given fraction
        """
        a, b = self.__numerator, self.__denominator
        gcd = greatest_common_divisor(a, b)
        new_numerator, new_denominator = self.__numerator // gcd, self.__denominator // gcd
        return Fraction(new_numerator, new_denominator)


    def __lt__(self, fraction):
        """ Returns True if this fraction is less than the other
        fraction, false otherwise.
        """
        if not isinstance(fraction, Fraction):
            return NotImplemented
        return self.__numerator * fraction.__denominator < fraction.__numerator * self.__denominator


    def __gt__(self, fraction):
        if not isinstance(fraction, Fraction):
            return False
        return self.__numerator * fraction.__denominator > fraction.__numerator * self.__denominator



    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


    # fraction_list = []
    # print("Enter fractions in the format integer/integer.\nOne fraction per line. Stop by entering an empty line.")
    # while True:
    #     input_fraction = input("")
    #     if str(input_fraction) != "":
    #         split_fraction = str(input_fraction).split("/")
    #         new_fraction = Fraction(int(split_fraction[0]), int(split_fraction[1]))
    #         fraction_list.append(new_fraction)
    #     else:
    #         print("The given fractions in their simplified form:")
    #         for fraction in fraction_list:
    #             # print("{:s} = {:s}").format(fraction, fraction.simplify())
    #             print("%s = %s" % (fraction, fraction.simplify()))
    #         return False

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
            input_fraction = input("Enter a fraction in the form integer/integer: ")
            split_fraction = input_fraction.split("/")
            new_fraction = Fraction(int(split_fraction[0]), int(split_fraction[1]))
            name = input("Enter a name: ")
            calculator[name] = new_fraction

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
            print(f"simplified {result.simplify()}")

        elif command == "file":
            try:
                file_name = input("Enter the name of the file: ")
                with open(file_name, mode="r") as file:
                    for line in file:
                        line_parts = line.split("=")
                        name = line_parts[0]
                        new_fraction = line_parts[1]
                        new_fraction_parts = new_fraction.split("/")
                        fraction = Fraction(int(new_fraction_parts[0]), int(new_fraction_parts[1]))
                        calculator[name] = fraction
            except:
                print("Error: the file cannot be read.")

        elif command == "quit":
            print("Bye bye!")
            break

        else:
            print("Unknown command!")


main()



