from compare import compare
from functools import wraps
from random import randrange
from time import perf_counter_ns


def timing(fn):
    @wraps(fn)
    def wrapper(*args, **kwds):
        t0 = perf_counter_ns()
        result = fn(*args, **kwds)
        t1 = perf_counter_ns()
        dt = t1 - t0
        print(f"took {dt / 1e9} seconds.")
        return result
    return wrapper


def is_sorted(l: list, cmp=compare) -> bool:
    """Return True if `l` is sorted in ascending order, False otherwise.

    Arguments:
        l -- a list whose items are comparable with `cmp`

    Keyword Arguments:
        cmp -- comparison function (default: {compare})

    Examples:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([1, 2, 4, 3])
        False
        >>> is_sorted([])
        True
    """
    return all(cmp(x, y) != 1 for x, y in zip(l, l[1:]))


@timing
def sort_many_lists(sort_fn, lst_len: int, nb_lst: int, cmp=compare) -> None:
    for _ in range(nb_lst):
        random_list = list(randrange(lst_len) for _ in range(lst_len))
        sort_fn(random_list)
