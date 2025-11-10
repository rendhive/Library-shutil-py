import shutil
import os

def safe_remove(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' telah dihapus.")
    else:
        print(f"File '{file_path}' tidak ditemukan.")

safe_remove('file_salinan.txt')

#Fungsi: Menghapus file dengan pemeriksaan untuk memastikan tidak ada error yang ditimbulkan.
#Kondisi: Ketika Anda ingin menghindari kesalahan saat menghapus file yang mungkin tidak ada.