# class BinaryTreeNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#     def insert(self, data):
#         if self.data:
#             if self.data <= data:
#                 if self.left is None:
#                     self.left.BinaryTreeNode(data)
#                 else:
#                     self.left.BinaryTreeNode(data)
#             else:
#                 if self.right is None:
#                     self.right.BinaryTreeNode(data)
#                 else:
#                     self.right.BinaryTreeNode(data)
#         else:
#             self.data = data
#
#     def printTree(self):
#         if self.left:
#             self.left.printTree()
#         print(self.data, end=' ')
#         if self.right:
#             self.right.printTree()
#
#
# l = [50, 100, 45, 11, 15, 30, 78]
# root = BinaryTreeNode(l[0])
# for i in l[1:]:
#     root.insert(i)
# root.printTree()

# node1 = BinaryTreeNode(50)
# node2 = BinaryTreeNode(20)
# node3 = BinaryTreeNode(45)
# node4 = BinaryTreeNode(11)
# node5 = BinaryTreeNode(15)
# node6 = BinaryTreeNode(30)
# node7 = BinaryTreeNode(78)
#
# node1.left = node2
# node2.right = node3
# node2.left = node4
# node4.right = node5
# node3.left = node6
# node1.right = node7


# find = 23
# l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# low = 0
# high = len(l)-1
# mid = low+high//2
# while l:
#     if :


l = [3, 5, 40, 25, 36, 43, 49]
for i in range(len(l)):
    tmp=i
    for j in range(len(l)):
        pass
