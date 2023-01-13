import model.daftar_nilai as dn
import view.input_nilai as nn
		

running = True
while running :
	perintah = input("(L)ihat, (T)ambah, (U)bah, (H)apus,(K)eluar : ")
	if perintah  == "t":
		nn.addnew()
		
	
	elif perintah == "k":
		a = input("Sure want to quit y/t = ")
		if a == "y":
			break

	elif perintah == "h":
		dn.hapus_data()

	elif perintah == "l":
		dn.carinama()

	elif perintah == "u":
		dn.ubah_data()

	else:
		print("Tidak ada data ditemukan")




		





