def roman_to_int(s):
    if len(s) <= 1 or len(s) >= 15 :
        return "Not a valid length"
    if s == "IV" :
        return 4
    if s == "IX" :
        return 9 
    if s == "XL" :
        return 40
    if s == "XC" : 
        return 90 
    if s == "CD" :
        return 400
    if s == "CM" : 
        return 900
    total = 0 
    for i in s :
        if i == "I" :
            total += 1 
        elif i == "V" :
            total += 5 
        elif i == "X" :
            total += 10 
        elif i == "L" :
            total += 50 
        elif i == "C" :
            total += 100 
        elif i == "D" :
            total += 500 
        elif i == "M" :
            total += 1000
        else :
            return "Not a valid input"    
    return total     
#test
s1 = "III"
print(roman_to_int(s1))
s2 = "ABC"
print(roman_to_int(s2))
s3 = "LVIII"
print(roman_to_int(s3))    
s4 = ""
print(roman_to_int(s4))     
