#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import sorts
from testing import sort_many_lists

NUMBER_OF_LISTS = 200
SORT_FUNCTIONS = (list.sort,
                  sorts.selection_sort,
                  sorts.insertion_sort,
                  sorts.quicksort,
                  sorts.mergesort,)

# Create plot
fig, ax = plt.subplots()
ax.set_title(f"Benchmarks results (sorting {NUMBER_OF_LISTS} lists)")
ax.set_xlabel("List length")
ax.set_ylabel("Time in seconds")

xs = np.arange(100, 901, 100)

for fn in SORT_FUNCTIONS:
    print('\n' + fn.__name__)
    # Record performances
    times = list()
    for list_length in xs:
        print(f"With {list_length} items :", end=" ")
        _, t = sort_many_lists(fn, list_length, NUMBER_OF_LISTS)
        times.append(t)
    # Add to plot
    times = np.array(times) / 1e9  # convert nanoseconds to seconds
    ax.plot(xs, times, label=fn.__name__)

# Show results
ax.legend()
plt.show()
