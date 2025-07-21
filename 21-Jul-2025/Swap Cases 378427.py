# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    result = ""
    for i in s :
        
        if i.isdigit():
            result+=i
        elif i.islower():
            result+=i.upper()
            
        elif i.isupper():
            result+=i.lower()
        else:
            result+=i
            
    return result