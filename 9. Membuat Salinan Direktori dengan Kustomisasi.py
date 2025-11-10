import shutil
import os

def copy_directory(src, dst):
    if not os.path.exists(dst):
        shutil.copytree(src, dst)
        print(f"Direktori '{src}' telah disalin menjadi '{dst}'.")
    else:
        print(f"Direktori '{dst}' sudah ada, salinan tidak dilakukan.")

copy_directory('direktori_asli', 'direktori_salinan')


#Fungsi: Menyalin direktori dengan pengecekan apakah direktori tujuan sudah ada.#Kondisi: Ketika Anda ingin mencegah penimpaan direktori yang ada yang bisa menyebabkan kehilangan data.