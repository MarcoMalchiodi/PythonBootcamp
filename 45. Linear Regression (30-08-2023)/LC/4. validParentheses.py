def validParentheses(str):
    temp_list = list(str)
    
    for n in range(len(temp_list)):
        if (temp_list[n] == '[' and temp_list[n+1] != ']') or (temp_list[n] == '{' and temp_list[n+1] != '}') or (temp_list[n] == '(' and temp_list[n+1] != ')'):
            return print("It's not valid")
    
    return print("It's valid")
            
    
    

validParentheses('[](){}[}')
validParentheses('[](){}[]')