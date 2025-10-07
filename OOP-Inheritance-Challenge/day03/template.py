class Pegawai:
    def __init__(self, nama, gaji_dasar):
        self.nama = nama
        self.gaji_dasar = gaji_dasar

    def hitung_gaji(self):
        return self.gaji_dasar

class Manager(Pegawai):
    def __init__(self, nama, gaji_dasar, tunjangan):
        super().__init__(nama, gaji_dasar)
        self.tunjangan = tunjangan
        
    def hitung_gaji(self):
        return super().hitung_gaji() + self.tunjangan    

if __name__ == "__main__":
    pegawai1 = Pegawai("Asep", 5000000)
    manager1 = Manager("Nizam", 7000000, 3000000)

    print(f"Gaji {pegawai1.nama}: Rp{pegawai1.hitung_gaji()}")
    print(f"Gaji {manager1.nama}: Rp{manager1.hitung_gaji()}")
