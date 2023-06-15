# Merge sort recursively splits a list, and rejoins the sorted pieces.

def merge_sort(arr):
    # Base Case for our recursive call.  If the array is longer than one.  Split it in half,
    # and call each half.
    if len(arr) == 1:
        return arr
    else:
        number = len(arr) // 2
        left_side = merge_sort(arr[0:number])
        right_side = merge_sort(arr[number::])

    # Once, we have a left and a right side we have to merge them together and return them.
    left_side.reverse()
    right_side.reverse()
    merged_numbers = list()
    while len(left_side) != 0 and len(right_side) != 0:
        if left_side[-1] < right_side[-1]:
            holder = left_side.pop()
        else:
            holder = right_side.pop()
        merged_numbers.append(holder)
    
    if len(left_side) > 0:
        left_side.reverse()
        merged_numbers.extend(left_side)
    if len(right_side) > 0:
        right_side.reverse()
        merged_numbers.extend(right_side)
    
    return merged_numbers