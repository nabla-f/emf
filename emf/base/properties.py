import numpy as np

__all__ = [
    'bool_property',
    'str_property',
    'array_property',
]


def bool_property(name):
    """
    Creates a class property that is restricted to boolean values.

    Parameters
    ----------
    name : str
        The variable name.
    """
    name = '_{}'.format(name)

    def fget(self):
        return getattr(self, name)

    def fset(self, value):
        if not isinstance(value, bool):
            value = bool(value)
        setattr(self, name, value)

    def fdel(self):
        delattr(self, name)

    return property(fget=fget, fset=fset, fdel=fdel)


def str_property(name):
    """
    Creates a class property that is restricted to string values.

    Parameters
    ----------
    name : str
        The variable name.
    """
    name = '_{}'.format(name)

    def fget(self):
        return getattr(self, name)

    def fset(self, value):
        if not isinstance(value, str):
            value = str(value)
        setattr(self, name, value)

    def fdel(self):
        delattr(self, name)

    return property(fget=fget, fset=fset, fdel=fdel)


def array_property(name):
    """
    Creates a class property that is restricted to array values.

    Parameters
    ----------
    name : str
        The variable name.
    """
    name = '_{}'.format(name)

    def fget(self):
        return getattr(self, name)

    def fset(self, value):
        value = np.asarray(value)
        setattr(self, name, value)

    def fdel(self):
        delattr(self, name)

    return property(fget=fget, fset=fset, fdel=fdel)