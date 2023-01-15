# Project UAS Program Tabel Daftar Nilai Mahasiswa
## Nama : Khaerunnisa Isnaeni Lestari
## Kelas : TI 22 C1

Berikut Link Youtube :

Berikut Tutorial pdf :

# Struktur Package dan Modul
![package@](https://user-images.githubusercontent.com/115929351/212522309-b1702268-f9f4-4708-bf74-f23ce44e1aca.png)

## Penjelasan

## Model

Pada package model ini terdapat 2 file, pertama file init.py hanya untuk menginisiasi package dan file yang kedua ada daftar_nilai.py yang terdiri dari source code untuk menambah data mahasiswa, mengubah data mahasiswa, menghapus data mahasiswa, dan mencari data mahasiswa. Package daftar_nilai.py disini saya memakai from TinyDB untuk menjalankan file db.json yang fungsinya untuk menyimpan data inputan, lalu disini saya memakai fungsi def manggil() untuk menampilkan tabel mahasiswanya.
 
1. data = TinyDB, untuk menginisiasi database untuk dapat menjalankan fungsi menambah, menghapus, mengubah, dan mencari, kemudian disimpan pada file db.json
3. User = Query, membuat variabel untuk Query sebagai perantara untuk menjalankan fungsi
4. Deklarasikan fungsi def manggil untuk memunculkan tabel mahasiswa

## Source Code
![carbon(12)](https://user-images.githubusercontent.com/115929351/212523843-b9a93a1c-4461-4f8e-a0fe-4ccaf9e94cd6.png)

- Tambah data :
1. Memakai def tambah untuk dipanggil pada menu tampilan
2. (**kwargs) = memakai banyak argumen
3. Membuat inputan nama (string), Tugas (integer), NIM (integer), UTS (integer), UAS (integer)
4. Nilai akhir dengan ketentuan, float (Tugas) x 30/100, (UTS) x 35/100, dan (UAS) x 35/100
4. Membuat dict main yang berisi variable tersebut {"nama":str(nama),"nim":nim, "tugas":tugas, "uts":uts, "uas":uas, "nilai_akhir":nilai_akhir}
5. data.insert(main), memakai fungsi insert untuk menambahkan semua item

- Cari data :
1. Buat variabel dengan inputan (string) "mau cari nama siapa", berdasarkan nama
2. Buat variabel res yang berisi data.search kemudian (User.nama, variable user untuk menjalankan Query fungsi mencari data/search)
3. Memanggil def manggil untuk menampilkan tabel mahasiswa

- Hapus data :
1. Buat variable dengan inputan (string) "masukkan nama yang ingin dihapus", berdasarkan nama
2. Lalu menggunakan (User.nama, variable user untuk menjalankan Query fungsi hapus data/remove
3. Dan memanggil kembali fungsi def manggil guna menampilkan tabel mahasiswa

- Ubah data :
1. Membuat variable inputan (string) "masukkan nama yang ingin diganti", berdasarkan nama
2. Membuat inputan integer NIM, Tugas, UAS dan UTS
3. Kemudian data.update kemudian membuat dict dari semua item (nama, nim, tugas, uts, dan uas) serta User.nama ariable user untuk menjalankan Query fungsi mengubah data/update
4. Dan memanggil kembali fungsi def untuk menampilkan tabel mahasiswa

## View

Package kedua ada view terdapat 2 file, yang berisi init.py untuk menginisiasi package dan file input_nilai.py yang berisi import an dari nama projectnya yaitu UASPython, lalu package model dan file daftar_nilai.py, dari package ini saya buat variable (dn). Disini saya membuat def addnew untuk nantinya dipanggil pada tampilan menu, dan inputan ini berisi data mahasiswa yaitu:

## Source Code
![carbon(13)](https://user-images.githubusercontent.com/115929351/212523942-a4cb4329-375b-4034-889d-bae83e1403f6.png)

>> nama   = Masukkan Nama
>> nim    = (int) Masukkan NIM
>> tugas  = (int) Masukkan Nilai Tugas
>> uts    = (int) Masukkan Nilai UTS
>> uas    = (int) Masukkan Nilai UAS
Kemudian terakhir variable dn.tambah, variable (dn) dan fungsi tambah untuk menambahkan semua argumen

## File db.json

Baik, pada file ini merupakan file diluar package-package ini (model dan view) yang berisi simpanan data inputan data mahasiswa kita yang tadi. File ini tidak diisi apa-sps oleh user karna difungsikan sebagai database untuk menyimpan hasil inputan saja.

## File main.py

File main.py, yaitu berisi import an dari package model dengan file daftar_nilai.py dengan variable (dn), dan import an dari package view dengan file input_nilai.py variablenya (nn). Dan ini merupakan tampilan menu nya :

## Source Code
![carbon(14)](https://user-images.githubusercontent.com/115929351/212524112-f399cf64-2c71-44f6-9744-8ee53c04a42b.png)

## MyEnv

Dan satu lagi, ada myenv ini bukan merupakan package tetapi hanya untuk membuat lingkungan virtual dari python, agar tidak mengganggu project lainnya, dan cara menjalankannya yaitu, source myenv/bin/activate.

## Output Program Tabel Daftar Nilai Mahasiswa

1. Tampilan Menu Pilihan Mahasiswa
![tmpiln](https://user-images.githubusercontent.com/115929351/212524257-a12b179c-a1e5-46fc-831e-6e1c823fea12.png)

2. Tampilan Tambah Data Mahasiswa
![tambah@](https://user-images.githubusercontent.com/115929351/212524272-2a0bf423-1b0d-410a-9be4-1f0720189403.png)

3. Tampilan Ubah Data Mahasiswa
![image](https://user-images.githubusercontent.com/115929351/212524428-8df18fa6-e9ea-4dd2-a030-71dd5f0c0c70.png)

4. Tampilan Cari Data Mahasiswa
![cari@](https://user-images.githubusercontent.com/115929351/212524313-c6c337a3-b4ff-4e92-902c-579228436263.png)

5. Tampilan Hapus Data Mahasiswa
![image](https://user-images.githubusercontent.com/115929351/212524415-ccbfc34b-6f87-4f8e-bca2-2a4fb954cdb6.png)

6. Tampilan Keluar Program Daftar Tabel Mahasiswa
![image](https://user-images.githubusercontent.com/115929351/212524400-63f3e2ed-4e19-4e13-9fb8-cf9021b40aa2.png)

Semoga bermanfaat man teman semuaaa....

## Thanks for Read Everyone
