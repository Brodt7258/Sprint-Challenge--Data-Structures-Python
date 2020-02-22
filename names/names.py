import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

names_set_1 = set(names_1)

# names_tree_1 = BinarySearchTree(None)

# for name in names_1:
#     names_tree_1.insert(name)

# print('tree_1 assembled')

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_set_2 = set(names_2)

# names_tree_2 = BinarySearchTree(None)

# for name in names_2:
#     names_tree_2.insert(name)

# print('tree_2 assembled')

# duplicates = []  # Return the list of duplicates in this data structure

# Runtime is ~O(n^2), where n is the length of a single list
# List one must be iterated through fully to find duplicates, requiring n steps
# and for each iteration on list one, a linear search is performed against list two,
# requiring another n steps on average. n * n == n^2

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime for this solution should be ~O(n log n). Every entry in tree 1 must be iterated through, requiring n steps.
# But searching tree 2 for duplicates should require only log n steps... assuming that tree 2 is fairly well balanced.
# no promises there, it's a btree, not an avl
# n * log n == n log n

# def append_dupes(item):
#     if names_tree_2.contains(item):
#         duplicates.append(item)

# names_tree_1.for_each(append_dupes)

# no idea why I started with 2 btrees. The only advantage came from searching the second one.
# iterating over the first caused a considerable, and unnecessary slowdown, due to the time needed to build it.
# for name in names_1:
#     if names_tree_2.contains(name):
#         duplicates.append(name)

# Are sets allowed for the stretch? I'm not importing them, and they're absurdly efficient at this.
# They are (obviously) a built-in tool, that I (obviously) did not write myself.
# though the first line of the stretch comment below seems to imply that may be acceptable?
duplicates = names_set_1.intersection(names_set_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
