"""Binary Search Tree."""


class Node(object):
    """A single node."""

    def __init__(self, data, left=None, right=None):
        """Construct a new Node."""
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    """Binary Search Tree object."""

    def __init__(self, iterable=None):
        """Create an instance."""
        self.root = None
        self._count = 0
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Create a insert method."""
        if not isinstance(val, (int, float)):
            raise ValueError('Please enter a number')
        if self.root is None:
            self.root = Node(val)
            self._count += 1
            return

        curr = self.root
        while curr:
            if val == curr.data:
                raise ValueError('Node already exists')
            elif val < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    self._count += 1
                    break
            elif val > curr.data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    self._count += 1
                    break

    def search(self, val):
        """Create search method to find value in BST."""
        if self.root is None or not isinstance(val, (int, float)):
            raise ValueError('Node does not exist')
        curr = self.root
        while curr:
            if val == curr.data:
                return curr.data
            elif val < curr.data:
                curr = curr.left
            elif val > curr.data:
                curr = curr.right

    def size(self):
        """Create size method to return size of bst."""
        return self._count

    def depth(self, root):
        """Create method to return bst depth."""
        if root is None:
            return 0
        if not self.root.left and not self.root.right:
            return 0
        elif self.root.left and not self.root.right:
            return self.depth(self.root.left) + 1
        elif self.root.right and not self.root.left:
            return self.depth(self.root.right) + 1
        else:
            return max(self.depth(self.root.left), self.depth(self.root.right)) + 1

    def contains(self, val):
        """Create method to find if an individual node exists."""
        if self.search(val) is not None:
            return True
        else:
            return False

    def balance(self):
        """Create method that returns how the BST is balanced."""
        if self.root is None:
            return 'The tree is empty.'
        elif not self.root.left and self.root.right:
            return 0
        elif self.root.left and not self.root.right:
            return self.depth(self.root.left)
        elif self.root.right and not self.root.left:
            return self.depth(self.root.right)
        else:
            return self.depth(self.root.right) - self.depth(self.root.left)
