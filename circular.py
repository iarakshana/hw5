#!/usr/bin/env python

def isprime(n):
    #make sure n is a positive integer
    n = abs(int(n))
    #0 and 1 are not primes
    if n < 2:
        return False
    if n == 2:
        return True
    #every other even number is not prime
    if not n & 1:
        return False
    #range starts with 3 and only needs to go up the squareroot of nfor all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def newrotation(y, n):
    #Checks the rotation of each prime number for primes
    c = 0
    while n != c:#everything but 0
        j = y[1:]
        r = y[0]
        j.append(r)
        s = ''.join(j)
        c = int(s)
        if isprime(c):
            pass
        else:
            return "False"
        y = list(str(s))
    return "True"

top = 1000000
def main():
    R = []
    for n in range(10, top):
        if isprime(n):
            y = list(str(n))
            if newrotation(y, n) == "True":
                R.append(n)
            else:
                continue
    # add 4 to the total (manually add prime 2, 3, 5, and 7)
    solution = (len(R) + 4)
    print(solution)

if __name__ == '__main__':
    main()
# First build your Sieve of Eratosthenes.
#  - It starts out all "true" except 0 and 1.
#  - Every time you find a prime p,
#      switch every multiple of p^2 to False,
#  - Then continue to the next True value.
# You can also apply some additional constraints
# to make a restricted list of primes to consider
# as "circular" primes.  No circular prime except
# 2 itself, will contain the digit "2".


# Next, loop over your primes and rearrange them
# to check if all the possible rearrangements
# are themselves prime.  I


print(solution)
