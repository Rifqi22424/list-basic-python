# Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian", "kiwi", "pir"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

list1 = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
list2 = []

for i in list1:
    if len(i) >= 5:
        list2.append(i)
print(list2)

# ['jeruk', 'mangga', 'pisang', 'anggur', 'durian']