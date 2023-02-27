#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.


def create_phone_number(n):
    s=[str(i) for i in n]
    j="".join(s)
    return "("+j[0:3]+") "+j[3:6]+"-"+j[6:10]