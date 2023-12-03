def compare(a, b) -> int:
    """Compares `a` to `b`.

    Returns:
        -1 if `a < b`, 1 if `a > b`, 0 otherwise

    Condition:
        `a` and `b` must be comparable with < and >

    Examples:
        >>> compare(0, 1)
        -1
        >>> compare('a', 'a')
        0
        >>> compare((2, 1), (1, 2))
        1
    """
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
