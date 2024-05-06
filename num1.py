# Array = [12, 45, 78, 23, 56, 91, 34]
# Output: Array diurutkan [12, 23, 34, 45, 56, 78, 91], elemen array terbesar 12, elemen array terkecil 91

list1 = [12, 45, 78, 23, 56, 91, 34]

list1.sort()

print(list1)
print(f"number terkecil {list1[0]}")
print(f"number terbesar {list1[-1]}")

# [12, 23, 34, 45, 56, 78, 91]
# number terkecil 12
# number terbesar 91