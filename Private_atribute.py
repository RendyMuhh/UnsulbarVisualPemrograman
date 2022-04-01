#Nama : Muhammad Rendy
#Nim  : D0219519

class data():
    __barang = 5 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barang(self,harga_barang):
       hasil = self.__barang * harga_barang
       return hasil
 
produk = data("Buku Pemrograman OPP")
print(produk.harga_barang(80))
