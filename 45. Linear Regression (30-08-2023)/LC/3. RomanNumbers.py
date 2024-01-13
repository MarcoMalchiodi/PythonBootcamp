def RomanNumber(num):
    
    my_num = num
    roman_num = []
    
    roman_numbers = {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
    }
    
    for key,value in roman_numbers.items():
        while my_num >= value:
            roman_num.append(key)
            my_num -= value
        
    return print(''.join(roman_num))
    

RomanNumber(1999)