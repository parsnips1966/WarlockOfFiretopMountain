from functions import *
import variables as vars


def checkpoint_14():        
        story("The short passage begins to narrow\nand ends a few metres ahead at a doorway.")
        vars.decision_90 = story("Do you wish to go through the DOOR or go back to the RIVER?")
        if vars.decision_90 == "DOOR":
            story("You are in a small, foul-smelling room.\nYou notice two doors: one to the west and one behind you to the south.")
            story("The furniture in the room is sparse and has been made mostly from bits of old boats.\nThere appears to be nothing of value in the room, but a bunch of keys hangs on the wall.")
            story("An old man in ragged clothes is slumped asleep on a 'bench'\nmade from half a rowing boat, snoring loudly.")
            story("Next to him is a vicious-looking brown dog with red eyes and black teeth,\nwhom you have awakened and who is now eyeing you suspiciously.\nA deep growl is coming from its throat")
            vars.decision_91 = story("Will you:\nTiptoe an exit through the SOUTH door\nBANG on the door behind you and cough a few 'Ahem's' to wake up the old man\nLEAP across the room with sword drawn to cut down the dog?")
            if vars.decision_91 == "LEAP":
                vars.decision_92 = "RUSH"
            if vars.decision_91 == "SOUTH":
                story("The door opens and you find yourself in the passage leading back to the riverbank.")
                vars.decision_89 = story("You return to the rockface. Do you go for the DOOR in the middle of the rockface?\nor go down the passage running off EASTwards along the riverbank?")
            if vars.decision_91 == "BANG":
                story("The old man's eyes flutter open. He sees you and grabs for half an oar lying by his bench.\nYou tell him you mean no harm but he remains on guard and eyes you cautiously.")
                story("Although he looks harmless enough, his dog could be dangerous.\nThe man's boots are undone.")
                vars.decision_92 = story("Will you:\nRUSH the dog with your weapon drawn?\nASK the man questions regarding your quest?\nTELL him his boots are undone?")
                if vars.decision_92 == "TELL":
                    story("The old man thanks you and rather sheepishly ties up his boots.\nYou explain that you mean no harm and he calms down, calling off his dog.")
                    story("He tells you that this area is the only passageway through to the inner chambers.\nSome years ago the river swelled after a particularly severe spring thaw\nand cut off supplies from the outside world.")
                    story("All the area's inhabitants starved to death but the Master,\nrealizing he needed defences against the outside world, put a curse on the area.")
                    story("The last remaining creatures became the Undead and now guard\nthe passageways through. He starts to inquire about you.")
                    vars.decision_99 = story("Will you:\nBe straight with him and TELL him of your quest\nThank him for the chat and leave through the south DOOR\nTry to GRAB the keys and go for the nearest door?")
                    if vars.decision_99 == "DOOR":
                        story("The door opens and you find yourself in the passage\nleading back to the riverbank. You return to the river.")
                        vars.decision_89 = story("Will you go for the DOOR in the middle of the rockface\nor go down the passage running off EASTwards along the river?")
                    elif vars.decision_99 == "GRAB":
                        vars.decision_92 = "RUSH"
                if vars.decision_92 == "ASK" or vars.decision_99 == "TELL":
                    story("When the old man learns of your quest for treasure he becomes angry\nand bids you begone - he'll have nothing to do with fortune hunters.")
                    vars.decision_98 = story("His dog senses his anger and snarls menacingly.\nWill you smile, thank him and exit through the SOUTH door\nor STAY to try and pacify him?")
                    if vars.decision_98 == "SOUTH":
                        story("The door opens and you find yourself in the passage\nleading back to the riverbank. You return to the river.")
                        vars.decision_89 = story("Will you go for the DOOR in the middle of the rockface\nor go down the passage running off EASTwards along the riverbank?")
                        pass
                    elif vars.decision_98 == "STAY":
                        story("He will not be pacified. As you shift uneasily around the room, he shouts a word at the dog.")
                        vars.decision_92 = "RUSH"                                  
            if vars.decision_92 == "RUSH" or vars.decision_98 == "STAY":
                if vars.decision_98 == "STAY":
                    story("He will not be pacified. As you shift uneasily around the room, he shouts a word at the dog."
                          )
                story("The dog springs as you move. Its hideous black teeth are coming straight for your throat!\nTwo "
                      "metres from you, a blast of fire shoots from its mouth right at your face!")
                story("You duck just in time but must now fight the beast.")
                story("In addition to its normal attack, throw one die every Attack Round for its fiery breath.")
                vars.monster = [7, 6]
                while True:
                    if fight("Dog", rounds=1):
                        break
                    vars.dice_num = randint(1, 6)
                    if vars.dice_num < 3:
                        if not stat_test(2):
                            story("The Dog scorched you with its fiery breath.")
                            change_stats(1, 1, "subtract")
                        else:
                            story("The Dog didn't scorch you with its fiery breath.")
                            # resets after 1 round
                    else:
                        story("The Dog didn't scorch you with its fiery breath.")
                story("The old man watches the fight but does not move until you kill his dog.\nYou may escape through the south door but you will not have time to take anything with you.")
                vars.decision_93 = story("Will you ESCAPE through the south door or do you wish to STAY?")
                change_stats(2, 1)
                if vars.decision_93 == "STAY":
                    story("The old man is furious at your killing his dog! His eyes turn white with anger.\nHe slowly rises from his seat and as he stands he appears to gain in size and stature.")
                    story("He is changing in front of your eyes.\nHe sprouts hair on his face and forearms. His nose lengthens and becomes dog-like.")
                    story("His teeth are pointed. He is a WEREWOLF and he advances towards you")
                    vars.decision_94 = story("You can escape only through the door behind you to the south. Otherwise you must fight him. Will you escape?")
                    if vars.decision_94 == "YES":
                        vars.decision_93 = "ESCAPE"
                    elif vars.decision_94 == "NO":
                        vars.monster = [8, 8]
                        if fight("Werewolf2"):
                            change_stats(2, 1)
                            vars.decision_95 = story("Will you rest and eat provisions?")
                            if vars.decision_95 == "YES":
                                take_provs()
                            story("As you look around the room there appears to be little of use,\nalthough the bunch of keys looks interesting, particularly the one marked 'Boat House'.")
                            story("None are numbered. You take the keys. There are doors to the west and south.")
                            vars.equipment.append("Boat House Key")
                            vars.decision_96 = story("Do you open the WEST door, or do you want to go SOUTH?")
                            if vars.decision_96 == "WEST":
                                story("You open the door to find the Werewolf's larder,\na miscellaneous collection of bones and decaying meats.")
                                vars.decision_97 = story("The smell is nauseating, although a jar of pickled eggs seems to offer fairly palatable food.\nIf you wish to take these, there will be enough for two meals. Will you?")
                                if vars.decision_97 == "YES":
                                    vars.provs += 2
                                story("Back in the room, you may now go out through the south door.")
                                vars.decision_96 ="SOUTH"
                            elif vars.decision_96 == "SOUTH":
                                vars.decision_93 = "ESCAPE"
                if vars.decision_93 == "ESCAPE":
                    story("The door opens and you find yourself in the passage\nleading back to the riverbank. You return to the river.")
                    vars.decision_89 = story("Will you go for the DOOR in the middle of the rockface\nor go down the passage running off EASTwards along the riverbank?")
        elif vars.decision_90 == "RIVER":
            vars.checkpoint = 13