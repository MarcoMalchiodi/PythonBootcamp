def addBinary(a,b):
    temp_list_a = list(a)
    temp_list_b = list(b)
    temp_list = []
    
    while len(temp_list_a) != len(temp_list_b):
        if len(temp_list_a) > len(temp_list_b):
            temp_list_b.insert(0,'0')
        elif len(temp_list_b) > len(temp_list_a):
            temp_list_a.insert(0,'0')
            
    carry = 0
    
    for n in range(len(temp_list_a) -1,-1,-1): # construct used to create a range of indices in reverse order
        bit_sum = int(temp_list_a[n]) + int(temp_list_b[n]) + carry
        temp_list.append(str(bit_sum %2))
        carry = bit_sum // 2
        
    if carry:
        temp_list.append(str(carry))
    
    return print(''.join(temp_list[::-1]))
    
    
addBinary('1','11')
addBinary("1010", "1011")