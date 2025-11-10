import shutil

shutil.copy2('file_asli.txt', 'backup/file_asli_backup.txt')
print("Backup dari 'file_asli.txt' telah dibuat.")


#Fungsi: Membuat salinan cadangan dari file dengan metadata.
#Kondisi: Ketika Anda ingin memastikan file yang penting memiliki salinan cadangan.