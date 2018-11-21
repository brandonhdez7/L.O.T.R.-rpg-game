class Hero(object):
    #What does every class?
    def __init__(self,name,power = 5, weapon = {"name": "", "power": 0}):
        self.name = name
        self.health = 10
        self.power = power + weapon["power"]
        self.weapon = {"name": weapon["name"], "power": weapon["power"]}
     
    def cheer_hero(self):
        print "welcome, brave %s" % (self.name)
    def take_damage(self,ammount_of_damage):
        self.health -= ammount_of_damage
    def is_alive(self):
        return self.health > 0

        



