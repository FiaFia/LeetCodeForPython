def reverse(self,x):
    flag = True
    
    x = int(str(x)[::-1])
    if x < 0:
        flag = False
        
    res = abs(x)
    
    if res > 2147483647:
        return 0
    
    if not flag:
        return -1*res
    
    return res
