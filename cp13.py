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
            story("Next to him is a vicious-looking brown dog with red eyes and black teeth,\nwhom you have awakened and who is now eyeing you suspiciously. A deep growl is coming from its throat")
            vars.decision_91 = story("You may:\nTiptoe an exit through the SOUTH door\nBANG on the door behind you and cough a few 'Ahem's' to wake up the old man\nLEAP across the room with sword drawn to cut down the dog")
            if vars.decision_91 == "SOUTH":
                story("The door opens and you find yourself in the passage leading back to the riverbank.")
                vars.decision_89 = story("You return to the rockface and may now either go for the DOOR in the middle of the rockface\nor go down the passage running off EASTwards along the riverbank.")
                pass
            elif vars.decision_91 == "BANG":
                #172
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
