from menu import Makanan, Minuman  # Import dari file menu.py
from penjualan import Penjualan   # Import dari file penjualan.py

def format_harga_rupiah(harga):
    """Format harga menjadi Rupiah dengan separator ribuan (misal: Rp50.000)"""
    return f"Rp{harga:,.0f}".replace(",", ".")

def urutkan_menu(daftar_menu):
    """Mengatur ulang nomor urut daftar menu agar berurutan dari 1"""
    return {index + 1: menu for index, menu in enumerate(daftar_menu.values())}

def tampilkan_menu(daftar_menu):
    print("\n--- Daftar Menu ---")
    for nomor, menu in daftar_menu.items():
        print(f"{nomor}. {menu.nama} - {format_harga_rupiah(menu.harga)}")

def kelola_menu(daftar_menu):
    """Fungsi untuk mengelola daftar menu (tambah, hapus, ubah, kembali)"""
    while True:
        print("\n--- Kelola Menu ---")
        print("1. Tambah Menu Baru")
        print("2. Hapus Menu")
        print("3. Ubah Menu")
        print("4. Kembali ke Menu Utama")
        try:
            pilihan = int(input("Pilih opsi (1-4): "))
            if pilihan == 1:
                # Tambah menu baru
                jenis = input("Jenis menu (Makanan/Minuman): ").strip().capitalize()
                nama = input("Masukkan nama menu baru: ").strip()
                harga = int(input("Masukkan harga menu baru: "))
                if jenis == "Makanan":
                    menu_baru = Makanan(nama, harga)
                elif jenis == "Minuman":
                    menu_baru = Minuman(nama, harga)
                else:
                    print("Jenis menu tidak valid. Pilih Makanan atau Minuman.")
                    continue
                daftar_menu[max(daftar_menu.keys(), default=0) + 1] = menu_baru
                print(f"Menu baru {menu_baru.nama} dengan harga {format_harga_rupiah(menu_baru.harga)} berhasil ditambahkan.")

            elif pilihan == 2:
                # Hapus menu
                if not daftar_menu:
                    print("Tidak ada menu yang tersedia untuk dihapus.")
                    continue
                print("\n--- Daftar Menu ---")
                for nomor, menu in daftar_menu.items():
                    print(f"{nomor}. {menu.nama} - {format_harga_rupiah(menu.harga)}")
                nomor_hapus = int(input("Masukkan nomor menu yang ingin dihapus: "))
                if nomor_hapus in daftar_menu:
                    menu_dihapus = daftar_menu.pop(nomor_hapus)
                    print(f"Menu {menu_dihapus.nama} berhasil dihapus.")
                    daftar_menu = urutkan_menu(daftar_menu)  # Urutkan ulang nomor menu
                else:
                    print("Nomor menu tidak valid.")

            elif pilihan == 3:
                # Ubah menu
                if not daftar_menu:
                    print("Tidak ada menu yang tersedia untuk diubah.")
                    continue
                print("\n--- Daftar Menu ---")
                for nomor, menu in daftar_menu.items():
                    print(f"{nomor}. {menu.nama} - {format_harga_rupiah(menu.harga)}")
                nomor_ubah = int(input("Masukkan nomor menu yang ingin diubah: "))
                if nomor_ubah in daftar_menu:
                    menu = daftar_menu[nomor_ubah]
                    print(f"Menu terpilih: {menu.nama} - {format_harga_rupiah(menu.harga)}")
                    nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ").strip()
                    harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ").strip()
                    if nama_baru:
                        menu.nama = nama_baru
                    if harga_baru:
                        try:
                            menu.harga = int(harga_baru)
                        except ValueError:
                            print("Harga baru tidak valid. Tidak ada perubahan pada harga.")
                    print(f"Menu berhasil diubah menjadi {menu.nama} - {format_harga_rupiah(menu.harga)}.")
                else:
                    print("Nomor menu tidak valid.")

            elif pilihan == 4:
                # Kembali ke menu utama
                print("Kembali ke Menu Utama.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-4.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    return daftar_menu

def urutkan_menu(daftar_menu):
    """Mengatur ulang nomor urut daftar menu agar berurutan dari 1"""
    return {index + 1: menu for index, menu in enumerate(daftar_menu.values())}

def format_harga_rupiah(harga):
    """Format harga menjadi Rupiah dengan separator ribuan (misal: Rp50.000)"""
    return f"Rp{harga:,.0f}".replace(",", ".")


def lakukan_pembelian(daftar_menu, penjualan):
    while True:
        tampilkan_menu(daftar_menu)
        try:
            pilihan = int(input(f"Pilih menu (1-{len(daftar_menu)} atau 0 untuk selesai): "))
            if pilihan == 0:
                penjualan.checkout()
                break
            elif pilihan in daftar_menu:
                jumlah = int(input(f"Masukkan jumlah untuk {daftar_menu[pilihan].nama}: "))
                penjualan.tambah_item(daftar_menu[pilihan], jumlah)
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def main():
    daftar_menu = {
        1: Makanan("Grilled Wagyu Steak", 1000000),
        2: Makanan("Lobster Bisque", 500000),
        3: Makanan("Seared Duck Breast", 350000),
        4: Makanan("Pumpkin Truffle Soup", 200000),
        5: Makanan("Caesar Salad Deluxe", 150000),
        6: Makanan("Truffle Mushroom Risotto", 180000),
        7: Minuman("Blueberry Mint Fizz", 50000),
        8: Minuman("Passionfruit Mojito", 52000),
        9: Minuman("Fine Wines and Champagne", 800000),
        10: Minuman("Artisan Coffee and Tea", 40000),
        11: Minuman("Chocolate Fondant", 250000),
        12: Minuman("Matcha Opera Cake", 400000)
    }

    penjualan = Penjualan()

    while True:
        print("\n--- Welcome To AL Black ---")
        print("\n--- Menu Utama ---")
        print("1. Tampilkan Menu")
        print("2. Kelola Menu")
        print("3. Lakukan Pembelian")
        print("4. Keluar")
        try:
            pilihan = int(input("Pilih opsi (1-4): "))
            if pilihan == 1:
                tampilkan_menu(daftar_menu)
            elif pilihan == 2:
                daftar_menu = kelola_menu(daftar_menu)
            elif pilihan == 3:
                lakukan_pembelian(daftar_menu, penjualan)
            elif pilihan == 4:
                print("Terima kasih telah menggunakan aplikasi.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

# Jalankan program
if __name__ == "__main__":
    main()
