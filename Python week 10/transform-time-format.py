'''
Introduction to Programming - TIE-02106
Transforming Time Format...
'''


DEFAULT_READ = "ovendata.csv"
DEFAULT_WRITE = "ovendata_seconds.csv"


def read_write_file(file_read, file_write):
    try:
        file_to_read = open(file_read, 'r')
        file_to_write = open(file_write, 'w')
        line = file_to_read.readline()
        file_to_write.write(line)
        # file_to_write.write('\n')
        coefficient = [3600, 60, 1]
        line = file_to_read.readline()
        last_time = 0
        cycle = 0
        while line:
            time_in_second = 0
            parts = line.strip().split(';')
            time = parts[0]
            temperature = parts[1:]
            time = time.split(':')
            # print(time)
            for i in range(len(coefficient)):
                time_in_second += coefficient[i] * int(time[i])
            if time_in_second < last_time:
                cycle += 1
            last_time = time_in_second
            time_in_second += cycle * 86400
            # print(time_in_second)
            # print(temperature)
            file_to_write.write(str(time_in_second))
            for temp in temperature:
                file_to_write.write(';')
                file_to_write.write(temp)
            file_to_write.write('\n')
            line = file_to_read.readline()
        file_to_write.close()
        file_to_write.close()
        print("Information saved successfully.")
    except FileNotFoundError:
        print("Error in reading the file!")
    except PermissionError:
        print("Cannot write to file")


def main():
    file_read = input("Enter the name of the file to be read: ")
    if file_read == "":
        file_read = DEFAULT_READ
    file_write = input("Enter the name of the file to be written: ")
    if file_write == "":
        file_write = DEFAULT_WRITE

    read_write_file(file_read, file_write)


main()
