from functions import *
import variables as vars

def checkpoint_18():
    story("Your tappings and scratchings at the rock face as you search\nfor secret doors and passageways resound "
          "through the dungeon corridors.")
    story("Various creatures roam freely through the underworld and your noises\nhave just attracted the attentions "
          "of one of the following monsters.")
    story("Roll one die.")
    vars.dice_num = randint(1, 6)
    if vars.dice_num == 1:
        vars.monster = [5, 3]
        if fight("Goblin"):
            vars.game = "Continue"
    if vars.dice_num == 2:
        vars.monster = [6, 3]
        if fight("Orc"):
            vars.game = "Continue"
    if vars.dice_num == 3:
        vars.monster = [6, 4]
        if fight("Gremlin"):
            vars.game = "Continue"
    if vars.dice_num == 4:
        vars.monster = [5, 4]
        if fight("Giant Rat"):
            vars.game = "Continue"
    if vars.dice_num == 5:
        vars.monster = [6, 5]
        if fight("Skeleton"):
            vars.game = "Continue"
    if vars.dice_num == 6:
        vars.monster = [8, 4]
        if fight("Troll"):
            vars.game = "Continue"
    if vars.game == "Continue":
        if vars.maze_monster == 48:
            vars.checkpoint = 17
            vars.decision_138 == "ON"
