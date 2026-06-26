class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        cur=root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                
                if not prev.right:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    res.append(cur.val)
                    cur=cur.right
        return res