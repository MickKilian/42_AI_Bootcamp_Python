from functools import reduce

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively."""
    if not callable(function_to_apply):
        raise TypeError(f"{function_to_apply} is not a callable function")
    try:
        iterator = iter(iterable)
        accumulator = next(iterator)  # Take the first element as initial accumulator
        for item in iterator:
            accumulator = function_to_apply(accumulator, item)
        return accumulator
    except TypeError as e:
        raise TypeError("ft_reduce expected an iterable") from e
    except StopIteration:
        raise TypeError("ft_reduce() of empty sequence with no initial value")
