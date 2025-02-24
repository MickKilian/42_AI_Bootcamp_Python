def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable."""
    if not callable(function_to_apply):
        raise TypeError(f"{function_to_apply} is not a callable function")
    try:
        for item in iterable:
            yield function_to_apply(item)
    except TypeError as e:
        raise TypeError("ft_map expected an iterable") from e
