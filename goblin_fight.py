# # This is a procedural appraoch to a text based rpg game
# The hero is a fighting the goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Go get the os module from python
import os
import random
# os.system() will take any linux command
# and if python can run it, it will

print        """        
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

# Get the hero name from the player

print """
    1: Legolas
    2: Aragon
    3: Gimbly
    4: Frodo
"""
legolas = """
                   .;;,.
                  ; '" ;\ \//
                 \|a (a|7 \//
                 j| ..  | ||/
                //'.--.')\-,/
              .-||- '' ||/  `-.
             ;  | \ |/ |/ L.  ,|
             f\ |\| Y  || \ '._\
            j | \|     (| |   | |
           |  L_\         L.__: |
            \(  '-.,-,    |   ; |
             |'-.'.L_rr>  f--f  |
.-=,,______,--------- J-. ;  ;__ 
   ``"-,__   |  |      h  |  f  '--.__
       `--;;--,_       h  f-j   |   __;==-.
            / `-''-,,__J,'  \_..--:'-'     '
            | |    `' --L7//'-'`|
            | ,     ||  h    |  (
            | ;     | \ J    j   |
            | L__   | |  L_.'    |
            |   |'-.| L.'h  |  : |
            |;  \     |  J ; : : |
            | :  (    \  'L| : : |
            | ;   \'.--|    \  : |
            | | : \    \-, /`\ : |
            L-'-;__\   \\ '  | | |
                    ;   \\   |'L_j
                    _>  _|   |
                   <___/ /-  \
                        /    /
                        '---'
"""

hero_name = raw_input("Who will you be in this fellowship? ")

def fight():
    print "Welcome, %s. Thou art brave!" % hero_name
    # declare some variables
    # These variables are in the function scope
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    # run the game as long as BOTH characters have health > 0
    while hero_health > 0 and goblin_health > 0:
        message = """You have %d health and %d power.
        The goblin has %d health and %d power.
        What do you want to do?
        1. fight goblin
        2. do a little dance
        3. flee""" 
        print message % (hero_health, hero_power,goblin_health,goblin_power)
        # Get the user's choice
        user_input = raw_input("> ")

        if user_input == "1":
            # The hero has decided to attack!
            # subtract goblins health by hero power
            goblin_health -= hero_power
            print "You have done %d damage to the goblin!" % hero_power
        elif user_input == "2":
            hero_health += 10
            print """The goblin stares at you in disbelief of your stupidity. 
            His jaw drops as your wounds heal."""
            print "Your health is now %d" % hero_health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            # the break statement will end the loop IMMEDIATELY!!
            break
        else:
            # user entered something that we didnt offer
            print "Thou fool. Thou hast stumbledith (invalid input)"
        
        # Now, it's the goblin's turn
        # unless he just died from the hero attack
        if goblin_health > 0:
            hero_health -= goblin_power
            print "The goblin hits you for %d damage" % random.randint(1,10)
            if hero_health <= 0:
                print "Thou hast been slain."
        else:
            os.system ("say Hooray. Thou hast killed the goblin!")
        if hero_health < 5:
            print "%s has gone into a rage as death appraoches. Power increased!" % hero_name
            hero_power += 5
        raw_input("Hit enter to conntinue")
        os.system("clear")

# ANYIME you have ()
# print hero_health
fight()
