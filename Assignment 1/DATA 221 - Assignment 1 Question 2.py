def dictionary_for_a_list_of_strings(list_of_strings):
    dictionary_of_lists = {}

    for string in list_of_strings:
        length_of_string = len(string)

        if length_of_string % 2 == 0:
            parity = "even"

        else:
            parity = "odd"

        dictionary_of_lists[string] = {
            "length": length_of_string,
            "parity": parity
        }

    return dictionary_of_lists

strings = ["data", "science"]
print(dictionary_for_a_list_of_strings(strings))



