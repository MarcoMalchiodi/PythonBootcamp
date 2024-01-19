def needleHaysack(haysack,needle,):
    
    if needle in haysack:
        temp_needle = list(needle)
        temp_haysack = list(haysack)
        
        for n in range(len(temp_haysack)):
            if temp_haysack[n:(n+len(needle))] == temp_needle:
                print('Index :',n)
    
    else:
        return print('-1')
    
    
    

needleHaysack('sadbutsad','sad')