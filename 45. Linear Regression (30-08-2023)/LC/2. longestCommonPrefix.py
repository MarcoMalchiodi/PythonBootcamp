def longestCommonPrefix(word_list):
    temp_list = [list(word) for word in word_list]
    
    first_word = temp_list[0]
    temp_list = temp_list[1:]
    prefix_list = []
    
    for word in temp_list:
        temp_pref = []
        counter = 0
        
        while word[counter] == first_word[counter]:
            temp_pref.append(word[counter])
            counter += 1
            
        prefix_list.append(''.join(temp_pref))
    
        
    
    return print(min(prefix_list, key=len))

longestCommonPrefix(['attila','attorno','attico'])
    


