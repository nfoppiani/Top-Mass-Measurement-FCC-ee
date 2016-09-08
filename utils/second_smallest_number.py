def second_smallest_number(my_list):
    """Next to the smallest number in a list of numbers."""
    minimum = min(my_list)
    second_min = max(my_list)
    index_second_min = -1
    for i, element in enumerate(my_list):
        if element < second_min and element > minimum:
            second_min = element
            index_second_min = i
    return second_min, index_second_min
