# Library-shutil-py
Shutil — Operasi File dan Direktori Tingkat Tinggi

shutil adalah modul Python yang berisi fungsi-fungsi untuk menangani operasi file dan direktori dengan cara yang lebih praktis dibandingkan menggunakan os. Modul ini mendukung proses penyalinan, pemindahan, penghapusan, hingga membuat arsip.


---

Fitur Utama shutil

• Menyalin file dan folder
• Memindahkan file atau direktori
• Menghapus folder secara rekursif
• Membuat file zip atau tar
• Menyalin metadata file (izin, waktu modifikasi, dll.)


---

Menyalin File

import shutil

shutil.copy("source.txt", "destination.txt")   # Menyalin isi file
shutil.copy2("source.txt", "destination.txt")  # Menyalin isi + metadata


---

Menyalin Folder

import shutil

shutil.copytree("src_folder", "backup_folder", dirs_exist_ok=True)


---

Memindahkan File atau Direktori

import shutil

shutil.move("file.txt", "folder_baru/file.txt")


---

Menghapus Folder

import shutil

shutil.rmtree("folder_yang_ingin_dihapus")


---

Membuat Arsip (zip/tar)

import shutil

shutil.make_archive("backup", "zip", root_dir="project_folder")


---

Mendapatkan Penggunaan Disk

import shutil

print(shutil.disk_usage("/"))   # total, used, free dalam bytes


---

Kapan Menggunakan shutil?

• Saat Anda ingin copy/move file dengan simple
• Untuk buat backup folder
• Saat perlu menghapus folder beserta isinya
• Untuk buat arsip zip sebagai distribusi project
• Untuk mengetahui penggunaan disk


---

shutil cocok digunakan ketika Anda bekerja dengan file dan folder dalam skala besar atau ingin melakukan operasi filesystem dengan cara yang lebih praktis dan aman.