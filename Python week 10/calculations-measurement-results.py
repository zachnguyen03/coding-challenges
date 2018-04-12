'''
Introduction to Programming - TIE-02106
Calculations Measurement Results...
'''


DEFAULT_READ = "ovendata.csv"
DEFAULT_WRITE = "ovendata_changes.csv"


def read_write_file(file_read, file_write):
    try:
        file_to_read = open(file_read, 'r')
        file_to_write = open(file_write, 'w')
        next(file_to_read)
        # file_to_write.write('\n')
        coeff = [3600, 60, 1]
        line = file_to_read.readline()
        parts = line.strip().split(';')
        time = parts[0]
        time = time.split(':')
        last_time = 0
        for i in range(len(coeff)):
            last_time += coeff[i] * int(time[i])
        last_temperature = parts[1:]
        cycle = 0
        line = file_to_read.readline()
        while line:
            temperature_change = []
            time_in_second = 0
            parts = line.strip().split(';')
            time = parts[0]
            temperature = parts[1:]
            time = time.split(':')
            # print(time)
            for i in range(len(coeff)):
                time_in_second += coeff[i] * int(time[i])
            if time_in_second < last_time:
                cycle += 1
            time_in_second += cycle * 86400
            interval = time_in_second - last_time
            for i in range(len(temperature)):
                temperature[i] = temperature[i].replace(',', '.')
                last_temperature[i] = last_temperature[i].replace(',', '.')
                change = round(((float(temperature[i])-float(last_temperature[i]))/interval), 1)
                temperature_change.append(change)
            last_time = time_in_second
            last_temperature = temperature
            # print(time_in_second)
            # print(temperature)
            file_to_write.write(str(float(interval)))
            for temp in temperature_change:
                file_to_write.write(';')
                file_to_write.write(str(temp))
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
