
# 1.	Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 4, 0, 0]

list1 = [8, 3, 12, 4, 7, 2]
list2 = []

for i in list1:
    if i < 5:
        list2.append(0)
    else:
        list2.append(i)
        
list2.sort(reverse= True)

print(list2)

# [12, 8, 7, 0, 0, 0]