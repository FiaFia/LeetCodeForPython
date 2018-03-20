
'''

https://leetcode.com/problems/reverse-integer/description/

Descirption：Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123  Output:  321
Example 2:

Input: -123  Output: -321
Example 3:

Input: 120  Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
 
'''
方法一
1. 反转的思路
    通过%取余，每次x%10就能得到最后一位
    再用res = res*10 + x%10，对每次得到的结果乘以10构造反转出的整数
    再通过x//=10除法，去掉x最后一位 ,直到所有数字都处理完，跳出while 循环

2. 正负号： 设置一个变量flag跟踪正负数，正数为True，负数为False
3. 反转后溢出问题，最大支持32位带符号，最高位为符号位，所以
     16位整数范围是-2^15~~2^15-1 : -32768到32767
     32位整数范围是-2^31~~2^31-1 : -2147483648到2147483647
4. 以0结尾怎么处理：第一步的算法已经覆盖，不需要单独加逻辑
'''

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
复制代码
 

'''
方法二
python 字符串自带的反转[::-1]
1. 可以先把整数转换成字符串，反转后再把字符串转换成整数  x = int(str(x)[::-1])
2. 正负号:设置一个变量flag跟踪正负数，正数为True，负数为False
3. 溢出判断：同方法一
'''

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
复制代码
