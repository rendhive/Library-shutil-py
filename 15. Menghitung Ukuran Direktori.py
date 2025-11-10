import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

size = get_directory_size('direktori_salinan')
print(f"Ukuran 'direktori_salinan' adalah {size} bytes.")

#Fungsi: Menghitung ukuran total dari semua file dalam direktori.
#Kondisi: Ketika Anda perlu memantau penggunaan ruang penyimpanan dalam direktori atau folder tertentu.