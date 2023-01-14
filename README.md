# Project UAS Membuat Daftar Nilai Mahasiswa
## Nama : Khaerunnisa Isnaeni Lestari
## Kelas : TI 22 C1

# Struktur Package dan Modul
![package](https://user-images.githubusercontent.com/115929351/212474345-8d3e9a77-381f-4908-be90-7e0179a96771.png)

## Penjelasan

## Model

Pertama saya membuat database untuk menyimpan file dengan nama db.json, di file ini data seperti id, nama, nilai-nilai akan disimpan.
Lalu dalam folder model terdapat file data_nilai.py dan di dalamnya terdapat operasi untuk menambah data, menghapus, mengedit, seta mencari berdasarkan nama. Dan disini saya pakai library bernama Tiny DB, merupakan database ringan untuk python.

- Tambah data :
1. data = {} untuk menampunf list data yang nanti akan terinput
2. Deklarasikan def untuk memanggil tambah data()
3. Dengan ketentuan nama = Input/masukkan nama mahasiswa
4. Masukkan nim dengan = input nim mahasiswa
5. Ketentuan nilai akhir = (tugas)*30/100+(uts)*35/100+(uas)*35/100
6. Lalu gunakan fungsi append untuk menggabungkan smua variabel

- Cari data :
1. Buat variabel dengan inputan integer untuk mencari baris ke berapa sesuai index
2. Kemudian buat list data, saya menggunakan variabel c untuk dimasukkan ke dalam enumarate

- Hapus data :
1. Buat variable dengan inputan integer untuk memasukkan baris berapa yang ingin dihapus
2. Kemudian menggunakan method pop untuk menghapus sebaris data berdasarkan index
3. Dan memanggil kembali fungsi def untuk menampilkan enumarate/table data

- Ubah data :
1. Membuat variable inputan integer untuk mengubah data mahasiswa
2. Membuat inputan baris = masukkan baris yang ingin diubah
3. Membuat inputan kolom = masukkan kolom yang ingin diubah
4. Mengubah data mahasiswa dengan data[kolom][baris], yaitu dengan memakai list baris dan kolom
5. Membuat inputan nilai = masukkan nilai yang ingin diubah
6. Kemudian data ,mahasiswa akan berubah pada kolom nilai

## View

Lalu di folder view terdapat file bernama input_nilai.py. Untuk melakukan pemanggilan file dari folder model. Kita harus menginisiasi packagenya, dan disini terdaoat sebuah fungsi dan fungsi itu, di teruskan dari file yang ada di dalam model yaitu daftar_nilai.py di fungsi addnew sendiri, meminta memasukkan nama, nim dan nilai
