print("40.	Create a tuple containing multiple lists. Access and modify the elements inside the lists.")
tuple_of_lists = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

# Accessing elements
print(tuple_of_lists[0])  # Output: [1, 2, 3]
print(tuple_of_lists[1][0])  # Output: 4

# Modifying elements (note: tuples are immutable, so we need to create a new tuple)
new_tuple_of_lists = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)
new_tuple_of_lists[0].append(4)  # This will raise an error since tuples are immutable
