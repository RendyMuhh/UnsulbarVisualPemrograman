class Hero:
  def __init__(self, herotype, keunikan):
    self.herotype = herotype
    self.keunikan = keunikan
    
class Hero_strategi(Hero):
  pass

petarung = Hero("Balmond", "Kuat")
magic = Hero_strategi("Cecilion", "Sihir")

print(petarung.herotype, petarung.keunikan)
print(magic.herotype)
