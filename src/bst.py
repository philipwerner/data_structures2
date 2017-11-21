"""Binary Search Tree."""


class Node(object):
    """A single node."""

    def __init__(self, val, left=None, right=None):
        """Construct a new Node."""
        self.val = val
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
        if self.count == 0:
            self.root = Node(val)
            self._count += 1
        else:
            curr = self.root
            while curr:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = Node(val, curr)
                        self._count += 1
                        break
                    else:
                        curr = curr.left
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = Node(val, curr)
                        self._count += 1
                        break
                    else:
                        curr = curr.right

