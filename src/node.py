"""A Node for use with everything."""


class Node(object):
    """A single node."""

    def __init__(self, val, nxt=None):
        """Construct a new Node."""
        self.val = val
        self.nxt = nxt
