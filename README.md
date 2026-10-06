# Minpro-2-DDP-FasilitasKampus

Nama : Ivanka Putri Meisyarah
NIM : 2609116066
Kelas : B

1. Data fasilitas: menyimpan nomor, nama, dan kondisi fasilitas menggunakan list dan tuple.
2. Data login: menyimpan username dan password menggunakan dictionary.
3. Function: digunakan untuk menjalankan fitur tambah, tampil, ubah, dan hapus fasilitas.
4. Login: pengguna harus memasukkan username dan password sebelum masuk ke menu.
5. Admin: memiliki akses penuh untuk menambah, melihat, mengubah, dan menghapus data.
6. User: hanya memiliki akses untuk melihat data fasilitas.
7. Validasi input: mengecek data agar tidak kosong, nomor tidak sama, dan pilihan menu tersedia.
8. Library datetime: digunakan untuk menampilkan waktu saat berhasil login.

<img width="1920" height="1080" alt="fc" src="https://github.com/user-attachments/assets/7295ef14-7d92-436d-9cf9-74dc60e619fd" />
Memulai Program: Program dimulai dengan menampilkan layar utama untuk proses login pengguna.  
​Memasukkan Data Login: Pengguna diminta untuk memasukkan username dan password.  
​Verifikasi Akun Admin:
​Apabila username dan password yang dimasukkan sesuai dengan akun administrator, sistem akan menampilkan jam login dan mengarahkan pengguna ke Menu Admin.  
​Apabila password salah, sistem akan menampilkan notifikasi kesalahan dan mengembalikan pengguna ke halaman login.  
​Verifikasi Akun User:
​Apabila username dan password yang dimasukkan sesuai dengan akun pengguna biasa, sistem akan menampilkan jam login dan mengarahkan pengguna ke Menu User.  
​Apabila password salah, sistem akan menampilkan pemberitahuan bahwa kata sandi tidak sesuai.  
​Penanganan Akun Tidak Terdaftar: Apabila username yang diinputkan tidak terdaftar dalam sistem, akan muncul pesan peringatan dan pengguna diminta melakukan login kembali.  
​Fungsi Menu Admin: Pada menu ini, administrator memiliki akses penuh untuk menambah, melihat, memperbarui, serta menghapus data fasilitas.
​Fungsi Menu User: Pada menu ini, pengguna biasa hanya dapat melihat daftar fasilitas yang tersedia.
​Keluar Sistem: Saat pengguna memilih opsi keluar (logout), sistem akan mengakhiri sesi dan menampilkan kembali layar login utama.

<img width="1920" height="1080" alt="opadmin" src="https://github.com/user-attachments/assets/7aed8c34-6e00-440a-9901-64e62dc9b306" />
<img width="1920" height="1080" alt="opuser" src="https://github.com/user-attachments/assets/2550bad7-710f-4e3a-aa23-2b4544a94215" />

Halaman login: menampilkan username dan password yang harus dimasukkan pengguna.
Login berhasil: menampilkan pesan berhasil dan waktu login.
Menu admin: menampilkan pilihan untuk menambah, melihat, mengubah, menghapus fasilitas, atau logout.
Menu user: menampilkan pilihan untuk melihat fasilitas atau logout.
Daftar fasilitas: menampilkan nomor, nama, dan kondisi setiap fasilitas.
Validasi: menampilkan pesan jika input kosong, nomor tidak ditemukan, nomor sudah digunakan, atau pilihan menu tidak tersedia.
Logout: menampilkan pesan bahwa logout berhasil dan kembali ke halaman login.
