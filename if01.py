def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>0:
        x=a+1
        return x
    elif a<0:
        x=a
        return x
print(main(-4))
