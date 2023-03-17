class Mobil :
    def _init_(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("Civic", "Putih")
mobilA.info()
