'''
Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

'''
方法一
可以参考 007-Reverse Integer,把整数翻转，再判断翻转后的数和原来的数是否相同来判断是否是回文数
1. 不能申请额外空间，所以007-Reverse Integer 方法二中将整数转成字符串，用字符串自带的反转[::-1]的方法就不可用
2. 可以借用007-Reverse Integer 方法一，依旧要注意溢出问题，翻转后不能超过32位 最大值
3. 正负号不用考虑，因为负数不可能是回文数， '-12321' --> '12321-' 是不相等的，所以负数直接返回False
'''

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
