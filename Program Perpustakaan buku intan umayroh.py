# Inisialisasi daftar buku
daftar_buku = []

# Fungsi untuk menambahkan buku
def tambah_buku():
    while True:
        print("\n=== Tambah Buku ===")
        judul = input("Masukkan judul buku: ").strip()
        penulis = input("Masukkan nama penulis: ").strip()
        tahun = input("Masukkan tahun penerbit: ").strip()
        
        # Validasi input
        if judul and penulis and tahun:
            buku_baru = {
                "judul": judul,
                "penulis": penulis,
                "tahun": tahun
            }
            daftar_buku.append(buku_baru)
            print("Buku berhasil ditambahkan!")
        else:
            print("Data tidak lengkap. Buku tidak ditambahkan.")
        
        # Tanyakan apakah ingin menambahkan buku lagi
        tambah_lagi = input("\nTambahkan buku lagi? (y/n): ").strip().lower()
        if tambah_lagi != 'y':
            break

# Fungsi untuk menampilkan daftar buku
def tampilkan_daftar_buku():
    print("\n=== Daftar Buku ===")
    if not daftar_buku:
        print("Daftar buku kosong.")
    else:
        for idx, buku in enumerate(daftar_buku, start=1):
            print(f"{idx}. Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
    print("")  # Tambahkan baris kosong di akhir

# Fungsi untuk mencari buku berdasarkan judul
def cari_berdasarkan_judul():
    judul_cari = input("Masukkan judul buku yang ingin dicari: ").strip().lower()
    ditemukan = False
    for buku in daftar_buku:
        if judul_cari in buku['judul'].lower():
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
            ditemukan = True
    if not ditemukan:
        print(f"Buku dengan judul '{judul_cari}' tidak ditemukan.")

# Fungsi untuk mencari buku berdasarkan nama penulis
def cari_berdasarkan_penulis():
    penulis_cari = input("Masukkan nama penulis yang ingin dicari: ").strip().lower()
    ditemukan = False
    for buku in daftar_buku:
        if penulis_cari in buku['penulis'].lower():
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
            ditemukan = True
    if not ditemukan:
        print(f"Buku yang ditulis oleh '{penulis_cari}' tidak ditemukan.")

# Fungsi untuk mencari buku berdasarkan tahun penerbit
def cari_berdasarkan_tahun():
    tahun_cari = input("Masukkan tahun penerbit yang ingin dicari: ").strip()
    ditemukan = False
    for buku in daftar_buku:
        if tahun_cari == buku['tahun']:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
            ditemukan = True
    if not ditemukan:
        print(f"Buku yang diterbitkan pada tahun '{tahun_cari}' tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    print("=== Program Perpustakaan Buku ===")
    while True:
        print("\nSilakan pilih operasi yang ingin dilakukan:")
        print("1. Tambahkan buku")
        print("2. Tampilkan daftar buku")
        print("3. Cari buku")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ").strip()
        
        if pilihan == '1':
            tambah_buku()
        elif pilihan == '2':
            tampilkan_daftar_buku()
        elif pilihan == '3':
            print("\nPilih kriteria pencarian:")
            print("a. Berdasarkan judul buku")
            print("b. Berdasarkan nama penulis")
            print("c. Berdasarkan tahun penerbit")
            
            kriteria = input("Masukkan pilihan (a/b/c): ").strip().lower()
            
            if kriteria == 'a':
                cari_berdasarkan_judul()
            elif kriteria == 'b':
                cari_berdasarkan_penulis()
            elif kriteria == 'c':
                cari_berdasarkan_tahun()
            else:
                print("Pilihan tidak valid.")
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program perpustakaan buku!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
