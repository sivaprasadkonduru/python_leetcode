'''
Leetcode: 43

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
    
        for i in range(len(num1)):
            for j in range(len(num2)):
                val = int(num1[i]) * int(num2[j])
                res[i+j] +=  val
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10

        for i in range(len(res)-1, -1, -1):
            if res[i]:
                break
            
        return ''.join(map(str, res[i::-1]))
