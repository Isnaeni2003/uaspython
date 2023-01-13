from tinydb import TinyDB, Query

data = TinyDB('db.json')
User = Query()
def manggil():
	print("==================================================================")
	print("  No  |  Nama  |  NIM  |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
	print("===================================================================")
	for i,x in enumerate(data.all()):
		print(f"  {i}  |  {x['nama']}  |  {x['nim']}  |   {x['tugas']}   |   {x['uts']}   |   {x['uas']}   |   {x['nilai_akhir']}   |")
		

def tambah(**kwargs):
	nama = kwargs['nama']
	nim = int(kwargs['nim'])
	tugas = int(kwargs['tugas'])
	uts = int(kwargs['uts'])
	uas = int(kwargs['uas'])
	nilai_akhir =  float(tugas)*30/100+(uts)*35/100+(uas)*35/100
	main = {"nama":str(nama),"nim":nim, "tugas":tugas, "uts":uts, "uas":uas, "nilai_akhir":nilai_akhir}
	data.insert(main)
	manggil()


def ubah_data():
	manggil()
	nama = input("masukkan nama yang mau di ganti = ")
	print(f"===> edit data  : {nama} <=====")
	nim = int(input("Masukkan NIM :"))
	tugas = int(input("Masukkan Nilai Tugas : "))
	uts = int(input("Masukkan Nilai UTS : "))
	uas = int(input("Masukkan Nilai UAS : "))
	data.update({
		'nim':nim,
		'tugas':tugas,
		'uts':uts,
		'uas':uas,
		},User.nama == nama)
	manggil()


def hapus_data():
	x = input("masukkan nama yang ingin di hapus = ")
	data.remove(User.nama == str(x))
	manggil()


def carinama():
	manggil()
	nama = input("mau cari nama siapa ? = ")
	res = data.search(User.nama == nama)
	print("==================================================================")
	print("  No  |  Nama  |  NIM  |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
	print("==================================================================")
	for x in res:
		print(f"   {x['nama']}  |  {x['nim']}  |   {x['tugas']}   |   {x['uts']}   |   {x['uas']}   |   {x['nilai_akhir']}   |")









		





