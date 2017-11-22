"""Test module for the BST."""
import pytest
from bst import BST


@pytest.fixture
def sample_bst():
    """Make an empty BST."""
    return BST()


@pytest.fixture
def filled_bst():
    """Make a filled BST."""
    return BST([10, 7, 12, 23, 2, 1.1, 89, 36, 9.8])
    


def test_size_is_callable(sample_bst):
    """Test that the size is callable."""
    assert sample_bst.size() == 0


def test_insert_to_bst(sample_bst):
    """Test insert method."""
    sample_bst.insert(10)
    assert sample_bst.size() == 1


def test_insert_float(sample_bst):
    """Test inserting float."""
    sample_bst.insert(10.9)
    assert sample_bst.size() == 1


def test_add_iterable_to_bst():
    """Test adding a iterable to BST."""
    a = BST([10, 7, 12, 4])
    assert a.size() == 4


def test_add_float_in_iterable():
    """Test that you can add floats in iterable."""
    a = BST([10.9, 9.8, 7.6])
    assert a.size() == 3


def test_insert_multiple_numbers(sample_bst):
    """Test inserting multiple nodes."""
    sample_bst.insert(9)
    sample_bst.insert(8)
    sample_bst.insert(7)
    assert sample_bst.size() == 3


def test_invalid_input_raises_error(sample_bst):
    """Test value error is raised when input is not valid."""
    with pytest.raises(ValueError):
        sample_bst.insert('@')


def test_can_not_insert_duplicate(sample_bst):
    """Test value error is raised when inserting duplicate node."""
    sample_bst.insert(10)
    with pytest.raises(ValueError):
        sample_bst.insert(10)


def test_search_existing_node(filled_bst):
    """Test search finds an existing node."""
    assert filled_bst.search(23) == 23


def test_depth_of_empty_bst(sample_bst):
    """Test depth method on empty bst returns 0."""
    assert sample_bst.depth(1) == 0


def test_depth_with_one_node(sample_bst):
    """Test depth method with one node returns 0."""
    sample_bst.insert(9)
    assert sample_bst.depth(9) == 0


def test_depth_with_multiple_nodes(filled_bst):
    """Test depth of filled bst."""
    assert filled_bst.depth(23) == 2



