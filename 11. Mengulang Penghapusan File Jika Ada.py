import shutil
import os

file_path = 'file_salinan.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' telah dihapus.")
else:
    print(f"File '{file_path}' tidak ada.")

#Fungsi: Menghapus file hanya jika memang ada.
#Kondisi: Ketika Anda tidak ingin menimbulkan error jika file yang ingin dihapus tidak ada.