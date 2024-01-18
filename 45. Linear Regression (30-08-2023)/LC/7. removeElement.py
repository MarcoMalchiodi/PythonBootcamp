def removeElement(num_list,value):
    
    temp_list = [str(num) for num in num_list]
    my_list = []
    counter = 0
    
    for num in temp_list:
        if (num == str(value)):
            my_list.append('_')
        else:
            my_list.append(num)
            counter += 1
    
    my_list = sorted(my_list)
    new_list = []
    
    for num in my_list:
        try:
            new_list.append(int(num))
        except:
            new_list.append(num)
            
    return print(f"The new list: {new_list}. k = {counter}")
    
    
    
removeElement([1,1,2,3,1,4,1],1)