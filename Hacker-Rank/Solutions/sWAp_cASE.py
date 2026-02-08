def swap_case(s):
    
    result = list(s)
    
    for i in range(len(result)):
        
        if result[i].isupper():
            result[i] = result[i].lower()
        elif result[i].islower():
            result[i] = result[i].upper()
        
    return "".join(result)

