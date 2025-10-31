''' Generator '''

'''
Call karne pr hume milta hai iterator object. ya return karta hai.
meanwhile yeh pause ho jata hai.
'''
import math

def first_n_primes(n):
    count = 0
    x = 2
    while count < n:
        for p in range(2, int(math.sqrt(x)) + 1):
            if x % p == 0:
                break
        else:
            yield x  
            count += 1
        x += 1

# Example: print first 10 primes
print(list(first_n_primes(10)))


#Example - 2
'''
def fun():
    yield 10
    yield 20

it=fun()
for x in it:
    print(x)
'''