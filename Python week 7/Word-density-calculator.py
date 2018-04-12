def main():
    string = input("Enter rows of text for word counting. Empty row to quit.\n")
    list_of_word = string.split(" ")
    all_words = []
    help_list = []
    for i in list_of_word:
        if i != "":
            all_words.append(i.lower())

            if i.lower() not in help_list:
                help_list.append(i.lower())

    while string != "":
        string = input()
        list_of_word = string.split(" ")
        for i in list_of_word:
            if i != "":
                all_words.append(i.lower())

                if i.lower() not in help_list:
                    help_list.append(i.lower())

    for word in sorted(help_list):
        print(word, ":", all_words.count(word), "times")


main()
