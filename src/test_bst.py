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


# def test_search_when_node_does_not_exist(filled_bst):
#     """Test searching for nonexistint node."""
#     result = filled_bst.search(999)
#     assert result is False


# def test_depth_of_empty_bst(sample_bst):
#     """Test depth method on empty bst returns 0."""
#     assert sample_bst.depth() == NoneType


def test_depth_with_one_node(sample_bst):
    """Test depth method with one node returns 0."""
    sample_bst.insert(9)
    assert sample_bst.depth() == 0


def test_depth_with_multiple_nodes(filled_bst):
    """Test depth of filled bst."""
    assert filled_bst.depth() == 4


def test_contains_with_node_in_bst(filled_bst):
    """Test that true is returned when node contained."""
    assert filled_bst.contains(10) is True


def test_containw_without_node_in_bst(filled_bst):
    """Test that false is returned when node not contained."""
    assert filled_bst.contains(999) is False


def test_balance_is_positive(filled_bst):
    """Test positive balance."""
    assert filled_bst.balance() == 2


def test_balance_is_negative():
    """Test negative balance."""
    a = BST([5, 4, 3, 2, 1, 6])
    assert a.balance() == -3


def test_balance_is_even():
    """Test for balance of 0."""
    a = BST([5, 4, 6, 3, 7, 2, 8])
    assert a.balance() == 0


def test_bft(filled_bst):
    """Test that BFT iterates."""
    iterate = filled_bst.bft()
    assert next(iterate) == 10
    assert next(iterate) == 7
    assert next(iterate) == 12


def test_bft_on_empty_tree(sample_bst):
    """Test value error is raised on empty tree."""
    a = sample_bst.bft()
    with pytest.raises(ValueError):
        next(a)
