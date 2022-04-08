'''
Leetcode: 110

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
             return True
        if self.get_node_depth(root) < 0:
            return False
        return True
    
    def get_node_depth(self, node):
        if node is None:
            return 1
        ld, rd = self.get_node_depth(node.left), self.get_node_depth(node.right)
        if ld < 0 or rd < 0 or abs(ld-rd) > 1:
            return -1
        
        return max(ld, rd) + 1
