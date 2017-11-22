"""Test module for the BST."""
import pytest
from bst import Node, BST


@pytest.ficture
def test_bst():
    """Make an empty BST."""
    return BST()


def test_add_to_bst(test_bst):
    """Test insert method."""
    assert test_bst.insert(2)
