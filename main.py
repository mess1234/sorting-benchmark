#!/usr/bin/python3


if __name__ == '__main__':
    import sorts
    from testing import sort_many_lists

    NUMBER_OF_LISTS = 200
    SORT_FUNCTIONS = (list.sort,
                      sorts.selection_sort,
                      sorts.insertion_sort,
                      sorts.quicksort,
                      sorts.mergesort,)

    for fn in SORT_FUNCTIONS:
        print('\n' + fn.__name__)
        for list_length in range(100, 1000, 100):
            print(f"With {list_length} items :", end=" ")
            sort_many_lists(fn, list_length, NUMBER_OF_LISTS)
