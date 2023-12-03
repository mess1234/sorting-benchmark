from compare import compare


# ==============================================================
# SELECTION SORT
# ==============================================================

def __swap(l: list, i: int, j: int) -> None:
    (l[i], l[j]) = (l[j], l[i])


def __get_min_index(l: list, a: int, b: int, cmp=compare) -> int:
    ind_min = a
    for i in range(a + 1, b):
        if cmp(l[i], l[ind_min]) == -1:
            ind_min = i
    return ind_min


def selection_sort(l: list, cmp=compare) -> None:
    n = len(l)
    for i in range(n - 1):
        ind_min = __get_min_index(l, i, n, cmp=cmp)
        __swap(l, i, ind_min)


# ==============================================================
# INSERTION SORT
# ==============================================================

def __insert(l: list, i: int, cmp=compare) -> None:
    aux = l[i]
    k = i - 1
    while k >= 0 and cmp(aux, l[k]) == -1:
        l[k+1] = l[k]
        k -= 1
    l[k+1] = aux


def insertion_sort(l: list, cmp=compare) -> None:
    # the slice l[0:1] is sorted
    for i in range(1, len(l)):
        # the slice l[0:i] triée
        __insert(l, i, cmp=cmp)
        # the slice l[0:i+1] is sorted
    # the slice l[0:len(l)] is sorted
