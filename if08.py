def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if abs(a)>10 and abs(a)<99 and abs(a)%2!=0:
        x="two-digit odd number"
    if abs(a)>10 and abs(a)<99 and abs(a)%2==0:
        x= "two-digit even number"
    if abs(a)>100 and abs(a)<999 and abs(a)%2!=0:
        x="three-digit odd number"
    if abs(a)>100 and abs(a)<999 and abs(a)%2==0:
        x="three-digit even number"
    return x
print(main(561))