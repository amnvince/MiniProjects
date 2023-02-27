#Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

#The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    timeInSec = [31536000,86400,3600,60] #year, day, hour, min
    units = ['years', 'days', 'hours', 'minutes', 'year', 'day', 'hour', 'minute'] #units of time, singular is +4 from plural
    time = [] #ints of years, days, hours and mins
    timeString = [] #strings of ints along with their units
    
    
    for i in range(len(timeInSec)):
        time.append(seconds // timeInSec[i]) #divide by timeInSec to find years, days, etc
        seconds = seconds % timeInSec[i] #seconds changes to remainder
        if time[i] > 1:
            timeString.append(str(time[i])+' '+units[i]) #if plural
        if time[i] == 1:
            timeString.append(str(time[i])+' '+units[i+4]) #if singular
    #the remainder of seconds would be <60secs
    if 1<seconds<60:
        timeString.append(str(seconds)+' seconds')
    if seconds == 1:
        timeString.append(str(seconds)+' second')
    
    #add ', ' after every element except the last two
    for x in range(len(timeString)-2):
        timeString[x] = timeString[x] + ', '
    
    #if there is >1 element, add an ' and ' between the last two elements
    if len(timeString) > 1:
        timeString.insert(-1,' and ')
    
    #this will be the output string
    timeStatement=''
    
    #put the string together
    for x in timeString:
        timeStatement=timeStatement+x
    
    return timeStatement