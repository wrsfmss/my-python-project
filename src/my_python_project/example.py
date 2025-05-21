"""Mathematical operations module.

This module provides basic mathematical operations.
"""

from typing import Union

Number = Union[int, float]


def calculate_sum(a: Number, b: Number) -> Number:
    """Calculate the sum of two numbers."""
    return a + b


def calculate_product(a: Number, b: Number) -> Number:
    """Calculate the product of two numbers."""
    return a * b
