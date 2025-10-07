class Binatang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mamalia(Binatang):
    def __init__(self, nama, umur, peliharaan):
        super().__init__(nama, umur)
        self.peliharaan = peliharaan

    def deskripsikan(self):
        status = "Ya" if self.peliharaan else "Tidak"
        return f"Nama: {self.nama}, Umur: {self.umur} tahun, Mamalia peliharaan: {status}"

if __name__ == "__main__":
    mamalia1 = Mamalia("Anjing", 4, True)
    mamalia2 = Mamalia("Paus", 25, False)

    print(mamalia1.deskripsikan())
    print(mamalia2.deskripsikan())
