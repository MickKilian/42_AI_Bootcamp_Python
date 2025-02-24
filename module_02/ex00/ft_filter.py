def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable."""
    if not callable(function_to_apply):
        raise TypeError(f"{function_to_apply} is not a callable function")
    try:
        for item in iterable:
            if function_to_apply(item):
                yield item
    except TypeError as e:
        raise TypeError("ft_filter expected an iterable") from e
