def isPalindrome(x):
    num = x
    num_list = [int(digit) for digit in str(num)]
    central_position = int(len(num_list) / 2)
    
    is_odd_length = False
    if (len(num_list)%2) != 0:
        is_odd_length = True
    
    if is_odd_length:
        left_side = num_list[:central_position]
        right_side = num_list[central_position+1:][::-1]
        
    else:
        middle = int(len(num_list)/2)
        left_side = num_list[:middle]
        right_side = num_list[middle:][::-1]
        
    for n in range(len(left_side)):
        if left_side[n] != right_side[n]:
            return print("It's not a palindrome number!")
        
    return print("It's a palindrome number!")



    


