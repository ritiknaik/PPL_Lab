class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(Animals):
    def place(self):
        print("Live in Jungle")

class domestic_animals(Animals):
    def place(self):
        print("Live in areas habitated by human beings")


class carnivores(wild_animals):
    def prefer(self):
        print("Hunting")
    def food(self):
        print("Meat")
               
class herbivores(wild_animals):
    def food(self):
        print("Plant based")
    def prefer(self):
        print("Grasslands")

class omnivores(wild_animals):
    def food(self):
        print("Both plants and meat")
    def prefer(self):
        print("Almost any habitable place")

    
        
class tiger(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Orange and black stripes")
    def speciality(self):
        print("Stripes on body")
        
class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow")
    def speciality(self):
        print("King of the jungle")
        
class hyena(carnivores):
    def speak(self):
        print("similar to dogs")
    def colour(self):
        print("Grey")
    def speciality(self):
        print("Belongs to Canine family")




class deer(herbivores):
    def speak(self):
        print("dummyvalue")
    def colour(self):
        print("Brown")
    def speciality(self):
        print("Black and white stripes on the body")
        
class elephant(herbivores):
    def speak(self):
        print("dummyvalue")
    def colour(self):
        print("Grey")
    def speciality(self):
        print("It has a trunk")
        
class zebra(herbivores):
    def speak(self):
        print("mostly silent")
    def colour(self):
        print("Black and white")
    def speciality(self):
        print("Stripes on the body")

class monkey(omnivores):
    def speak(self):
        print("squeeks")
    def colour(self):
        print("brown hair")
    def speciality(self):
        print("Ancestor of humans")
        
class dog(domestic_animals):
    def speak(self):
        print("bark")
    def colour(self):
        print("brown, black, white, golden, etc")
    def speciality(self):
        print("Man's best friend")
        
class cat(domestic_animals):
    def speak(self):
        print("meow")
    def colour(self):
        print("Grey,brown, black, white, etc")
    def speciality(self):
        print("Common pet animal")
        
class cow(domestic_animals):
    def speak(self):
        print("moo")
    def colour(self):
        print("white, brown,etc")
    def speciality(self):
        print("Worshipped by Hindus")
        
class goat(domestic_animals):
    def speak(self):
        print("dummyvalue")
    def colour(self):
        print("black, brown, white. etc")
    def speciality(self):
        print("Has variety of breeds")

p1=Animals(4, 3)


Sherkhan = tiger()
Sherkhan.speak()
Sherkhan.speciality()
Sherkhan.place()
Sherkhan.colour()

print("Sherkhan has",Sherkhan.eyes,"eyes")
print("Sherkhan has", Sherkhan.legs,"legs")

Rodger = dog()
Rodger.speak()
Rodger.speciality()
Rodger.place()
Rodger.colour()

print(Rodger.eyes)
print(Rodger.legs)
