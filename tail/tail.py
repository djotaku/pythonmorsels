def tail(sequence, number_of_elements):
    if number_of_elements > 0:
        return list(sequence[-number_of_elements:])
    else:
        return []