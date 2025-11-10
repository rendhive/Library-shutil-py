import shutil
import os

src_dir = 'folder_sumber'
dst_dir = 'folder_tujuan'

for filename in os.listdir(src_dir):
    shutil.copy(os.path.join(src_dir, filename), os.path.join(dst_dir, filename))
print("Semua file dari folder sumber telah disalin ke folder tujuan.")

#Fungsi: Menyalin seluruh file dalam bulk dari satu folder ke folder lain.
#Kondisi: Ketika Anda perlu melakukan copy file secara massal dari satu lokasi ke lokasi lain.