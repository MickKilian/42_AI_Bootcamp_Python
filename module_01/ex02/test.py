from vector import Vector  # Import the Vector class

def test_vector_operations():
    # Test initialization
    v1 = Vector([[1.], [2.], [3.]])
    v2 = Vector([[4.], [5.], [6.]])
    v3 = Vector([[1., 2., 3.]])
    v4 = Vector([[7.]])

    # Test dot product
    assert v1.dot(v2) == 32, f"Expected 32, but got {v1.dot(v2)}"

    # Test transpose
    v1_transpose = v1.T()
    assert v1_transpose.shape == (1, 3), f"Expected shape (1, 3), but got {v1_transpose.shape}"

    # Test addition
    v5 = v1 + v2
    assert v5.values == [[5.], [7.], [9.]], f"Expected [[5.], [7.], [9.]], but got {v5.values}"

    # Test subtraction
    v6 = v1 - v2
    assert v6.values == [[-3.], [-3.], [-3.]], f"Expected [[-3.], [-3.], [-3.]], but got {v6.values}"

    # Test multiplication by scalar
    v7 = v1 * 2
    assert v7.values == [[2.], [4.], [6.]], f"Expected [[2.], [4.], [6.]], but got {v7.values}"

    # Test reverse multiplication by scalar
    v8 = 3 * v1
    assert v8.values == [[3.], [6.], [9.]], f"Expected [[3.], [6.], [9.]], but got {v8.values}"

    # Test division by scalar
    v9 = v1 / 2
    assert v9.values == [[0.5], [1.], [1.5]], f"Expected [[0.5], [1.], [1.5]], but got {v9.values}"

    # Test division by zero
    try:
        v1 / 0
    except ZeroDivisionError:
        pass  # Expected behavior, do nothing
    else:
        assert False, "Expected ZeroDivisionError"

    # Test reverse division (raises error)
    try:
        1 / v1
    except ArithmeticError:
        pass  # Expected behavior, do nothing
    else:
        assert False, "Expected ArithmeticError"

    print("All tests passed!")

# Run the test function
test_vector_operations()
