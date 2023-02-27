#Your task is to write a function that takes a string and return a new string with all vowels removed.
#Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    astring = string.replace("a", "")
    Astring = astring.replace("A", "")
    estring = Astring.replace("e", "")
    Estring = estring.replace("E","")
    istring = Estring.replace("i", "")
    Istring = istring.replace("I", '')
    ostring = Istring.replace("o", "")
    Ostring = ostring.replace("O", "")
    ustring = Ostring.replace("u", "")
    Ustring = ustring.replace("U", "")
    return Ustring