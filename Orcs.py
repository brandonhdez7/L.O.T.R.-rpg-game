from random import randint

class Orc(object):
    #What does every class?
    def __init__(self):
        randomPower = randint(2,10)
        self.name = "Orc"
        self.health = 10
        self.power = randomPower
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage
    def is_alive(self):
        return self.health > 0
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds."