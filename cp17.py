from functions import *
import variables as vars

def checkpoint_17():
    vars.game = "no"
    vars.decision_138 = story("Will you press ON forward or check the walls for SECRET passages?")
    if vars.decision_138 == "SECRET":
        story("You find no secret passages. However, your explorations\nattract some sort of creature, and as you listen you can hear\nsomething coming down the corridor towards you.")
        vars.maze_monster = 48
        vars.checkpoint = 18
    if vars.decision_138 == "ON":
        if vars.decision_139 != "EAST":
            vars.decision_139 = story("You are in a east-west corridor. If you go east,\nyou will turn a corner northwards. Will you go EAST or WEST?")
        if vars.decision_139 == "EAST":
            story("You are at the south end of a north-south corridor.\nLooking northwards, you can see a passage coming off from the east wall.")
            vars.decision_140 = story("Will you GO up to this passage\ncheck for SECRET passages as you walk northwards\nor go SOUTH, following a bend to the west?")
            if vars.decision_140 == "GO":
                story("You are standing in a T-junction where a passage\nto the east comes off a north-south corridor.")
                vars.decision_141 = story("Will you go SOUTH\ncheck for secret passages on the way SOUTHWARDS\ngo NORTH\ncheck for secret passages on the way NORTHWARDS\nor go EAST?")
                if vars.decision_141 == "SOUTH":
                    vars.checkpoint = 17
                    vars.decision_138 = "ON"
                    vars.decision_139 = "EAST"
                elif vars.decision_141 == "SOUTHWARDS":
                    #362
                    pass
                elif vars.decision_141 == "NORTH":
                    story("You are standing at a bend in the passage where you may go either west or south.")
                    vars.decision_142 = story("Will you go WEST\ngo SOUTH\ncheck for secret passages on the way WESTWARDS\nor check for secret passages on the way SOUTHWARDS?")
                    if vars.decision_142 == "WEST":
                        story("You are standing at a crossroads. To the west\nthe passageway goes on a few metres and turns northwards.")
                        story("To the north the passageway ends at a door. To the east\nthe passage continues and eventually turns southwards.")
                        story("Looking south, the passage\ngoes on as far as you can see.")
                        vars.decision_143 = story("Do you go WEST\ngo NORTH\ngo SOUTH\nor go EAST?")
                        if vars.decision_143 == "WEST":
                            story("You are standing in the corner of a bend in the passage.\nTo the north the passage ends in a dead end.")
                            vars.decision_144 = story("Will you INVESTIGATE this or go EASTwards?")
                            if vars.decision_144 == "INVESTIGATE":
                                story("You are standing at the north end of a short\nnorth-south passage. You are at a dead end.")
                                vars.decision_145 = story("Do you INVESTIGATE the wall\nor go SOUTHwards?")
                                if vars.decision_145 == "INVESTIGATE":
                                    story("You find no secret passages, but as you press the walls,\nyou hear a click. You feel dizzy and slump to the ground.")
                                    story("When you come to,\nthe suroundings look strange.")
                                    vars.decision_146 = story("You now stand at a crossroads. Will you go NORTH\ngo SOUTH\ngo WEST\nor go EAST?")
                                    if vars.decision_146 == "NORTH":
                                        story("You follow a long, narrow passageway which goes north, then west,\nthen north again and you eventually find yourself at a crossroads.")
                                        #308
                                        pass
                                    elif vars.decision_146 == "SOUTH":
                                        story("You set off south along a cobbled passageway. It swings west,\nthen south, then west again until you find yourself at a three-way junction.")
                                        vars.decision_147 = story("Will you go NORTH\ngo WEST\nor go back EAST?")
                                        if vars.decision_147 == "NORTH":
                                            story("You set off and find yourself in the middle of a north-south passageway.\nThere is a door in the western wall of the passage.")
                                            story("Opposite the door is a passage going off eastwards. To the north\nyou can see a door some metres ahead. To the south you can see a junction.")
                                            vars.decision_148 = story("Will you choose the door in the WEST wall\nthe door to the NORTH\nEASTwards\nor SOUTHwards?")
                                            if vars.decision_148 == "WEST":
                                                vars.decision_149 = story("The door opens into and east-west passage, which turns north\nafter several metres. Will you FOLLOW this direction\nor DECIDE against going through the door?")
                                                if vars.decision_149 == "FOLLOW":
                                                    story("You find yourself in a north-south corridor.\nTo the north the passge turns east some metres ahead.") #4
                                                    vars.decision_150 = story("Do you INVESTIGATE or go SOUTH,\nwhere the passageway also turns east?")
                                                    if vars.decision_150 == "INVESTIGATE":
                                                        story("You are standing in a short east-west passageway,\nwith a door blocking the way to the east.")
                                                        vars.decision_151 = story("To the west, the passage turns southwards after several metres.\nWill you GO round the bend or go through the DOOR?")
                                                        if vars.decision_151 == "GO":
                                                            #4
                                                            pass
                                                        elif vars.decision_151 == "DOOR":
                                                            story("You enter a large square room. In the centre of the room\nis a grey-haired old man sitting at a desk.")
                                                            story("His desk is covered in papers and parchments of various sorts\nand he holds a long quill pen. He is surrounded by books.")
                                                            story("Thousands of them line the shelves around the walls, from floor to ceiling. As you enter he looks up at you.")
                                                            if vars.game == "yes":
                                                                story("'You again?' says the Mazemaster, obviously annoyed at being disturbed. 'You are disturbing my concentration. Be off with you!'")
                                                                story("You begin to explain that you only returned by mistake,\nbut as you open your mouth, an icy glare from the old man silences you.")
                                                                vars.decision_152 = story("You decide to leave him to it. Will you leave\nby the WEST door or the SOUTH door?")
                                                                if vars.decision_152 == "WEST":
                                                                    #46
                                                                    pass
                                                                elif vars.decision_152 == "SOUTH":
                                                                    #392
                                                                    pass
                                                            elif vars.game == "no":
                                                                story("The old man glares at you as you enter the room.\nYou may either apologise, explain that you lost your way and leave\nthrough either the door in the west or south walls.")
                                                                story("Alternatively, you may try to talk to the old man. If you want to talk to him,\nyou can either be pleasant or you can demand that he answers your questions.")
                                                                vars.decision_153 = story("Will you apologise and leave through the WEST or SOUTH door,\nor talk to him and be PLEASANT or DEMANDing?")
                                                                vars.game = "yes"
                                                                if vars.decision_153 == "WEST":
                                                                    #46
                                                                    pass
                                                                elif vars.decision_153 == "SOUTH":
                                                                    #392
                                                                    pass
                                                                elif vars.decision_153 == "PLEASANT":
                                                                    #220
                                                                    pass
                                                                elif vars.decision_153 == "DEMAND":
                                                                    #191
                                                                    pass
                                                    elif vars.decision_150 == "SOUTH":
                                                        #332
                                                        pass
                                                elif vars.decision_149 == "DECIDE":
                                                    #329
                                                    pass
                                            elif vars.decision_148 == "NORTH":
                                                #392
                                                pass
                                            elif vars.decision_148 == "EAST":
                                                #299
                                                pass
                                            elif vars.decision_148 == "SOUTH":
                                                #238
                                                pass
                                        elif vars.decision_147 == "WEST":
                                            #180
                                            pass
                                        elif vars.decision_147 == "EAST":
                                            #70
                                            pass
                                    elif vars.decision_146 == "WEST":
                                        #79
                                        pass
                                    elif vars.decision_146 == "EAST":
                                        #349
                                        pass
                                elif vars.decision_145 == "SOUTH":
                                    #187
                                    pass
                            elif vars.decision_144 == "EAST":
                                #308
                                pass
                        elif vars.decision_143 == "NORTH":
                            #54
                            pass
                        elif vars.decision_143 == "SOUTH":
                            #160
                            pass
                        elif vars.decision_143 == "EAST":
                            #354
                            pass
                    elif vars.decision_142 == "SOUTH":
                        #52
                        pass
                    elif vars.decision_142 == "WESTWARDS":
                        #14
                        pass
                    elif vars.decision_142 == "SOUTHWARDS":
                        #234
                        pass
                elif vars.decision_141 == "NORTHWARDS":
                    #234
                    pass
                elif vars.decision_141 == "EAST":
                    #291
                    pass
            elif vars.decision_140 == "SECRET":
                #362
                pass
            elif vars.decision_140 == "SOUTH":
                #48
                pass
        elif vars.decision_139 == "WEST":
            story("You walk along the corridor, only to find out that the way westwards\nis blocked by a heavy portcullis. You walk back to where you were.")
            #48
            pass