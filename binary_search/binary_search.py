import matplotlib.pyplot as plt
import random
import time

# Create a binary search function that takes a list of numbers, and a number to search for.
# In our test case the search term will always be in the number_list.


def binary_search(number_list, search_for):
    lower_index = 0
    upper_index = len(number_list)
    index = len(number_list) // 2

    while True:
        if number_list[index] == search_for:
            return index
        else:
            if number_list[index] > search_for:
                upper_index = index
            else:
                lower_index = index
            index = (upper_index + lower_index) // 2


# Test the binary_search on a number of lists and graph the results.

i = 10000
lengths = []
times = []
while i < 100000000000000000:
    numbers = range(i)
    search = random.randint(0, i-1)
    start_time = time.time()
    binary_search(numbers, search)
    total_time = time.time() - start_time
    lengths.append(i)
    times.append(total_time)
    i = i + 10000000000000

plt.scatter(lengths, times)
plt.show()
