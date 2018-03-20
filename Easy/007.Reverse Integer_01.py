def reverse(self,x):
    """
    :type x: int
    :rtype: int
    """
    flag = True
    if x < 0:
        flag = False
    x = abs(x)   
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x //= 10
    if res > 2147483647:
        return 0
    
    if not flag:
        return -1*res

    return res
