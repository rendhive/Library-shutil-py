import os

directory = 'folder_sumber'

print("Isi dari folder_sumber:")
for filename in os.listdir(directory):
    print(filename)

#Fungsi: Menampilkan semua file dalam direktori tertentu.
#Kondisi: Saat Anda ingin melihat apa yang ada di dalam sebuah folder sebelum melakukan operasi lebih lanjut.