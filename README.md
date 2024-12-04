# Sistem Penjualan Sederhana dengan OOP

Proyek ini merupakan implementasi dari konsep Pemrograman Berorientasi Objek (OOP) untuk sebuah sistem penjualan sederhana. Sistem ini terdiri dari dua jenis menu: **Makanan** dan **Minuman**, dengan berbagai ketentuan diskon berdasarkan total harga pembelian.

## Fitur Utama
1. **Kelas Menu**:
   - `Menu`: Kelas dasar untuk item menu.
   - `Makanan`: Subkelas untuk menu makanan.
   - `Minuman`: Subkelas untuk menu minuman.

2. **Kelas Penjualan**:
   - Mengelola pembelian, menghitung total harga, dan menerapkan diskon berdasarkan total pembelian.

3. **Diskon**:
   - Total < Rp50.000: Tidak ada diskon.
   - Total ≥ Rp50.000: Diskon 2.5%.
   - Total ≥ Rp75.000: Diskon 3%.
   - Total ≥ Rp100.000: Diskon 3.5%.

## Struktur File
- `menu.py`: Berisi definisi kelas `Menu`, `Makanan`, dan `Minuman`.
- `penjualan.py`: Berisi logika untuk kelas Penjualan.
- `main.py`: File utama untuk menjalankan program dan mengelola interaksi dengan pengguna.

## Contoh Kode
### menu.py
```python
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Makanan(Menu):
    def __init__(self, nama, harga):
        super().__init__(nama, harga)

class Minuman(Menu):
    def __init__(self, nama, harga):
        super().__init__(nama, harga)

### penjualan,py
