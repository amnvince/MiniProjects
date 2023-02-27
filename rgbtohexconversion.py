#The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

#Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

#The following are examples of expected output values:

#rgb(255, 255, 255) # returns FFFFFF
#rgb(255, 255, 300) # returns FFFFFF
#rgb(0,0,0) # returns 000000
#rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    hex_r=[]
    hex_g=[]
    hex_b=[]
    hex=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"] #a list to translate numbers to hexidecimal based on index
    #cases where the numbers are <0 or >255
    if r<=0:
        hex_r=[0,0]
    if g<=0:
        hex_g=[0,0]
    if b<=0:
        hex_b=[0,0]
    if r>255:
        r=255
    if g>255:
        g=255
    if b>255:
        b=255
        
    if 0<r<16: #if number is small than 16, does not need to be converted
        hex_r=[0,r]
    else: #if 16 or greater, must be converted to base 16 
        while r>0:
            hex_r.append(r%16) #remainder gets added to hexidecimal number
            r=r//16 #r becomes the result
        hex_r.reverse() #reverse the order, since hxidecial is right to left
    if 0<g<16:
        hex_g=[0,g]
    else:
        while g>0:
            hex_g.append(g%16)
            g=g//16
        hex_g.reverse()
    if 0<b<16:
        hex_b=[0,b]
    else:
        while b>0:
            hex_b.append(b%16)
            b=b//16
        hex_b.reverse()
        
    hex_r_string="" #making hex strings for final output
    hex_g_string=""
    hex_b_string=""
    for i in range(len(hex_r)):
        hex_r_string+=hex[hex_r[i]] #adding elements from array into the string
    for i in range(len(hex_g)):
        hex_g_string+=hex[hex_g[i]]
    for i in range(len(hex_b)):
        hex_b_string+=hex[hex_b[i]]
    return hex_r_string+hex_g_string+hex_b_string #returning each string