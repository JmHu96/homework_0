"""
Egyptian algorithm
"""

def egyptian_multiplication(a, n):
    """
    returns the product a * n

    assume n is a nonegative integer
    """
    def isodd(n):
        """
        returns True if n is odd
        """
        return n & 0x1 == 1

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)


if __name__ == '__main__':
    # this code runs when executed as a script
    for a in [1,2,3]:
        for n in [1,2,5,10]:
            print("{} * {} = {}".format(a, n, egyptian_multiplication(a,n)))


def power(a, n):
    """
    computes the power a ** n

    assume n is a nonegative integer
    """
    
    if n == 1:
        return a
    if n == 0:
        return 1
    
    product = 1
    for i in range(1,n+1):
        product = egyptian_multiplication(product,a)
        
    return product
    
    
if __name__ == '__main__':
    # this code runs when executed as a script
    for a in [3,4,5]:
        for n in [0,1,3,4,5]:
            print("{} ** {} = {}".format(a, n, power(a,n)))
