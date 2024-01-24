def plusOne(digits):
    
    temp_list = [str(n) for n in digits]
    temp_list = list(str(int(''.join(temp_list))+1))
    
    return print(temp_list)
    
    

plusOne([3,4,9,9])