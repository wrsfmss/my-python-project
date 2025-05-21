"""Test module for example mathematical operations.

This module contains tests for the basic mathematical operations.
"""

from my_python_project.example import calculate_product, calculate_sum


def test_calculate_sum() -> None:
    """Test the calculate_sum function with various inputs."""
    # Test with positive numbers
    assert calculate_sum(1, 2) == 3

    # Test with negative numbers
    assert calculate_sum(-1, -2) == -3

    # Test with zero
    assert calculate_sum(0, 0) == 0

    # Test with floating point numbers
    assert calculate_sum(1.5, 2.5) == 4.0


def test_calculate_product() -> None:
    """Test the calculate_product function with various inputs."""
    # Test with positive numbers
    assert calculate_product(2, 3) == 6

    # Test with negative numbers
    assert calculate_product(-2, 3) == -6

    # Test with zero
    assert calculate_product(0, 5) == 0

    # Test with floating point numbers
    assert calculate_product(2.5, 2) == 5.0
