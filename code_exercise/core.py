"""Code for RTS code excercise."""


from collections.abc import Sequence
from typing import TypedDict
from itertools import count

class AboveBelow(TypedDict):
    above:int
    below:int

class SequenceComparison:
    """Compare sequences against a value."""

    def __init__(self):
        """Nothing to initialize."""
        pass

    def above_below(self, sequence:Sequence[int], value:int)->AboveBelow:
        """Count how many values in sequence are above/below value."""
        return {
            "above": sum(i > value for i in sequence),
            "below":sum(i < value for i in sequence),
        }
        

def string_rotation(
    string:str,
    rotation:int,
)->str:
    """Rotate a string."""
    tail = string[0:-rotation:1]
    head = string[-rotation::1]

    return head + tail
