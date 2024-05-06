# Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.
# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]

list1 = [105, 20, 8, 150, 30, 5, 200]
list2 = []

for i in list1:
    if i > 10 and i < 100:
        list2.append(i)
    
list2.sort()

print(list2)

# [20, 30]