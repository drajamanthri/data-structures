def checkPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
        
    return True 

s = 'abcba'

r = checkPalindrome(s)
print(r)
