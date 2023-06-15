# Selection Sort works by pulling the minimum value from an array, and storing it.
# This process is repeated until all numbers have been used

def selection_sort(arr):
    numbers = arr.copy()
    sorted_numbers = list()
    while len(numbers) > 0:
        minimum = min(numbers)
        sorted_numbers.append(minimum)
        numbers.remove(minimum)
    return sorted_numbers