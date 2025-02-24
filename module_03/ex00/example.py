from NumPyCreator import NumPyCreator

npc = NumPyCreator()

# from_list
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
# Output: array([[1, 2, 3], [6, 3, 4]])

# from_tuple
print(npc.from_tuple(("a", "b", "c")))
# Output: array(['a', 'b', 'c'])

# from_iterable
print(npc.from_iterable(range(5)))
# Output: array([0, 1, 2, 3, 4])

# from_shape
print(npc.from_shape((3, 5)))
# Output: array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

# random
print(npc.random((3, 5)))

# identity
print(npc.identity(4))
# Output: array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])
