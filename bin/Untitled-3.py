print ('Enter the RGB values')

R = int(input ("red"))

if 0 <= R <= 255 :
    print ("red value is true")
    G = int(input ("green"))
    if 0 <= G <= 255 :
        print ("green value is true")
        B = int(input ("blue"))
        if  0 <= B <= 255 :
            print ("blue value is true")
        else:
            print ('The value doesn''t match the criterias')
            print ('please reenter the value of the color blue')
            B = int(input ("blue"))
    else:
        print ('The value doesn''t match the criterias')
        print ('please reenter the value of the color green')
        G = int(input ("green"))
else:
    print ('The value doesn''t match the criterias')
    print ('please reenter the value of the color red')
    R = int(input ("red"))

FR = R / 16
FG = G / 16
FB = B / 16


print ("the final value is :")
print ("#") 
if FR == 10 :
    FR = "A"
elif FR == 11 :
    FR = "B"
elif FR == 12 :
    FR = "C"
elif FR == 13 :
    FR = "D"
elif FR == 14 :
    FR = "E"
elif FR == 15 :
    FR = "F"
print (FR) 

if FG == 10 :
    FG = "A"
elif FG == 11 :
    FG = "B"
elif FG == 12 :
    FG = "C"
elif FG == 13 :
    FG = "D"
elif FG == 14 :
    FG = "E"
elif FG == 15 :
    FG = "ghF"
print (FG)

if FB == 10 :
    FB = "0A"
elif FB == 11 :
    FB = "0B"
elif FB == 12 :
    FB = "0C"
elif FB == 13 :
    FB = "0D"
elif FB == 14 :
    FB = "0E"
elif FB == 15 :
    FB = "0F"
print (FB)
 
