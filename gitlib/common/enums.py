from enum import Enum


class DiffLineType(Enum):
    """
        Enum for different types of diff line prefixes.
    """
    ADDITION = "+"
    DELETION = "-"
