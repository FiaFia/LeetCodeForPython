def isPalindrome(x):
    a = x
    rev_x = 0 
    if x < 0:
        print('%s is negative' % x)
        return False
    while x > 0:
        rev_x = rev_x * 10 + x % 10
        if rev_x > 2147483647:
            print('x is overflow')
            return False
        x //= 10
    if rev_x == a:
        print('%d is Palindrome' % a)
        return True
    else:
        print('%d is not Palindrome' % a)
        return False
