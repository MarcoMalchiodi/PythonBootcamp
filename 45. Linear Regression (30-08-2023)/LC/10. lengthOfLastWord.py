def lengthOfLastWord(s):
    
    temp_str = s[::-1]
    
    for char in temp_str:
        if char == ' ':
            temp_str = temp_str[:temp_str.index(' ')][::-1]
            return print(f"The final word in '{s}' is '{temp_str}' with a length of {len(temp_str)}")
        
    return print("There is only one word...")
        
    



lengthOfLastWord("Mammia mia")