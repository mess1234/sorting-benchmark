from collections.abc import Callable
from typing import Any

from compare import compare

ComparisonFn = Callable[[Any, Any], int]  # TypeAlias for comparison function


# ==============================================================
# SELECTION SORT
# ==============================================================

def __swap(l: list, i: int, j: int) -> None:
    """Swaps two items of `l`.

    Arguments:
        l -- a list
        i -- index of the firt item, 0 <= i < len(l)
        j -- index of the second item, 0 <= j < len(l)

    Examples:
        >>> l1 = list(range(7))
        >>> l2 = l1.copy()
        >>> a, b = 3, 5
        >>> __swap(l2, a, b)
        >>> (l1[a], l1[b]) == (l2[b], l2[a])
        True
    """
    l[i], l[j] = l[j], l[i]


def __get_min_index(l: list, a: int, b: int, cmp: ComparisonFn = compare) -> int:
    """
    Arguments:
        l -- a list whose items are comparable with `cmp`
        a -- lower bound
        b -- upper bound

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Returns:
        index of the smallest item in l[a:b]

    Condition:
        0 <= a < b <= len(l)

    Examples:
        >>> l1 = [1, 2, 3, 4, 5, 6, 7, 0]
        >>> __get_min_index(l1, 0, 8)
        7
        >>> __get_min_index(l1, 1, 7)
        1
    """
    min_idx = a
    for i in range(a + 1, b):
        if cmp(l[i], l[min_idx]) == -1:
            min_idx = i
    return min_idx


def selection_sort(l: list, cmp: ComparisonFn = compare) -> None:
    """Sorts `l`.

    Arguments:
        l -- a list whose items are comparable with `cmp`

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Examples:
        >>> from random import randrange
        >>> from testing import is_sorted
        >>> n = 100
        >>> l1 = [randrange(0, n) for _ in range(n)]
        >>> selection_sort(l1)
        >>> is_sorted(l1)
        True
    """
    n = len(l)
    for i in range(n - 1):
        min_idx = __get_min_index(l, i, n, cmp=cmp)
        __swap(l, i, min_idx)


# ==============================================================
# INSERTION SORT
# ==============================================================

def __insert(l: list, i: int, cmp: ComparisonFn = compare) -> None:
    """Insert l[i] in l[0:i+1]. The slice l[0:i] is supposed to be sorted.  

    Arguments:
        l -- a list whose items are comparable with `cmp`
        i -- index of the item to insert in l[0:i+1]

    Keyword Arguments:
        cmp -- comparison function (default: {compare})
    """
    aux = l[i]
    k = i - 1
    while k >= 0 and cmp(aux, l[k]) == -1:
        l[k+1] = l[k]
        k -= 1
    l[k+1] = aux


def insertion_sort(l: list, cmp: ComparisonFn = compare) -> None:
    """Sorts `l`.

    Arguments:
        l -- a list whose items are comparable with `cmp`

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Examples:
        >>> from random import randrange
        >>> from testing import is_sorted
        >>> n = 100
        >>> l1 = [randrange(0, n) for _ in range(n)]
        >>> selection_sort(l1)
        >>> is_sorted(l1)
        True
    """
    # l[0:1] is sorted
    for i in range(1, len(l)):
        # l[0:i] is sorted
        __insert(l, i, cmp=cmp)
        # l[0:i+1] is sorted
    # l[0:len(l)] is sorted


# ==============================================================
# QUICKSORT
# ==============================================================

def __partition(x, l: list, cmp: ComparisonFn = compare) -> tuple[list, list]:
    """Split `l` in two lists `(l1, l2)` such that `l2` contains the items
    greater than `x`.

    Arguments:
        x -- pivot, must be comparable with elements of `l`
        l -- list

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Returns:
        (l1, l2)

    Examples:
        >>> __partition(3, [1, 4, 1, 5, 9, 2])
        ([2, 1, 1], [9, 5, 4])
        >>> __partition(10, [1, 4, 1, 5, 9, 2])
        ([2, 9, 5, 1, 4, 1], [])
        >>> __partition(3, [])
        ([], [])
    """
    if l == []:
        return ([], [])
    l1, l2 = __partition(x, l[1:], cmp=cmp)
    if cmp(l[0], x) == 1:
        l2.append(l[0])
    else:
        l1.append(l[0])
    return (l1, l2)


def quicksort(l: list, cmp: ComparisonFn = compare) -> list:
    """Return a new list containing elements of `l` sorted in ascending order.

    Arguments:
        l -- a list whose items are comparable with `cmp`

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Returns:
        sorted version of `l`

    Examples:
        >>> from random import randrange
        >>> from testing import is_sorted
        >>> n = 100
        >>> l1 = [randrange(0, n) for _ in range(n)]
        >>> l2 = quicksort(l1)
        >>> len(l1) == len(l2)
        True
        >>> is_sorted(l2)
        True
    """
    if len(l) <= 1:
        return l.copy()
    pivot = l.pop()
    l1, l2 = __partition(pivot, l, cmp=cmp)
    l.append(pivot)  # undo l.pop()
    l1 = quicksort(l1, cmp=cmp)
    l2 = quicksort(l2, cmp=cmp)
    return l1 + [pivot] + l2


# ==============================================================
# MERGE SORT
# ==============================================================

def __split(l: list) -> tuple[list, list]:
    """Splits `l` in two lists `(l1, l2)` such that
    `len(l2) - len(l1) == len(l) % 2`.

    Arguments:
        l -- a list

    Returns:
        (l1, l2)

    Examples:
        >>> from random import randrange
        >>> from testing import is_sorted
        >>> n = 100
        >>> l = [randrange(0, n) for _ in range(n)]
        >>> l1, l2 = __split(l)
        >>> len(l2) - len(l1) == len(l) % 2
        True
        >>> l1 + l2 == l
        True
    """
    middle = len(l) // 2
    return (l[:middle], l[middle:])


def __merge(l1: list, l2: list, cmp: ComparisonFn = compare) -> list:
    """Merge two sorted lists.

    Arguments:
        l1 -- a sorted list
        l2 -- a sorted list

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Returns:
        A sorted version of `l1 + l2`

    Examples:
        >>> __merge([1, 3, 4, 9], [1, 2, 5])
        [1, 1, 2, 3, 4, 5, 9]
    """
    if l1 == []:
        return l2.copy()
    if l2 == []:
        return l1.copy()
    if cmp(l1[0], l2[0]) == -1:
        return [l1[0]] + __merge(l1[1:], l2, cmp=cmp)
    return [l2[0]] + __merge(l1, l2[1:], cmp=cmp)


def mergesort(l: list, cmp: ComparisonFn = compare) -> list:
    """Return a new list containing elements of `l` sorted in ascending order.

    Arguments:
        l -- a list whose items are comparable with `cmp`

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Returns:
        sorted version of `l`

    Examples:
        >>> from random import randrange
        >>> from testing import is_sorted
        >>> n = 100
        >>> l1 = [randrange(0, n) for _ in range(n)]
        >>> l2 = quicksort(l1)
        >>> len(l1) == len(l2)
        True
        >>> is_sorted(l2)
        True
    """
    n = len(l)
    if n <= 1:
        return l.copy()
    l1, l2 = __split(l)
    l1 = mergesort(l1, cmp=cmp)
    l2 = mergesort(l2, cmp=cmp)
    return __merge(l1, l2, cmp=cmp)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
