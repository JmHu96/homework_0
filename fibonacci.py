"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""

import time # to compute runtimes
from tqdm import tqdm # progress bar
import numpy as np

# Question 2
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return(fibonacci_recursive(n-2) + fibonacci_recursive(n-1))


# Question 2
def fibonacci_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    for i in range(n-1):
        a,b = [b,a+b]
    
    return b



# Question 3
def fibonacci_power(n):
    # Due to the nature of this problem, A is symmetric, so if B = A@A, then B is symmetric, so does A@B.
    # So we only have to compute 3 entries at max.
    def twobytwosymmul(A,B):
        C11 = A[0,0]*B[0,0]+A[0,1]*B[1,0]
        C12 = A[1,0]*B[0,0]+A[1,1]*B[1,0]
        C22 = A[1,0]*B[0,1]+A[1,1]*B[1,1]
        return np.array([[C11,C12],[C12,C22]])
    
    A = np.array([[1,1],[1,0]]) 
    
    def egyptian_power(A, n):
             
        def isodd(n):
            return n & 0x1 == 1
        
        # Two special cases
        if n == 1:
            return A
        if n == 0:
            return np.array[[1,0],[0,1]]
        
        if isodd(n):
            return twobytwosymmul(egyptian_power(twobytwosymmul(A,A), n//2),A)
        else:
            return egyptian_power(twobytwosymmul(A,A), n//2)
    
    # Everything is the same as above.
    x = np.array([1,0])
    if n == 0:
        return x[1]
    if n == 1:
        return x[0]
    
    A = egyptian_power(A, n-1)
    
    return(A[0,0])
    
    
    
    
    
    
    
    
    
    
    


if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts


    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    ## write your code for problem 4 below...
    
    import matplotlib.pyplot as plt
    plt.loglog(trecursive)
    plt.loglog(titer)
    plt.loglog(tpower)
    plt.legend(["recursive","iteration","power"])
    plt.title('Fibonacci Number VS Runtime')
    plt.xlabel('Fibonacci Number Index')
    plt.ylabel('Runtime')