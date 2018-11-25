import os
from Hero import Hero
from Goblin import Goblin
from Orcs import Orc
from random import randint
from time import sleep


weapons = [{"name": "sword", "power": 7},{"name": "bow arrow", "power": 6}, {"name": "axe", "power": 8}]





print"""    
                 ___ . .  _                                                                                             
        "T$$$P"   |  |_| |_                                                                                             
         :$$$     |  | | |_                                                                                             
         :$$$                                                      "T$$$$$$$b.                                          
         :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
         $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
         :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
         :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
         $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
         $$$   Tb.       ,dP  $$""'Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$;
         $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $...$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP 
         $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $""'$ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P  
         $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.                                       
        d$$$$$$$$$$P                                                        `T$b.
"""
sleep(2)
print """                 
                             Three Rings for the Elvin-Kings under the sky.
                            Seven for the DwarfLords in their halls of stone.
                          Nine for the Mortal Men doomed to die.
                            One for the Dark Lord on his dark throne.
                              In the Land of Mordor where the Shadow Lies.
                
                            One Ring to rule them all,One Ring to find them,
                           One Ring to bring them all and in the Darkness
                             Bind Them
                              In the Land of Mordor where the Shadows Lie.
                        """

os.system("""                 
                say             Three Rings for the Elvin-Kings under the sky.
                say            Seven for the DwarfLords in their halls of stone.
                say          Nine for the Mortal Men doomed to die.
                say            One for the Dark Lord on his dark throne.
                say              In the Land of Mordor where the Shadow Lies.
                
                say            One Ring to rule them all,One Ring to find them,
                say          One Ring to bring them all and in the Darkness
                say            Bind Them
                say              In the Land of Mordor where the Shadows Lie.
                        """)

print """
    
    Legolas
    Frodo
    Aragon
    Gimbly
    Gandolf   
""" 
hero_name = raw_input("Who will you be in this fellowship? ")   
#there is only one hero
theHero = Hero(hero_name, 4)
theHero.cheer_hero()

while(theHero.is_alive()):
    #while there are many monsters
    randMonster = randint(1,2)
    if randMonster == 1:
        monster = Goblin()
    else:
        monster = Orc()

    print "you have encountered the terrifying %s" % monster.name
    
    while(theHero.is_alive() and monster.is_alive()):
    
        print """

                        _               _,-----------._        ___
                        (_,.-       _,-'_,-----------._`-._    _)_)
                            |      ,'_,-'  ___________  `-._`.
                                ,','  _,-'___________`-._  `.`.
                            ,','  ,'_,-'     .     `-._`.  `.`.
                            /,'  ,','        >|<        `.`.  `.'
                            //  ,','      ><  ,^.  ><      `.`.  ''
                            //  /,'      ><   / | \   ><      `.\  ''
                        //  //      ><    \/\^/\/    ><      ''  ''
                        ;;  ;;              `---'              ::  ::
                        ||  ||              (____              ||  ||
                        _||__||_            ,'----.            _||__||_
                        (o.____.o)____        `---'        ____(o.____.o)
                        |    | /,--.)                   (,--.\ |    |
                        |    |((  -`___               ___`   ))|    |
                        |    | |\,'',  `.           .'  .``.// |    |
                        |    |  // (___,'.         .'.___) \|  |    |
                        /|    | ;;))  ____) .     . (____  ((\| |    |;
                        \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                        |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                        |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                        |    |,\  /,                     ,\  /,|    |
                        |    ||: : )          .          ( : :||    |
                        /|    |:; |/  .      ./|\,      ,  \| :;|    |;
                        \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                        |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                        |   `..   ,' `'       '       `  `.   ,.'   |
                        |    ||  :                         :  ||    |
                        |    ||  |                         |  ||    |
                        |    ||  |                         |  ||    |
                        |    |'  |            _            |  `|    |
                        |    |   |          '|))           |   |    |
                        ;____:   `._        `'           _,'   ;____:
                        [______]     \___________________/     [______]
                        |______|_______________________________|______|
                """     

        print"""        
                        The Doors of Durin, also known as the West-gate
                        the West-door of Moria, or Elven Door, were built into the Walls of Moria in the dark cliffs of the Silvertine 
                        and formed the western entrance to the great Dwarven city of Khazad-dum.
                    """
        sleep(3)



        message = """You have %d health and %d power.
        The %s has %d health and %d power.
        What do you want to do?
        1. fight %s
        2. change weapon
        3. Retreat!!""" 
        print message % (theHero.health, theHero.power, monster.name, monster.health, monster.power, monster.name)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack!
            # subtract monsters health by hero power
            monster.take_damage(theHero.power)
            print "You have done %d damage to the monster!" % theHero.power
        elif user_input == "2":
            weapon_number = 0
            for weapon in weapons: 
                weapon_number += 1
                print "%d. %s" %  (weapon_number, weapon["name"])
                
            user_input = int(raw_input("choose weapon? "))

            theHero.weapon = weapons[user_input - 1]
            theHero.power += weapons[user_input - 1]["power"]

            

            
            
            print "Your power is now %d" % theHero.power
        elif user_input == "3":
            print "Retreat!! Call for elves help %s" % theHero.name
            # the break statement will end the loop IMMEDIATELY!!
            break
        else:
            # user entered something that we didnt offer
            print "Thou fool. Thou hast stumbledith (invalid input)"
        
        # Now, it's the monster's turn
        # unless he just died from the hero attack
        if monster.is_alive():
            theHero.take_damage(monster.power)
            print "The monster hits you for %d damage" % (monster.power)
            if not theHero.is_alive():
                print "Thou hast been slain."
            
        else:
            os.system ("say Hooray. Thou hast killed the monster!")
            break
        if theHero.health < 5:
            print "%s has gone into a rage as death appraoches. Power increased!" % theHero.name
            theHero.power += 5
        raw_input("Hit enter to conntinue")
        os.system("clear") 

    
