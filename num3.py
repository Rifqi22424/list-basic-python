# Array: [1, 2, 3, 2, 4, 3, 5]
# Output: Array setelah menghapus angka 2 dan mengurutkannya secara terbalik adalah [5, 4, 3, 3, 1]

list1 = [1, 2, 3, 2, 4, 3, 5]
list2 = []

for i in list1:
    if i != 2:
        list2.append(i)

list2.sort(reverse= True)
print(list2)

# [5, 4, 3, 3, 1]