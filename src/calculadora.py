
def soma(x, y):
    """
    >>> soma(30 ,  20)
        50
    >>> soma('a',  20)
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

if __name__ == "__main__":
    pass

def subtrai(x, y):
    """
    >>> subtrai(30 ,  20)
        10
    >>> soma('a',  20)
    typerror

    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose= True)