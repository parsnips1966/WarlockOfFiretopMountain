from functions import *
import variables as vars

def checkpoint_13():
    story("You are on the north bank of a fast-flowing river\nin a large underground cavern.")
    story("Facing northwards, the rock face is smooth and glistening with moisture.\nMoss of many different hues grows on the surface.")
    story("There is an eerie silence punctuated only by the splashings of the river\nas it flows behind you. You have three options.")
    vars.decision_89 = story("A passage runs off to the north-WEST\nA large timber DOOR is directly in front of you in the middle of the rock face\nAnother passage runs out along the river EASTwards.")
    if vars.decision_89 == "WEST":
        story("The short passage begins to narrow\nand ends a few metres ahead at a doorway.")
        vars.decision_90 = story("Do you wish to go through the DOOR or go back to the RIVER?")
        if vars.decision_90 == "DOOR":
            story("You are in a small, foul-smelling room.\nYou notice two doors: one to the west and one behind you to the south.")
            story("The furniture in the room is sparse and has been made mostly from bits of old boats.\nThere appears to be nothing of value in the room, but a bunch of keys hangs on the wall.")
            story("An old man in ragged clothes is slumped asleep on a 'bench'\nmade from half a rowing boat, snoring loudly.")
            story("Next to him is a vicious-looking brown dog with red eyes and black teeth,\nwhom you have awakened and who is now eyeing you suspiciously.\nA deep growl is coming from its throat")
            vars.decision_91 = story("Will you:\nTiptoe an exit through the SOUTH door\nBANG on the door behind you and cough a few 'Ahem's' to wake up the old man\nLEAP across the room with sword drawn to cut down the dog?")
            if vars.decision_91 == "SOUTH":
                story("The door opens and you find yourself in the passage leading back to the riverbank.")
                vars.decision_89 = story("You return to the rockface. Do you go for the DOOR in the middle of the rockface?\nor go down the passage running off EASTwards along the riverbank?")
                pass
            elif vars.decision_91 == "BANG":
                story("The old man's eyes flutter open. He sees you and grabs for half an oar lying by his bench.\nYou tell him you mean no harm but he remains on guard and eyes you cautiously.")
                story("Although he looks harmless enough, his dog could be dangerous.\nThe man's boots are undone.")
                vars.decision_92 = story("Will you:\nRUSH the dog with your weapon drawn?\nASK the man questions regarding your quest?\nTELL him his boots are undone?")
                if vars.decision_92 == "RUSH":
                    story("The dog springs as you move. Its hideous black teeth are coming straight for your throat!\nTwo metres from you, a blast of fire shoots from its mouth right at your face!")
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
                        else:
                            story("The Dog didn't scorch you with its fiery breath.")
                    
                elif vars.decision_92 == "ASK":
                    #141
                    pass
                elif vars.decision_92 == "TELL":
                    #165
                    pass
            elif vars.decision_91 == "LEAP":
                #249
                pass
        elif vars.decision_90 == "RIVER":
            vars.checkpoint = 13
            pass
    elif vars.decision_89 == "DOOR":
        #104
        pass
    elif vars.decision_89 == "EAST":
        #99
        pass
