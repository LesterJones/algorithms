# This is an implementation of the Bubble Sort Algorithm.

def bubble_sort(arr):
    # Create a copy of the input.
    numbers = arr.copy()
    # Loop through the numbers array, and swap entries when needed.
    # If a loop through the array creates no changes we know we are finished
    # sorting.  We will then return the sorted array.  If changes were made
    # we will loop through the array again.  This will be implimented using
    # a flag to let us know if changes were made.
    flag = True
    while flag:
        flag = False
        i = 0
        while i < len(arr) - 1:
            if numbers[i] > numbers[i+1]:
                holder = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = holder
                flag = True
            i = i + 1
    return numbers