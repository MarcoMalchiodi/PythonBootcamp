def removeDuplicates(num_list):
    
    unique_nums = []
    k = 0
    
    for num in sorted(num_list):
        if str(num) not in unique_nums:
            unique_nums.append(str(num))
        else:
            unique_nums.append('_')
            k += 1
    
    unique_nums = sorted(unique_nums)
    my_list = []
    
    for num in unique_nums:
        try:
            my_list.append(int(num))
        except:
            my_list.append(num)
    
    return print(my_list,f'k={k}')

removeDuplicates([6,8,6,9,4,9,9,5])