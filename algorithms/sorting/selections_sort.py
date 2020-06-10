import sys
from load import load_numbers

numbers = load_numbers = sys.argv[1]


def selection_sort(values):
    sorted_list = []
    for idx in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop())
    return sorted_list


def index_of_min(values):
    min_index = 0
    for idx in range(1, len(values)):
        if values[idx] < values[min_index]:
            min_index = idx
    return min_index


print(selection_sort(numbers))
