from menu import Makanan, Minuman  # Import dari file menu.py
from penjualan import Penjualan   # Import dari file penjualan.py

def format_harga_rupiah(harga):
    """Format harga menjadi Rupiah dengan separator ribuan (misal: Rp50.000)"""
    return f"Rp{harga:,.0f}".replace(",", ".")

def urutkan_menu(daftar_menu):
    """Mengatur ulang nomor urut daftar menu agar berurutan dari 1"""
    daftar_menu_urut = {index + 1: menu for index, menu in enumerate(daftar_menu.values())}
    return daftar_menu_urut

def main():
    # Daftar menu awal
    daftar_menu = {
        1: Makanan("Nasi Goreng", 25000),
        2: Makanan("Ayam Bakar", 30000),
        3: Makanan("Rendang", 35000),
        4: Makanan("Soto Ayam", 20000),
        5: Makanan("Bakso", 15000),
        6: Makanan("Mie Goreng", 18000),
        7: Minuman("Es Teh", 5000),
        8: Minuman("Kopi", 15000),
        9: Minuman("Es Jeruk", 8000),
        10: Minuman("Jus Alpukat", 20000),
        11: Minuman("Jus Mangga", 25000),
        12: Minuman("Air Mineral", 4000)
    }

    penjualan = Penjualan()

    while True:
        # Menampilkan menu utama
        print("\n--- Daftar Menu ---")
        for nomor, menu in daftar_menu.items():
            print(f"{nomor}. {menu.nama} - {format_harga_rupiah(menu.harga)}")

        print("13. Selesai dan Checkout")
        print("14. Update Pesanan")
        print("15. Hapus Pesanan")
        print("16. Edit Menu")
        print("-----------------------")

        try:
            # Input pilihan user
            pilihan = int(input("Pilih menu (1-16): "))
            if pilihan == 13:
                break
            elif pilihan == 14:
                penjualan.update_pesanan()
            elif pilihan == 15:
                penjualan.hapus_pesanan()
            elif pilihan == 16:
                daftar_menu = edit_menu(daftar_menu)
            elif pilihan in daftar_menu:
                jumlah = int(input(f"Masukkan jumlah untuk {daftar_menu[pilihan].nama}: "))
                penjualan.tambah_item(daftar_menu[pilihan], jumlah)
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    # Checkout
    penjualan.checkout()

def edit_menu(daftar_menu):
    """Fungsi untuk mengedit daftar menu"""
    print("\n--- Edit Menu ---")
    print("1. Tambah Menu Baru")
    print("2. Hapus Menu")
    try:
        pilihan = int(input("Pilih opsi (1-2): "))
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
                return daftar_menu
            daftar_menu[max(daftar_menu.keys(), default=0) + 1] = menu_baru
            print(f"Menu baru {menu_baru.nama} dengan harga {format_harga_rupiah(menu_baru.harga)} berhasil ditambahkan.")
        elif pilihan == 2:
            # Hapus menu
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
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
    return daftar_menu

# Jalankan program
if __name__ == "__main__":
    main()
