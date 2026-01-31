def turning_a_list_into_a_dictionary(list_to_turn):
    length_of_list = len(list_to_turn)
    dictionary_for_list = {}

    for item in sorted(set(list_to_turn)):
        amount_of_elements = 0

        for key in list_to_turn:
            if key <= item:
                amount_of_elements += 1

                dictionary_for_list[key] = int((amount_of_elements / length_of_list) * 100)

    return dictionary_for_list

list_to_return = [3, 1, 2, 3, 4, 2]
print(turning_a_list_into_a_dictionary(list_to_return))