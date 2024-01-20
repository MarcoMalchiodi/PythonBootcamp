def searchInsert(nums, target):
    
    for n in range(len(nums)):
        if nums[n] == target:
            return print('The target is in position ',n)
            
        else:
            temp_list = nums.copy()
            temp_list.append(target)
            temp_list = sorted(temp_list)
            return print("The new list is ",temp_list,". The target is in position ",temp_list.index(target))
    
    
    
searchInsert([1,2,4,5],2)
searchInsert([1,2,4,5],3)