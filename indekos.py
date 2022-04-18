from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah):
        super().__init__("Indekos", 1, 1, luas_tanah)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos.\n Nama Pemilik: " + self.get_nama_pemilik() + "\nNama Penghuni: " + self.get_nama_penghuni() + "\nLuas Tanah: " + str(self.get_luas_tanah()) + "m2" + "\nDokumen: " + self.get_dokumen()