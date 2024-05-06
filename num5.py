# Soal: Manajemen Daftar Belanja

# Andi memiliki sebuah daftar belanjaan dan ingin mengelola daftar tersebut menggunakan beberapa metode array.
# Pada awalnya, daftar belanjaan Andi kosong.

# 1.	Andi menambahkan beberapa item ke daftar belanjaan tersebut menggunakan method append().
# 2.	Andi ingin mengetahui berapa banyak item yang ada dalam daftar belanjaan menggunakan method count().
# 3.	Andi memutuskan untuk menambahkan beberapa item lagi ke daftar belanjaan menggunakan method extend().
# 4.	Kemudian, Andi ingin menghapus salah satu item yang sudah tidak diperlukan lagi dari daftar belanjaan menggunakan method remove().
# 5.	Andi menyadari bahwa ia lupa menambahkan satu item penting ke daftar belanjaan, maka ia menggunakan method insert() untuk menambahkannya di posisi tertentu.
# 6.	Setelah itu, Andi ingin mengurutkan daftar belanjaan secara alfabetis menggunakan method sort().
# 7.	Terakhir, Andi ingin menghapus semua item dari daftar belanjaan karena sudah selesai berbelanja menggunakan method clear().

list1 = []

anggur = "anggur"

list1.append(anggur)
list1.append(anggur)

list1.count(anggur)

list_buah = ["pisang", "apel"]

list1.extend(list_buah)

list1.remove("apel")

list1.insert(1, "semangka")
list1.insert(1, "apel")
list1.insert(1, "alpukat")


list1.sort()
list1.clear()

print(list1)

# []