def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
        x= a+1
        return x
    if a<0:
        x=a-2
        return x
    elif a==0:
        x=a+10
        return x
print(main(0))
