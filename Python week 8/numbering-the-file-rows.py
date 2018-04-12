def print_lines(input_file):
    file = open(input_file, "r")
    num_of_lines = sum(1 for line in input_file)
    while line != "":
        