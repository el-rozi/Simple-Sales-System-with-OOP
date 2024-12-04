class Penjualan:
    def __init__(self):
        self.keranjang = []  # List untuk menyimpan item yang dibeli

    def tambah_item(self, item, jumlah):
        # Menambahkan item ke keranjang belanja
        self.keranjang.append((item, jumlah))
        print(f"{jumlah} x {item.nama} ditambahkan ke keranjang.")

    def hitung_total(self):
        # Menghitung total harga sebelum diskon
        total = sum(item.harga * jumlah for item, jumlah in self.keranjang)
        return total

    def hitung_diskon(self, total):
        # Menghitung diskon berdasarkan total harga
        if total >= 100000:
            return total * 0.035
        elif total >= 75000:
            return total * 0.03
        elif total >= 50000:
            return total * 0.025
        else:
            return 0

    def format_harga_rupiah(self, harga):
        """Format harga menjadi Rupiah dengan separator ribuan (misal: Rp50.000)"""
        return f"Rp{harga:,.0f}".replace(",", ".")

    def update_pesanan(self):
        """Update jumlah pesanan untuk item yang sudah ada di keranjang"""
        if not self.keranjang:
            print("Keranjang kosong. Tidak ada yang bisa diupdate.")
            return

        print("\n--- Update Pesanan ---")
        for i, (item, jumlah) in enumerate(self.keranjang, 1):
            print(f"{i}. {item.nama} - {jumlah} pcs")
        try:
            pilihan = int(input("Pilih nomor pesanan yang ingin diupdate: "))
            if 1 <= pilihan <= len(self.keranjang):
                item, _ = self.keranjang[pilihan - 1]
                jumlah_baru = int(input(f"Masukkan jumlah baru untuk {item.nama}: "))
                self.keranjang[pilihan - 1] = (item, jumlah_baru)
                print(f"Pesanan {item.nama} berhasil diupdate menjadi {jumlah_baru} pcs.")
            else:
                print("Nomor pesanan tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    def hapus_pesanan(self):
        """Hapus item dari keranjang belanja"""
        if not self.keranjang:
            print("Keranjang kosong. Tidak ada yang bisa dihapus.")
            return

        print("\n--- Hapus Pesanan ---")
        for i, (item, jumlah) in enumerate(self.keranjang, 1):
            print(f"{i}. {item.nama} - {jumlah} pcs")
        try:
            pilihan = int(input("Pilih nomor pesanan yang ingin dihapus: "))
            if 1 <= pilihan <= len(self.keranjang):
                item, _ = self.keranjang.pop(pilihan - 1)
                print(f"Pesanan {item.nama} berhasil dihapus.")
            else:
                print("Nomor pesanan tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    def checkout(self):
        # Menampilkan total harga, diskon, dan total akhir setelah diskon
        total = self.hitung_total()
        diskon = self.hitung_diskon(total)
        total_akhir = total - diskon

        print("\n--- Ringkasan Pembelian ---")
        for item, jumlah in self.keranjang:
            print(f"{jumlah} x {item.nama} (@{self.format_harga_rupiah(item.harga)}) = {self.format_harga_rupiah(item.harga * jumlah)}")
        print(f"Total Harga: {self.format_harga_rupiah(total)}")
        print(f"Diskon: {self.format_harga_rupiah(diskon)}")
        print(f"Total Akhir: {self.format_harga_rupiah(total_akhir)}")
