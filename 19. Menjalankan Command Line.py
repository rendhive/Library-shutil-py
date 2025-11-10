import shutil
import subprocess

# Menjalankan command line untuk menyalin file
subprocess.run(["cp", "file_asli.txt", "file_salinan.txt"])
print("File 'file_asli.txt' telah disalin menggunakan command line.")

#Fungsi: Menjalankan perintah sistem dari dalam script.
#Kondisi: Ketika Anda ingin menggunakan command line untuk operasi file tertentu yang lebih efisien daripada menggunakan Python.