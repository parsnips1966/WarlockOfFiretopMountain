from functions import *
import variables as v


def checkpoint_1():
    v.background = "passage"
    v.decision_2 = story("You enter the caverns of Firetop Mountain and within a few metres\nyou arrive at a "
                         "junction, do you want to go EAST or WEST?")
    if v.decision_2 == "EAST":
        v.background = "door"
        v.decision_3 = story("The passageway soon comes to an end at a locked wooden door.\nYou listen at the door "
                             "but hear nothing. Will you try to charge it down?")
        if v.decision_3 == "YES":
            story("You charge the door with your shoulder. Test your Skill by rolling two dice\nto see if it's less "
                  "than or equal to your Skill score.")
            if stat_test(0):
                v.background = "pit"
                story("The door bursts open and you fall headlong into a room.")
                story("But your heart jumps as you realise you are not landing on\nthe floor, but plunging down a pit "
                      "of some kind!")
                change_stats(1, 1, "subtract")
                story("Luckily it's not very deep.")
                v.background = "passage"
                story("You climb out and leave through the door heading westwards.")
            else:
                story("You rub your bruised shoulder and decide against\ntrying again. You turn around and head back "
                      "to the junction.")
                v.background = "passage"
        elif v.decision_3 == "NO":
            v.background = "passage"
            story("You turn around and head back to the junction.")
        v.background = "archtooutside"
        story("You arrive back at the junction. You look left to see the\ncave entrance in the dim distance but walk "
              "straight on.")
        v.decision_2 = "WEST"
    if v.decision_2 == "WEST":
        v.background = "passage"
        story("There's a right-hand turn to the north. Cautiously you approach a sentry post\non the corner and see a "
              "strange goblin-like creature wearing leather armour.")
        v.background = "sleepingorc"
        story("He is asleep at his post so you try to tiptoe past him. Test your Luck\nby rolling 2 dice to see if "
              "it's less than or equal to your Luck score.")
        story("Each time you Test your Luck one point\nwill be subtracted from your Luck score.")
        if stat_test(2):
            v.background = "door"
            story("You make it past. On your left,\nthe west face of the passage, there is a rough-cut wooden door.")
        else:
            v.background = "orc"
            story("You step with a crunch on some loose ground and his eyes flick open.")
            story("The creature that has just awakened is an Orc! He scrambles to his feet\nand turns to grasp an "
                  "alarm bell. You must attack him quickly.")
            fight_tuto()
            v.monster = [6, 5]
            if fight("Orc"):
                v.background = "door"
                story("On your left, the west face of the passage,\nthere is a rough-cut wooden door.")
        v.decision_4 = story("You listen at the door and can hear a rasping sound which\nmay be some kind of "
                             "creature snoring. Do you want to open the door?")
    v.checkpoint = 2
