import csv

READ_FILE = "lecturepoints.csv"
WRITTEN_FILE = "lecturepoints_converted.csv"


def main():
    try:
        to_be_read_file = input("Enter the name of the input file: ")
        if to_be_read_file == "":
            to_be_read_file = READ_FILE

        read_file_dialect = input("and its dialect: ")

        to_be_written_file = input("Enter the name of the output file: ")
        if to_be_written_file == "":
            to_be_written_file = WRITTEN_FILE

        write_file_dialect = input("and its dialect: ")

        csv.get_dialect(read_file_dialect)
        csv.get_dialect(write_file_dialect)

        csv_write = open(to_be_written_file, mode='w')
        csv_write = csv.writer(csv_write, dialect=write_file_dialect)

        with open(to_be_read_file, mode='r') as read_file:
            csv_read = csv.reader(read_file, dialect=read_file_dialect)
            for row in csv_read:
                csv_write.writerow(row)

        print()
        print(f"File {to_be_read_file} has been converted into {write_file_dialect}.")

    except csv.Error:
        print()
        print("The given dialect is wrong.")

    except OSError:
        print()
        print("There was an error in handling the file.")


main()
