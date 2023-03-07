def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if abs(a)%2 == 1 and a > 0:
        x= "positive odd number"

    elif abs(a)%2 == 0 and a >0:
        x = "positive even number"

    elif abs(a)%2 == 1 and a < 0:
        x = "negative odd number"

    elif abs(a)%2 == 0 and a < 0:
        x= "negative even number"

    else:
        x= "the number is zero"


    return x

print(main(-32))

