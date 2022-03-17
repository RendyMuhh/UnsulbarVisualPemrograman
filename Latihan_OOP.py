class Hewan:
    def __init__(self, inputNama, inputJenis_mkn, inputHabitat):
        self.nama = inputNama
        self.jenis_mkn = inputJenis_mkn
        self.habitat = inputHabitat

animal_1 = Hewan("Hiu","Karnivora","air")
animal_2 = Hewan("Sapi","Herbivora","Darat")
animal_3 = Hewan("Elang","Karnivora","Darat")

print(animal_1.nama)
    
