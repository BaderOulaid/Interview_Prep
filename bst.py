class TreeNode:
    def __init__(self, value, left=None,
                 right=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChid(self):
        return self.parents and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def hasBothChildren(self):
        return self.left and self.right

    def hasAnyChildren(self):
        return self.left or self.right

    def isLeaf(self):
        return not self.hasAnyChildren()


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, data):
        # if no root, then assign node to root.
        # else traverse accodingly and put in place.

        node = TreeNode(value=data)
        if not self.root:
            print "no root, making node root"
            self.root = node
        else:
            self._put(self.root, node)

    def _put(self, root, node):
        if root.value < node.value:
            if root.hasRightChild():
                self._put(root.right, node)
            else:
                node.parent = root
                root.right = node
        else:
            if root.hasLeftChild():
                self._put(root.left, node)
            else:
                node.parent = root
                root.right = node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print root.value
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print root.value

            self.preorder(root.left)
            self.preorder(root.right)

    def get(self, value):
        if self.root:
            result = self._get(self.root, value)
            if result:
                return result.value
            else:
                return None
        else:
            return None


    def _get(self, current_node, value):
        if not current_node:
            return None
        elif current_node.value == value:
            return current_node
        elif current_node.value < value:
            self._get(current_node.right, value)
        else:
            self._get(current_node.left, value)


    def delete(self, value):
        if self.size > 1:
            nodeToDelete = self._get(value)

            if nodeToDelete:
                self.remove(nodeToDelete)
                self.size = self.size - 1
            else: raise ValueError('Error value not in tree')
        elif self.size == 1 and self.root.value == value:
            self.root = None
            self.size = self.size - 1
        else:
            raise ValueError("Error, value not in tree")

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.parent.leftChild == currentNode:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.value = succ.value
        else:
            return False


    def is_balanced(self, root):
        # a bst is balanced if the left subtree and right subtree
        # from the root's height is off
        # by at most one

        if root is None:
            return True

        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1

    def get_height(self, root):
        if root is None:
            return 0
        return 1 + self.get_height(root.left)


bst = BST()
bst.put(5)
bst.put(3)
bst.put(7)
bst.put(2)
bst.put(1)


bst.inorder(bst.root)
print bst.is_balanced(bst.root)
