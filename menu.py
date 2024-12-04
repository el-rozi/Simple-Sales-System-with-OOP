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
