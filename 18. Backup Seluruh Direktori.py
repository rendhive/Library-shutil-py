import shutil

shutil.copytree('folder_sumber', 'backup/folder_sumber_backup')
print("Seluruh direktori 'folder_sumber' telah dibackup.")

#Fungsi: Mengekspor direktori beserta seluruh isinya ke lokasi baru.
#Kondisi: Ketika Anda ingin memastikan salinan utuh dari direktori