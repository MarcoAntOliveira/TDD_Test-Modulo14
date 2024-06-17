from calculadora import soma


if __name__ =="__main__":
    x = 5
    y = 6

    """
    print(soma(x, y))
    print(soma(6, 7))
    print(soma(80, 56))
    print(soma(89, 90))
    """
    try:
        soma('15', 10)
    except TypeError as e:
        print(f"O erro foi {e}")

