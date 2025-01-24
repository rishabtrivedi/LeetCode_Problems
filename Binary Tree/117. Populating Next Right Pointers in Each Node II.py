class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = collections.deque([root])

        while queue:
            size = len(queue)
            

            for i in range(size):
                node = queue.popleft()
                if i < size-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


#  class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return None

#         queue = collections.deque([root])

#         while queue:
#             size = len(queue)
            

#             for i in range(size):
#                 node = queue.popleft()
#                 if i < size-1:
#                     node.next = queue[0]
#                 if node.left:
#                     queue.append(node.left)

#                 if node.right:
#                     queue.append(node.right)

#         return root

#


"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


"""