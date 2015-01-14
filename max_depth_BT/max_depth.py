#!/usr/bin/env python

from TreeNode import TreeNode

a = TreeNode(1)

b = TreeNode(2)
a.left = b

c = TreeNode(3)
a.right = c

d = TreeNode(4)
b.left = d

e = TreeNode(5)
b.right = e

print a.val, a.left.val, a.right.val, a.left.left.val, a.left.right.val

w = a.left.left

if w is not None:
    print 'W'

if a is TreeNode.TreeNode:
    print 'a'
