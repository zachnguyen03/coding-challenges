def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents: ")
    sort_list = sorted(english_spanish)
    list_value = []
    for key in sort_list:
        list_value.append(key)
    print(", ".join(list_value))

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word_in_english = input("Enter the word to be translated: ")
            if word_in_english in english_spanish:
                print(word_in_english, "in Spanish is", english_spanish[word_in_english])
            else:
                print("The word", word_in_english, "could not be found from the dictionary.")

        elif command == "A":
            in_english = input("Give the word to be added in English: ")
            in_spanish = input("Give the word to be added in Spanish: ")
            english_spanish[in_english] = in_spanish
            print("Dictionary contents: ")
            sort_list = sorted(english_spanish)
            list_value = []
            for key in sort_list:
                list_value.append(key)
            print(", ".join(list_value))
        elif command == "R":
            removed_word = input("Give the word to be removed: ")
            if removed_word in english_spanish:
                del english_spanish[removed_word]
            else:
                print("The word", removed_word, "could not be found from the dictionary.")
        elif command == "P":
            new_dict = sorted(english_spanish.items())
            l_spain = []
            print("\nEnglish-Spanish")
            for i in new_dict:
                print(i[0], i[1])
                l_spain.append(i[1])
            print("\nSpanish-English")
            for j in sorted(l_spain):
                for k in new_dict:
                    if j == k[1]:
                        print(j, k[0])
            print("")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            sentence_in_list = sentence.split(" ")
            for j in sentence_in_list:
                if j in english_spanish:
                    index = sentence_in_list.index(j)
                    sentence_in_list.insert(index, english_spanish[j])
                    sentence_in_list.remove(j)
            new_sentence = " ".join(sentence_in_list)
            print("The text, translated by the dictionary:")
            print(new_sentence)
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
