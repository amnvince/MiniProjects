#Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

#Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

def solution(n):
    # TODO convert int to roman string
    s=str(n).zfill(4) #zfill fills in leading zeros; makes the number 4 digits
    
    th=int(s[0]) #int for the 1000th place
    hu=int(s[1]) #int for the 100th place
    tn=int(s[2]) #int for the 10th place
    on=int(s[3]) #int for the 1st place
    
    #dictionaries for each digit
    on_rom=["","I","II","III","IV","V","VI","VII","VIII","IX"] 
    tn_rom=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hu_rom=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    th_rom=["","M","MM","MMM"]
    
    return th_rom[th]+hu_rom[hu]+tn_rom[tn]+on_rom[on]