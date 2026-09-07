# Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with no child
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Node with two children
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def find_min(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# Main program
bst = BST()
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = bst.insert(root, value)

print("Inorder Traversal:")
bst.inorder(root)

print("\nPreorder Traversal:")
bst.preorder(root)

print("\nPostorder Traversal:")
bst.postorder(root)

# Delete a node
root = bst.delete(root, 30)

print("\nAfter deleting 30:")
print("Inorder Traversal:")
bst.inorder(root)