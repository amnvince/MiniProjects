#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    x=0 #counter for number of characters that have duplicates
    t=text.lower() #makes all characters lowercase
    for i in t:
        count = t.count(i) #counts the number of times a character is repeated
        t=t.replace(i,"") #character is removed so it doesn't get counted again
        if count>1: #if the count is greater than 1, the counter (x) is increased by 1
            x = x+1
            
    return x