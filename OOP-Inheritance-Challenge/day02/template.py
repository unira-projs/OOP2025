class Kendaraan:
    def __init__(self, merk, kecepatan_maksimal):
        self.merk = merk
        self.kecepatan_maksimal = kecepatan_maksimal

    def berjalan(self):
        return f"{self.merk} sedang berjalan dengan kecepatan {self.kecepatan_maksimal} km/jam."
        
class Mobil(Kendaraan):
    def berjalan(self):
        return f"Mobil {self.merk} melaju dengan kecepatan maksimal {self.kecepatan_maksimal} km/jam."

class Motor(Kendaraan):
    def berjalan(self):
        return f"Motor {self.merk} meluncur dengan kecepatan maksimal {self.kecepatan_maksimal} km/jam."

if __name__ == "__main__":
    mobil1 = Mobil("Porsche 911 GT2 RS", 340)
    motor1 = Motor("Kawasaki Ninja ZX-14R", 299)

    print(mobil1.berjalan())
    print(motor1.berjalan())
