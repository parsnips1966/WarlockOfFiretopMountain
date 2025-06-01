from functions import *
import variables as vars


def checkpoint_13():
    story("You are on the north bank of a fast-flowing river\nin a large underground cavern.")
    story("Facing northwards, the rock face is smooth and glistening with moisture.\nMoss of many different hues "
          "grows on the surface.")
    story("There is an eerie silence punctuated only by the splashings of the river\nas it flows behind you. You have "
          "three options.")
    vars.decision_89 = story("Do you take the passage running off to the north-WEST\nA large timber DOOR directly in "
                             "front of you in the middle of the rock face\nor another passage running out along the "
                             "river EASTwards?")
    if vars.decision_89 == "WEST":
        vars.checkpoint = 14
    elif vars.decision_89 == "DOOR":
        vars.checkpoint = 15
    elif vars.decision_89 == "EAST":
        vars.checkpoint = 16