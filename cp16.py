from functions import *
import variables as vars

def checkpoint_16():
    story("The passageway runs eastwards. Ahead of you, you can see that\na solid-looking door blocks the passage. You step up to investigate.")
    story("A sign above the door reads 'Boat House'. The door is firmly locked\nbut a small barred window allows you to look inside.")
    story("You can see a number of Skeleton-men working on building a boat of some sort.\nThey move in a series of quick, jerky actions, rather insect-like.")
    vars.decision_123 = story("Do you have a KEY clearly marked 'Boat House' that you wish to use?\nOtherwise, do you want to try breaking down the DOOR\nor returning to the RIVERbank to try another route?")
    if vars.decision_123 == "DOOR":
        story("There is no way you are going to charge the door down,\nas it is twelve centimetres of solid oak! You bruise your sword arm at the attempt.")
        change_stats(0, 1, "subtract")
        story("You can only get through the door\nif you have the Boat House key.")
        if "Boat House Key" in vars.equipment:
            story("You have this key.\nMore fool you for not using it straightaway.")
            vars.decision_124 = "KEY"
        else:
            story("You will have to return\nto the riverbank and try again.")
            vars.decision_123 = "RIVER"
    if vars.decision_123 == "RIVER":
        story("You return to the riverbank and decide to try\nthe door in the middle of the rockface.")
        vars.checkpoint = 13
        vars.decision_89 = "DOOR"
    if vars.decision_123 == "KEY":
        if "Boat House Key" in vars.equipment:
            vars.decision_124 = "KEY"
        else:
            vars.decision_123 = story("You do not have a key marked 'Boat House'. Will you try breaking the DOOR down\nor returning to the RIVERbank to try another route?")
            if vars.decision_123 == "DOOR":
                story("There is no way you are going to charge the door down,\nas it is twelve centimetres of solid oak! You bruise your sword arm at the attempt.")
                change_stats(0, 1, "subtract")
                story("You can only get through the door\nif you have the Boat House key.")
                if "Boat House Key" in vars.equipment:
                    story("You have this key.\nMore fool you for not using it straightaway.")
                    vars.decision_124 = "KEY"
                else:
                    story("You will have to return\nto the riverbank and try again.")
                    vars.decision_123 = "RIVER"
            if vars.decision_123 == "RIVER":
                story("You return to the riverbank and decide to try\nthe door in the middle of the rockface.")
                vars.checkpoint = 13
                vars.decision_89 = "DOOR"
    if vars.decision_124 == "KEY":
        story("The key fits the lock and opens the door. You find yourself in a large boathouse.\nVarious boats, in different stages of construction, are lying around.")
        story("Apart from the door behind you, there is another\nin the north wall. As you enter, the Skeletons stop their work\nand crane their bony necks around to look at you.")
        story("They pick up planks of wood and hammers\nand advance towards you. There are five of them.")
        vars.decision_125 = story("Do you:\nSmile nervously and BACK out of the door into the passage\nTELL them you've come about buying a boat\nTell them you're their new boss and ORDER them back to work\nor draw your SWORD and prepare for battle?")
        if vars.decision_125 == "BACK":
            story("You return to the riverbank and decide to try\nthe door in the middle of the rockface.")
            vars.checkpoint = 13
            vars.decision_89 = "DOOR"
        if vars.decision_125 == "TELL":
            story("Will they believe your story about buying a boat?\nSkeletons are pretty simple-minded, so roll one die.")
            vars.dice_num = randint(1, 6)
            if vars.dice_num < 4:
                story("They believe you, and they all go running through the door\nin the north wall, leaving you alone in the Boat House.")
                change_stats(2, 2)
                story("You're alone in the Boat House and have some time to search\nbefore the Skeletons will inevitably return.")
                vars.decision_126 = story("Will you search the DRAWERS in the room,\nor investigate the TOOLS before they come back?")
                story("As you begin to search you hear a noise\nfrom behind the door in the north wall.")
                if vars.decision_126 == "DRAWERS":
                    vars.skeletons = 322
                elif vars.decision_126 == "TOOLS":
                    vars.skeletons = 34
            elif vars.dice_num < 6:
                story("They're not sure. They send two of their members through the north door\nwhilst the other three watch you with their makeshift weapons.")
                story("You realize that the two Skeletons who have just run off\nwill soon return and expose your bluff. You must react quickly.")
                vars.decision_131 = story("Will you beat a hasty retreat through the DOOR behind you\nor draw your SWORD and lash out at the remaining Skeletons?")
                if vars.decision_131 == "DOOR":
                    story("You return to the riverbank and decide to\ntry the door in the middle of the rockface.")
                    vars.checkpoint = 15
                elif vars.decision_131 == "SWORD":
                    story("The battle commences. The Skeletons attack you one by one:")
                    vars.monster = [6, 5]
                    if fight("Skeleton A"):
                        vars.monster = [6, 6]
                        if fight("Skeleton B"):
                            vars.monster = [5, 5]
                            if fight("Skeleton C"):
                                vars.skeletons = 395
            else:
                story("They definitely don't believe you and keep on advancing.\nThe Skeletons advance and force you back to the door.")
                vars.skeletons = 140
        if vars.decision_125 == "ORDER":
            story("This is a rather unlikely story,\nconsidering that they see very few humans around.")
            story("Nevertheless, Skeletons are pretty dim - you knew this\nand that's why you tried the story. Roll one die.")
            vars.dice_num = randint(1, 6)
            if vars.dice_num < 3:
                story("They don't believe you and keep on advancing.")
                vars.skeletons = 140
        if vars.decision_125 == "SWORD":
            vars.skeletons = 140
        if vars.skeletons == 140:
            story("The leader approaches, with two behind, and the final two behind them.\nResolve this battle by first fighting the leader and then fighting the pairs:")
            vars.monster = [7, 5]
            if fight("Skeleton"):
                story("Both members of a pair will have a seperate attack on you\nin each Attack Round, but you will attack just once each turn.")
                story("Against the other, you will throw for your Attack Strength\nin the normal way, but you will not wound it if your attack strength is the greater.")
                story("You must just count this as though you have defended against its blow.\nOf course if its Attack Strength is greater, it has wounded you in the normal way.")
                """1st pair: Skeleton A = [6, 5]
                             Skeleton B = [6, 6]
                   2nd pair: Skeleton A = [5, 6]
                             Skeleton B = [5, 5]
                             make work"""
                vars.skeletons = 395
        if vars.skeletons == 395:
            story("You step over the bones on the floor\nto take a closer look at the Boat House.")
            story("You pick up and study a few of the tools scattered around:\nhammers, nails, chisels and the like, but they appear very ordinary.")
            story("You hear a banging sound coming from beyond the north door\nand have time for one further search before you must react.")
            vars.decision_132 = story("Do you look through the DRAWERS of the benches\naround the room or check the TOOLS more carefully?")
            if vars.decision_132 == "DRAWERS":
                vars.skeletons = 322
            elif vars.decision_132 == "TOOLS":
                vars.skeletons = 34
        if vars.skeletons == 322:
            story("The drawers are full of nails, tacks and miscellaneous bits and pieces.\nIn one drawer is a copper-coloured key, inscribed with the number 66 which looks interesting.")
            vars.equipment.append("Key 66")
            vars.decision_127 = story("If you wish to take this key, you must discard\none item of equipment you are carrying. Which will you discard?")
            print(vars.decision_127.title())
            print(vars.equipment)
            while vars.decision_127.title() not in vars.equipment:
                vars.decision_127 = story("You don't have that. Which piece of\nequipment will you choose from your pack?")
            vars.equipment.remove(vars.decision_127.title())
            story("The noise from the north gets louder.\nYou go to the north door to investigate.")
        if vars.skeletons == 34:
            story("Looking through the tools you come across a mallet\nwith a hardwood head and a chisel with a solid silver blade.")
            vars.decision_128 = story("You may keep either of these if you are prepared to forfeit\none of the items of equipment you are carrying. Are you?")
            if vars.decision_128 == "YES":
                vars.decision_129 = story("Which item do you wish to take - the MALLET or the CHISEL?")
                if vars.decision_129 == "MALLET":
                    vars.equipment.append("Mallet")
                elif vars.decision_129 == "CHISEL":
                    vars.equipment.append("Chisel")
                vars.decision_130 = story("Which item will you discard from your pack?")
                print(vars.decision_130.title())
                print(vars.equipment)
                while vars.decision_130.title() not in vars.equipment:
                    vars.decision_130 = story("You don't have that. Which piece of\nequipment will you choose from your pack?")
                vars.equipment.remove(vars.decision_130.title())
                story("The noise from the north gets louder.\nYou go to the north door to investigate.") 
        story("The door opens into a short corridor about fifteen metres long.\nThere are two doors, one at each end. You now realise what the noise was.")
        story("More Skeletons! Four of them, armed with swords\nare running down the corridor towards you.")
        story("They don't appear to have seen you and you notice a slight recess\nin the wall which may be a useful hiding place. You decide to try it.")
        story("The Skeletons do not notice you and disappear\nthrough the door into the Boat House.")
        vars.decision_133 = story("Breathing a sigh of relief, you press on to try the door\nat the north end of the passage. Will you eat provisions?")
        if vars.decision_133 == "YES":
            take_provs()
        change_stats(2, 2)
        story("Going through the door you enter a large room.\nVarious bits of wooden debris are strewn untidily across the floor.")
        story("Apart from your entrance door, there is also a door in the north wall.\nIn one corner is a crude wooden desk with a box on it.")
        story("In another corner, apparently asleep (or dead), is a hideous-looking\nman-sized creature with warty skin, wild hair and long claws for fingernails.")
        vars.decision_134 = story("Will you tiptoe out through the NORTH door\nor tiptoe across to the desk to look at the BOX?")
        if vars.decision_134 == "BOX":
            story("As you move, the creature's eyes flash open.\nHe sees you and slowly gets to his feet.")
            story("His breathing becomes heavy and he stalks towards you.\nYou must stand and fight him. He is a powerful adversary - a WIGHT!")
            story("He is large, strong and evil. The battle commences:\nYou fight with your sword.")
            vars.monster = [9, 6]
            #after inflicting first wound:
            story("Something is not quite right. You landed a fair blow on him,\nbut he appears not to have noticed the wound!")
            story("You deduce that this Undead creature is not vulnerable to normal weapons.\nYou may choose a new weapon or use your current weapon.")
            story("Wights are vulnerable only to\nweapons made of solid silver.")
            while vars.decision_135 not in vars.equipment:
                vars.decision_135 = story("Which item from your pack\ndo you choose?")
                if vars.decision_135 not in vars.equipment:
                    story("You don't have that.")
            if vars.decision_135 == "CHISEL" or vars.decision_135 == "Bow And Arrow":
                if vars.decision_135 == "BOW AND ARROW":
                        if stat_test(2):
                            story("You are lucky, you hit and the creature dies instantly.")
                        else:
                               story("You are unlucky. You miss.")
                story("Your weapon is made of solid silver.\nIf you wish to escape during the battle, you may do so.")
                if fight("Wight"):#the creature wounds you 3 times
                    story("After you have suffered your third wound, you notice that your strength is ebbing.")
                    change_stats(0, 1)
                    story("You deduce that this is yet another magical power of this foul creature and you feel a shiver of panic.")
                    vars.decision_136 = story("Will you continue or run? If you want to escape, pay the penalty to flee through the north door. Will you?")
                    if vars.decision_136 == "YES":
                        story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                        story("You follow it for several metres,\nuntil bends to the west, and continue onwards.")
                        story("Some way down the passage you come across a narrow opening in the north wall and decide to go through.")
                        vars.door = 89
                    #from now on, every third wound takes 1 point from your skill
                if fight("Wight"): #before 3 wounds
                    story("The Wight lies in a heap in the corner of the room. You approach his desk\nand open the box. There are 18 Gold Pieces within the box.")
                    vars.gold += 18
                    change_stats(2, 2)
                    vars.decision_137 = story("Do you want to eat provisions?")
                    if vars.decision_137 == "YES":
                        take_provs()
                    story("When you are ready,\nyou leave by the north door.")
                    story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                    story("You follow it for several metres,\nuntil bends to the west, and continue onwards.")
                    story("Some way down the passage you come across a narrow opening in the north wall and decide to go through.")
                    vars.door = 89
            else:    
                story("The weapon you are using is not made of silver, have one more Attack Round.") #if he hits you, it counts. if you hit him, it doesn't
                story("You run for the north door and he inflicts a final wound as you flee.") #make work
        elif vars.decision_134 == "NORTH":
            if stat_test(2):
                story("You are lucky, you make it out\nthrough the north door.")
                story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                story("You follow it for several metres,\nuntil bends to the west, and continue onwards.")
                story("Some way down the passage you come across a narrow opening in the north wall and decide to go through.")
                vars.door = 89
                story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                story("You follow it for several metres,\nuntil it bends to the west, and continue onwards.")
                story("Some way down the passage you come across a narrow opening\nin the north wall and decide to go through.")
                story("You climb through the opening and find yourself at the top\nof a narrow staircase leading downwards. Cautiously, you descend the stairs...")
                vars.checkpoint = 15
                vars.decision_113 = "GO"
            else:
                story("You are unlucky. As you move, the creature's eyes flash open.\nHe sees you and slowly gets to his feet.")
                story("His breathing becomes heavy and he stalks towards you.\nYou must stand and fight him. He is a powerful adversary - a WIGHT!")
                story("He is large, strong and evil. The battle commences:\nYou fight with your sword.")
                vars.monster = [9, 6]
                #after inflicting first wound:
                story("Something is not quite right. You landed a fair blow on him,\nbut he appears not to have noticed the wound!")
                story("You deduce that this Undead creature is not vulnerable to normal weapons.\nYou may choose a new weapon or use your current weapon.")
                story("Wights are vulnerable only to\nweapons made of solid silver.")
                while vars.decision_135 not in vars.equipment:
                    vars.decision_135 = story("Which item from your pack\ndo you choose?")
                    if vars.decision_135 not in vars.equipment:
                        story("You don't have that.")
                if vars.decision_135 == "CHISEL" or vars.decision_135 == "Bow And Arrow":
                    if vars.decision_135 == "BOW AND ARROW":
                            if stat_test(2):
                                story("You are lucky, you hit and the creature dies instantly.")
                            else:
                                story("You are unlucky. You miss.")
                    story("Your weapon is made of solid silver.\nIf you wish to escape during the battle, you may do so.")
                    if fight("Wight"):#if the creature wounds you 3 times:
                        story("After you have suffered your third wound, you notice that your strength is ebbing.")
                        change_stats(0, 1)
                        story("You deduce that this is yet another magical power of this foul creature and you feel a shiver of panic.")
                        vars.decision_136 = story("Will you continue or run? If you want to escape, pay the penalty to flee through the north door. Will you?")
                        if vars.decision_136 == "YES":
                            story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                            story("You follow it for several metres,\nuntil bends to the west, and continue onwards.")
                            story("Some way down the passage you come across a narrow opening in the north wall and decide to go through.")
                            vars.door = 89
                        #from now on, every third wound takes 1 point from your skill
                    if fight("Wight"): #before 3 wounds
                        story("The Wight lies in a heap in the corner of the room. You approach his desk\nand open the box. There are 18 Gold Pieces within the box.")
                        vars.gold += 18
                        change_stats(2, 2)
                        vars.decision_137 = story("Do you want to eat provisions?")
                        if vars.decision_137 == "YES":
                            take_provs()
                        story("When you are ready,\nyou leave by the north door.")
                        story("The door slams shut with a loud bang behind you.\nYou find yourself in a passageway running ahead northwards.")
                        story("You follow it for several metres,\nuntil bends to the west, and continue onwards.")
                        story("Some way down the passage you come across a narrow opening in the north wall and decide to go through.")
                        vars.door = 89
                else:    
                    story("The weapon you are using is not made of silver, have one more Attack Round.") #if he hits you, it counts. if you hit him, it doesn't
                    story("You run for the north door and he inflicts a final wound as you flee.") #make work
    
    if vars.door == 89:
        vars.checkpoint = 15
        vars.decision_113 = "GO"