#Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime'

def divisors(n):
    z = [] #creating a list of divisors
    for x in range(2, n): # checking for non-prime divisors
        y = n % x 
        if y == 0: #checking for numbers that result in no remainder
            z.append(x) #if a divisor is found, it is added to the list
    if not z: # if list is empty, n is a prime number
        return(str(n) + " is prime")
    else: #if list is not empty, return the list of divisors
        return(z)
    pass