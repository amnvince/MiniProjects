#So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise `nil or null or None or Nothing
import math
def gap(g, m, n):
    prime = [] #list of prime numbers
    differences = [] #list of differences between primes
    pair = [] #final pair of numbers if there is a pair
    for x in range(m,n):
        factors = [] #factors for x
        for i in range(2,int(math.sqrt(x))+1): #checking for primeness
            y = x % i
            if y == 0:
                factors.append(i)
        if not factors:
            prime.append(x) #add primes to prime list
            if len(prime)>1: #as long as list has 2 or more elements, check for difference betwwen last nd second last numbers
                differences.append(prime[-1]-prime[-2])
                if differences[-1]==g: #if difference matches g, stop making the list
                    break
    if g not in differences: #if the gap is not in differences, return None
        return None
    pair.append(prime[-2]) #final two numbers in the prime list are the pair with the gap
    pair.append(prime[-1])
    return pair