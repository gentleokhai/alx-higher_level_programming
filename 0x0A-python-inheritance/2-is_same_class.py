"""
    Thsi has a function to compare class
"""


def is_same_class(obj, a_class):
    """Returns a bool value to check if instance"""
    if isinstance(obj, a_class):
        v = True
    else:
        v = False
    return v
