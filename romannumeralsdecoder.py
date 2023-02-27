#Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

#Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

def solution(roman):
  #arrays to convert roman strings to an digit using the string's index
  ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
  tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
  huns=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
  thou=["","M","MM","MMM"]
  
  #strings and counters for each "digit"
  one_dec=""
  one_count=0
  ten_dec=""
  ten_count=0
  hun_dec=""
  hun_count=0
  tho_dec=""
  tho_count=0
  
  #loop through characters to find the characters that make up the 1000 digit
  for i in range(len(roman)):
      if roman[i]=="M": #1000 string can only have M
          tho_dec=tho_dec+roman[i] #adding characters to the 1000 string
          tho_count+=1 #number of digits in the 1000 digit string, used to splice characters off oroginal string
      else:
          break #end when an "M" is not the next character (all hundrends, tens and ones have digits that don't start with M)
  roman=roman[tho_count:] #removes characters that have been added to thousand digit string
  
  for i in range(len(roman)):
      if roman[i]=="C" or roman[i]=="D" or roman[i]=="M": #hundreds strings only begin with C or D and could end in an M
          hun_dec=hun_dec+roman[i]
          hun_count+=1
      else:
          break
  roman=roman[hun_count:]
  
  for i in range(len(roman)):
      if roman[i]=="X" or roman[i]=="L" or roman[i]=="C": #tens strings only begin with X or L and could contain a C
          ten_dec=ten_dec+roman[i]
          ten_count+=1
      else:
          break
  roman=roman[ten_count:]
  
  for i in range(len(roman)):
      if roman[i]=="I" or roman[i]=="V" or roman[i]=="X": #ones strings only begin with I or V and could contain an X
          one_dec=one_dec+roman[i]
          one_count+=1
      else:
          break
  roman=roman[one_count:]
  
  #loop through the arrays to find the index that corresponds to the string
  for i in range(len(ones)):
      if one_dec==ones[i]:
          one_dec=i
          
  for i in range(len(tens)):
      if ten_dec==tens[i]:
          ten_dec=i
          
  for i in range(len(huns)):
      if hun_dec==huns[i]:
          hun_dec=i
          
  for i in range(len(thou)):
      if tho_dec==thou[i]:
          tho_dec=i
          
  return int(str(tho_dec)+str(hun_dec)+str(ten_dec)+str(one_dec)) #converts numbers to strings, adds the strings, then converts to back into an int