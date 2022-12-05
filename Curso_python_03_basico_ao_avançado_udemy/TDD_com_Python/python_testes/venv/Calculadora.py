def soma(x, y):
    """Soma x e y
    >>> soma(10, 20)
    30
    >>> soma(30, 20)
    50
    >>> soma(15, 20)
    35
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)