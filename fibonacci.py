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
    # This is the same function as in problem 2, but we write its abbreviation as egymul 
    def egymul(a,n):
        
        def isodd(n):
            return n & 0x1 == 1

        if n == 1:
            return a
        if n == 0:
            return 0

        if isodd(n):
            return egymul(a + a, n // 2) + a
        else:
            return egymul(a + a, n // 2)
    
    def egyptian_power(n):
        A = np.array([[1,1],[1,0]])      
        B = np.array([[1,0],[0,1]])
        for i in range(n):
             B[0,0],B[0,1],B[1,0],B[1,1] = [egymul(A[0,0],B[0,0])+egymul(A[0,1],B[1,0]),
                                            egymul(A[0,0],B[0,1])+egymul(A[0,1],B[1,1]),
                                            egymul(A[1,0],B[0,0])+egymul(A[1,1],B[1,0]),
                                            egymul(A[1,0],B[0,1])+egymul(A[1,1],B[1,1])]
            
        return B
    
    x = np.array([1,0])
    if n == 0:
        return x[1]
    if n == 1:
        return x[0]
    
    A = egyptian_power(n-1)
    #print(A)
    
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