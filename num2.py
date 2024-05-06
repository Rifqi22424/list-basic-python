# Array: [1, 2, 3, 2, 4, 3, 5]
# Output: Array setelah menghapus duplikat adalah [1, 2, 3, 4, 5]

list1 = [1, 2, 3, 2, 4, 3, 5]
list1.sort()
list1 = set(list1)
list1 = list(list1)

print(list1)

# [1, 2, 3, 4, 5]