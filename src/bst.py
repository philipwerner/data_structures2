"""Binary Search Tree."""


class Node(object):
    """A single node."""

    def __init__(self, data, left=None, right=None, parent=None, depth=1):
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

        self.depths_list = []
        self.left_depths_list = []
        self.right_depths_list = []

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
                    curr.left = Node(val, None, None, curr)
                    self._count += 1
                    break
            elif val > curr.data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val, None, None, curr)
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

    def depth(self):
        """Return depth."""
        self.depths_list = []
        depth = 0
        if self.root:
            self._depth_func(self.root, depth)
            return max(self.depths_list)
        return depth

    def _depth_func(self, current, depth):
        if current.right is None and current.left is None:
            self.depths_list.append(depth)
            return
        if current.right:
            return self._depth_func(current.right, depth + 1)
        if current.left:
            return self._depth_func(current.left, depth + 1)

    def contains(self, val):
        """Create method to find if an individual node exists."""
        if self.search(val) is not None:
            return True
        else:
            return False

    def balance(self):
        """Return tree balance."""
        self.depths_list = []
        left_depth = 0
        if self.root.left:
            self._depth_func(self.root.left, left_depth + 1)
            left_depth = max(self.depths_list)

        self.depths_list = []
        right_depth = 0
        if self.root.right:
            self._depth_func(self.root.right, right_depth + 1)
            right_depth = max(self.depths_list)

        return right_depth - left_depth