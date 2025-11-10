import shutil

def manage_files(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)  # Menghapus jika sudah ada
    shutil.copytree(src, dst)
    print(f"Proyek '{src}' telah dikelola dan disalin ke '{dst}'.")

manage_files('proyek_lama', 'proyek_baru')


#Fungsi: Memperbarui dan menyimpan salinan dari proyek.
#Kondisi: Ketika Anda ingin memelihara folder proyek dengan salinan terbaru.