"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""

"""
思路1：

首先只想到DFS：  判空，一个dfs辅助函数进行递归，退出条件为左右子节点均为空，则append一条路径，否则，对非空的子节点调用dfs函数，并更新当前根节点的路径信息

"""


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        def dfs(root, string):
            if not root.left and not root.right:
                res.append(string + [str(root.val)])
                # return string
            if root.left:
                dfs(root.left, string + [str(root.val)])
            if root.right:
                dfs(root.right, string + [str(root.val)])
        
        dfs(root, [])

        return ['->'.join(item) for item in res]
