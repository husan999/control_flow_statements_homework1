def main(a):
    """
    If the number is positive, increase it to 1,otherwise decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    if a>0:
        x=a+1
    else:
        x=a-2
    return x
print(main(-2))