def soma(x, y):
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)