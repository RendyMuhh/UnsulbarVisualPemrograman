class data_mhs():
    jumlah_mhs = 0
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
        data_mhs.jumlah_mhs +=1

        
rendy = data_mhs("Muhammad Rendy")
iska = data_mhs("Yiska Astuti")
 
print(data_mhs.jumlah_mhs)

