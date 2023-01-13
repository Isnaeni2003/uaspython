import sys
sys.path.append('../')

import mainan.model.daftar_nilai as dn

def addnew():
	nama = input("Masukkan Nama :")
	nim = int(input("Masukkan NIM :"))
	tugas = int(input("Masukkan Nilai Tugas : "))
	uts = int(input("Masukkan Nilai UTS : "))
	uas = int(input("Masukkan Nilai UAS : "))
	if not nama == "" and not nim == "" and not tugas == "" and not uts =="" and not uas =="":
		dn.tambah(nama=nama,nim=nim,tugas=tugas,uts=uts,uas=uas)


