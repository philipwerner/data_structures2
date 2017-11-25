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

    def bft(self):
        """Use a generator with breadth first traversal."""
        if self.root is None:
            raise ValueError('The tree is empty')
        breadth = [self.root]
        while breadth:
            curr = breadth.pop(0)
            if curr.left:
                breadth.append(curr.left)
            if curr.right:
                breadth.append(curr.right)
            yield curr.data

    def ordered(self):
        """Use generator for an ordered search."""
        curr = self.root
        searched = []
        if self.root is None:
            raise ValueError('The tree is empty')
        while curr or searched:
            if curr:
                searched.append(curr)
                curr = curr.left
            else:
                curr = searched.pop()
                yield curr.data
                curr = curr.right

    def pre_ordered(self):
        """."""
        curr = self.root
        searched = []
        if self.root is None:
            raise ValueError('The tree is empty')
        while curr or searched:
            if curr:
                yield curr.data
                if curr.right:
                    searched.append(curr.right)
                curr = curr.left
            else:
                curr = searched.pop()

    def post_order(self):
        """."""
        curr = self.root
        searched = []
        child = None
        if self.root is None:
            raise ValueError('The tree is empty')
        while curr or searched:
            if curr:
                searched.append(curr)
                curr = curr.left
            else:
                if searched[-1].right and searched[-1].right is not child:
                    curr = searched[-1].right
                else:
                    child = searched.pop()
                    yield child.data


if __name__ == '__main__':  # pragma: no cover
    import timeit

    insert_time_ub = BST()
    num = (x for x in range(1000))
    a = timeit.timeit('insert_time_ub.insert(next(num))',
                      setup='from __main__ import insert_time_ub, num',
                      number=1000)
    search_time_ub = BST()
    for i in range(100):
        search_time_ub.insert(i)
    b = timeit.timeit('search_time_ub.search(99)',
                      setup='from __main__ import search_time_ub',
                      number=1000)
    c = timeit.timeit('search_time_ub.search(0)',
                      setup='from __main__ import search_time_ub',
                      number=1000)
    insert_time_b = BST()

    def insert_time(val):
        """."""
        if (500 + val) % 2 == 0:
            insert_time_b.insert(500 + val)
        else:
            insert_time_b.insert(500 - val)

    num_b = (x for x in range(1000))
    d = timeit.timeit('insert_time(next(num_b))',
                      setup='from __main__ import insert_time, num_b',
                      number=1000)

    search_time_b = BST()
    for i in range(1000):
        if (500 + i) % 2 == 0:
            search_time_b.insert(500 + i)
        else:
            search_time_b.insert(500 - i)
    e = timeit.timeit('search_time_b.search(999)',
                      setup='from __main__ import search_time_b',
                      number=1000)
    f = timeit.timeit('search_time_b.search(500)',
                      setup='from __main__ import search_time_b',
                      number=1000)

    print('The following time relates to worst case insert.')
    print('Insert unbalanced: {}'.format(a))
    print('Insert balanced: {}'.format(d))
    print('\nThe following time relates to worst case search.')
    print('Search unbalanced leaf: {}'.format(b))
    print('Search balanced leaf: {}'.format(e))
    print('\nThe following time relates to best base search.')
    print('Search unbalanced head: {}'.format(c))
    print('Search balanced head: {}'.format(f))
