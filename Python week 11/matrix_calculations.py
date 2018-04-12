class Matrix:
    def __init__(self, matrix_file='', matrix_name=''):
        self.__file = matrix_file
        self.__name = matrix_name
        self.__matrix = []
        # read the matrix in the file into the self.__matrix
        if matrix_file != '':
            with open(matrix_file, mode="r") as file:
                for line in file:
                    row = line.split()
                    row = [int(i) for i in row]
                    self.__matrix.append(row)

        self.__rows = len(self.__matrix)
        if self.__rows > 0:
            self.__columns = len(self.__matrix[0])

    def get_matrix_info(self, info):
        if info == "matrix":
            return self.__matrix
        elif info == "columns":
            return self.__columns
        elif info == "rows":
            return self.__rows

    def print(self):
        print(self.__name, "=", self.__matrix)

    def scalar_multiply(self, scalar_multiplier):
        scalar_product = Matrix()
        for i in self.__matrix:
            result = [j * scalar_multiplier for j in i]
            scalar_product.__matrix.append(result)
        return scalar_product.__matrix

    def matrix_multiply(self, second_matrix):
        product = Matrix()
        r = []
        # iterate through rows of matrix a
        for i in range(self.__rows):
            # iterate through columns of matrix b
            for j in range(second_matrix.get_matrix_info("columns")):
                sums = 0
                # iterate through rows of matrix b
                for k in range(second_matrix.get_matrix_info("rows")):
                    sums += self.__matrix[i][k] * second_matrix.get_matrix_info("matrix")[k][j]
                r.append(sums)
            product.get_matrix_info("matrix").append(r)
            r = []

        return product.get_matrix_info("matrix")


def user_interface():
    matrixes = {}

    while True:

        print(">", end=" ")
        command = input().strip()

        if command == "add":
            matrix_file = input("Enter the name of the matrix file: ")
            matrix_name = input("Enter a name for the matrix: ")
            new_matrix = Matrix(matrix_file, matrix_name)
            matrixes[matrix_name] = new_matrix

        elif command == "quit":
            print("Bye bye!")
            break

        elif command == "print":
            matrix_to_print = input("Name: ")
            if matrix_to_print in matrixes:
                matrixes[matrix_to_print].print()
            else:
                print(f"Name {matrix_to_print} was not found")

        elif command == "list":
            for key in sorted(matrixes):
                matrixes[key].print()

        elif command == "scalarproduct":
            matrix_to_scalar = input("Enter the name: ")
            multiplier = int(input("Enter a multiplier: "))
            if matrix_to_scalar in matrixes:
                print(multiplier, " * ", matrixes[matrix_to_scalar].get_matrix_info("matrix"), "\n", "= ",
                      matrixes[matrix_to_scalar].scalar_multiply(multiplier), sep='')

        elif command == "matrixproduct":
            first = input("1st name: ")
            if first not in matrixes:
                print(f"Name {first} was not found")
                continue
            second = input("2nd name: ")
            if second not in matrixes:
                print(f"Name {second} was not found")
                continue
            if matrixes[first].get_matrix_info("columns") != matrixes[second].get_matrix_info("rows"):
                print("Error, the dimensions of the matrices don't match")
                continue
            print(matrixes[first].get_matrix_info("matrix"), "\n",
                  "* ", matrixes[second].get_matrix_info("matrix"), "\n",
                  "= ", matrixes[first].matrix_multiply(matrixes[second]), sep='')

        else:
            print("Unknown command!")


def main():
    user_interface()


main()