from datetime import datetime

data_fasilitas = [
    ("1", "Proyektor", "Baik"),
    ("2", "Kipas angin", "Rusak"),
    ("3", "AC", "Baik"),
    ("4", "Papan tulis", "Baik"),
    ("5", "Lampu", "Rusak")
]

data_user = {
    "admin": "pipupipu",
    "user": "lalalala"
}

def tampilkan_fasilitas():
    print("\n===== DAFTAR FASILITAS =====")

    if len(data_fasilitas) == 0:
        print("Fasilitas belum tersedia")
    else:
        for data in data_fasilitas:
            print(
            "Nomor:", data[0],
            "| Nama Fasilitas:", data[1],
            "| Kondisi:", data[2]
        )

def tambahkan_fasilitas():
    print("/n===== TAMBAH FASILITAS =====")

    nomor = input("Masukkan nomor fasilitas: ")
    nama = input("Masukkan nama fasilitas: ")
    kondisi = input("Masukkan kondisi fasilitas (Baik/Rusak): ")

    if nama == "":
        print("Nama fasilitas tidak boleh kosong!")
        return

    elif kondisi == "":
        print("Kondisi fasilitas tidak boleh kosong!")
        return

    data_fasilitas_baru = (nomor, nama, kondisi)

    data_fasilitas.append(data_fasilitas_baru)
    print("Fasilitas berhasil ditambahkan!")

def ubah_fasilitas():
    print("/n===== UBAH FASILITAS =====")

    nomor = input("Masukkan nomor fasilitas yang ingin diubah: ")

    for i in range(len(data_fasilitas)):

        cari_nomor = input("Masukkan nomor fasilitas yang ingin diubah: ")

    for i in range(len(data_fasilitas)):
            if data_fasilitas[i][0] == cari_nomor:
                nama_baru = input("Masukkan nama fasilitas baru: ")
                kondisi_baru = input("Masukkan kondisi fasilitas baru (Baik/Rusak): ")

            if nama_baru == "":
                print("Nama fasilitas tidak boleh kosong!")
                return

            if kondisi_baru == "":
                print("Kondisi fasilitas tidak boleh kosong!")
                return

            data_fasilitas[i] = (nomor, nama_baru, kondisi_baru)
            print("Fasilitas berhasil diubah!")
            return

            print("Fasilitas berhasil diubah!")
            return

    print("Nomor fasilitas tidak ditemukan!")

def hapus_fasilitas():
    print("\n===== HAPUS FASILITAS =====")

    cari_nomor = input("Masukkan nomor fasilitas yang ingin dihapus: ")


    for i in range(len(data_fasilitas)):
        if data_fasilitas[i][0] == cari_nomor:

            del data_fasilitas[i]
            print("Fasilitas berhasil dihapus!")
            return

    print("Nomor fasilitas tidak ditemukan!")

def menu_admin():
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Tampilkan fasilitas")
        print("2. Tambah fasilitas")
        print("3. Ubah fasilitas")
        print("4. Hapus fasilitas")
        print("5. Logout")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tampilkan_fasilitas()
        elif pilihan == "2":
            tambahkan_fasilitas()
        elif pilihan == "3":
            ubah_fasilitas()
        elif pilihan == "4":
            hapus_fasilitas()
        elif pilihan == "5":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan menu tidak tersedia!")

def menu_user():
    while True:
        print("\n===== MENU USER =====")
        print("1. Tampilkan fasilitas")
        print("2. Logout")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tampilkan_fasilitas()
        elif pilihan == "2":
            print("Logout berhasil!")
            break

        else:
            print("Pilihan menu tidak tersedia!")

while True:
    print("\n===== LOGIN =====")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_user and data_user[username] == password:
        print("Login berhasil!")

        if username == "admin":
            menu_admin()
        else:
            menu_user()
    else:
        print("Username atau password tidak ditemukan!")