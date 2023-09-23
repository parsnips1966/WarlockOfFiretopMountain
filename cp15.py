from functions import *
import variables as vars

def checkpoint_15():
        story("You find yourself in a short, narrow passageway with a door ahead to the north.\nYou try this door. The door squeaks open on rusty hinges.")
        story("The room is dark and your eyes begin to adjust themselves\nas you close the door behind you. You hear a shuffling in the room\nbut before you can react, a blow to your head knocks you sensless.")
        change_stats(1, 2, "subtract")
        story("You awake with a throbbing head and look around. The room is about eight metres square,\nwith doors to the north and south. You have been dumped in the south-west corner.")
        story("Standing motionless in the centre of the room are four men.\nAt least, they appear to be men. There skin is a greeny-grey colour.")
        story("Their clothes are tattered and torn - and they are all staring vacantly at the ceiling.\nOne carries a club, one a scythe, one an axe and one a pick.")
        story("Around the room are various peasant style weapons\n(pitchforks, axe-handles, pointed sticks etc.),\none or two shields, and several barrels.")
        story("In the north-east corner is a human corpse with a sword in one hand\nand a shield in the other. You move your hand up to your head to feel for signs of blood\nand you are relieved to find you are not bleeding.")
        story("But as your hand moves, the strange creatures\nin the centre of the room turn their eyes down towards you")
        vars.decision_100 = story("Do you:\nTry to TALK to them\nJUMP to your feet and charge them with your sword\nScramble for an exit through the south DOOR?")
        if vars.decision_100 == "TALK":
            story("Their vocabulary is limited to a series of moans and groans.\nThey appear not to be intelligent at all. Furthermore your conversation\nmerely serves to attract their attention to you.")
            story("They grip their weapons and it looks as though you will have to fight them.\nHowever there is a slim chance that you could make it to the door you came in through.")
            vars.decision_100 = story("Do you you want to try for that DOOR or have you resigned yourself to a BATTLE?")
        if vars.decision_100 == "DOOR":
            story("Your head hurts and you feel dizzy as you rise to your feet.\nThe four men stir into action and move towards you in single file with their weapons ready.")
            story("You grope your way down the wall for the south door\nbut it will be touch and go whether you make it.\nYour foot slips on a loose pebble and you fall to the ground.")
            story("Before you can regain your footing,\nthe creatures are upon you.")
        story("The four creatures shuffling towards you are mindless ZOMBIES.\nTheir vacant eyes suggest that their actions are controlled by a will which is not their own.")
        story("You are still too dizzy to think properly, but you must act quickly.\nThe first Zombie reaches you and prepares to swing his club.")
        story("You must fight him.")
        vars.monster = [7, 6]
        if fight("Zombie"):
            change_stats(2, 2)
            vars.monster = [6, 6]
            if fight("Zombie with scythe"):
                vars.monster = [6, 6]
                if fight("Zombie with pick"):
                    vars.monster = [6, 5]
                    if fight("Zombie with axe"):
                        story("The poor wretches lying dead at your feet almost look happy\nto be relieved of the burden of life. But as you look down at them,\nyou sense you are not the only one to know of their deaths.")
                        vars.decision_101 = story("Looking around the room, will you:\nInvestigate the WEAPONS lying around\nGO over to the dead body in the north-east corner\nor CHECK the barrels?")
                        if vars.decision_101 == "GO":
                            vars.gold1 = 0
                            story("You check over the body. The poor wretch was obviously caught\nin the same way that you were, but his weaker skull shattered under the club's blow.")
                            story("He wears a suit of leather armour no better than your own,\nholds a wooden shield on one wrist and clutches a steel-bladed sword in his other hand.")
                            story("In his pockets are 8 Gold Pieces and around his neck is a silver crucifix.\nYou may take any two of these items you wish.")
                            vars.items = 0
                            story("What are these mysterious items you have collected.")
                            while vars.items < 2:
                                vars.decision_108 = story("Which item do you take:\nThe ARMOUR, The SHIELD, The SWORD, The GOLD or the CRUCIFIX?")
                                if vars.decision_108 == "ARMOUR":
                                    story("You now have a fresh set of armour, equivalent to your own.\nYou decide which of the two you wish to keep and throw the away.")
                                    vars.items += 1
                                elif vars.decision_108 == "SHIELD":
                                    vars.decision_109 = story("The shield is a standard wooden type.\nDo you want to keep it anyway?")
                                    if vars.decision_109 == "YES":
                                        vars.equipment.append("Zombie's Shield")
                                    vars.items += 1
                                elif vars.decision_108 == "SWORD":
                                    change_stats(2, 2)
                                    story("The sword is enchanted and will aid you in battle.\nAs long as you use this sword, you may increase your initial skill by 2 points.")
                                    vars.decision_110 = story("Will you TAKE it and throw your old sword away\nor would you rather KEEP your own sword?")
                                    if vars.decision_110 == "TAKE":
                                        vars.equipment.append("Enchanted Sword")
                                        change_stats(0, 2) #initial skill and current skill
                                    vars.items += 1
                                elif vars.decision_108 == "GOLD":
                                    story("You are now 8 Gold Pieces richer. You also find\nanother 2 Gold Pieces in his boot, hidden there for safety.")
                                    vars.gold += 10
                                    vars.items += 1
                                elif vars.decision_108 == "CRUCIFIX":
                                    story("The crucifix is solid silver and worth 4 Gold Pieces.")
                                    vars.equipment.append("Crucifix")
                                    vars.items += 1
                            change_stats(0, 1)
                            change_stats(2, 1)
                            story("A noise startles you, prompting you to leave the room quickly.\nYou walk up to investigate the north door.")
                            vars.decision_111 = "DOOR"
                        elif vars.decision_101 == "CHECK":
                            story("The barrels contain a clear brown liquid.\nYou sniff it. It smells like rum. You taste it. It is rum.")
                            story("You cup your hands, pour some in and take a swig.\nYou gasp - by golly, it's good!")
                            change_stats(1, 6)
                            change_stats(2, 1)
                            story("A noise startles you, prompting you to leave the room quickly.\nYou walk up to investigate the north door.")
                            vars.decision_111 = "DOOR"
                        elif vars.decision_101 == "WEAPONS":
                            story("You find nothing remarkable about the weapons,\nin fact not a single weapon looks more useful than your sword.")
                            story("As you search the debris, you hear a deep thumping from the north followed by a scream\nthat sends a shiver down your spine. You rush to the north door to investigate.")
                            vars.decision_111 = "DOOR"
                        if vars.decision_111 == "DOOR":
                            story("The door opens and you find yourself in a dark crypt\nof some kind. The room is very large.")
                            story("At one end is an altar, and various coffins are strewn about the room.\nThere is a door behind you in the south wall, and also one in the west wall.")
                            vars.decision_102 = story("Do you want to INVESTIGATE the room further or,\nif the place gives you the creeps, will you LEAVE via the west door?")
                            if vars.decision_102 == "INVESTIGATE":
                                story("The silence is deathly. A slow drip startles you as you creep around the coffins.\nThe altar is ornately carved and studded with jewels.")
                                story("Beautifully woven drapes hang from the walls although they are\nthreadbare in places. There are three coffins in the room.")
                                story("A creaking noise makes you whirl round and the light\nfrom your lantern falls on the largest coffin. It is opening!")
                                story("As you watch, a tall man with a white face sits upright. His eyes open and fall on you.\nHis expression changes from one of tranquility to one of abject hate.")
                                story("His mouth opens and a terrifying hiss comes from his throat.\nHis teeth are wolf-like. He beckons you to come over.")
                                vars.decision_103 = story("Do you:\nAPPROACH him as he wishes?\nDraw your sword and prepare to FIGHT?\nReach into your BAG for another means of attack?\nRun for the west DOOR?")
                                if vars.decision_103 == "APPROACH":
                                    story("As you approach you feel his eyes burn into you\nwith considerable power. You begin to weaken under his gaze.")
                                    change_stats(1, 1, "subtract")
                                    story("You are gradually losing your own will.")
                                    vars.decision_103 = story("Will you try to draw your sword and FIGHT him\nor look for some other means of attack in your BAG?")
                                if vars.decision_103 == "FIGHT":
                                    vars.decision_107 = "SWORD"
                                if vars.decision_103 == "BAG":
                                    story("The creature you are facing is a VAMPIRE! You have various lines of attack.\nYour sword will do little real damage.")
                                    story("A Crucifix or steel-bladed sword will hold him at bay but will not kill him.\nIf you have either of these you may use it to get you through the west door.")
                                    story("If you are determined to kill the Vampire,\nyou must overpower it and drive a wooden stake through its heart.")
                                    vars.decision_107 = story("Will you go for the DOOR\nuse a wooden STAKE\nor draw your SWORD?")
                                    if vars.decision_107 == "DOOR":
                                        if "Crucifix" not in vars.equipment and "Steel sword" not in vars.equipment:
                                            vars.decision_107 = story("You don't have a steel-bladed sword or a crucifix. Will you use a wooden STAKE or draw your SWORD?")
                                        else:
                                            vars.decision_102 = "LEAVE"
                                    if vars.decision_107 == "STAKE":
                                        if "Wooden Stake" in vars.equipment:
                                            story("Using the wooden stake and mallet (or makeshift mallet if you aren't carrying one),\nyou form a cross and move towards the Vampire, backing it into a corner.")
                                            story("It hisses and snatches at you but cannot come near you.\nHowever, it is going to be tricky getting the stake through its heart.")
                                            story("As you advance, you stumble and fall forwards. As luck would have it,\nthe stake flies forward and plunges into the shrieking creature.")
                                            if stat_test(2):
                                                story("You are lucky. The stake pierces the Vampire's heart.")
                                                vars.vampire = "dead"
                                            else:
                                                story("You are unlucky. The Vampire is merely grazed by the wound\nand it flings you backwards across the room towards the west door.")
                                                vars.monster = [10, 7]
                                                vars.decision_107 = story("Do you want to escape through the west DOOR\nor draw your SWORD and keep fighting?")
                                        else:
                                            vars.decision_107 = story("You do not have a wooden stake.\nWill you go for the DOOR or draw your SWORD?")
                                    if vars.decision_107 == "SWORD":
                                        story("As you swing your sword at the creature,\nit reaches out and catches the blade in its hand!")
                                        story("Your weapon is almost ineffective against the considerable strength of the creature.\nYou realize this and panic, but you must fight on.")
                                        vars.monster = [10, 10] #can test luck every 6 rounds to escape (vars.decision_102 = "LEAVE"). If roll 11 or 12 and unlucky - pg.224
                                        if fight("Vampire"):
                                            vars.vampire = "dead"
                                if vars.vampire == "dead":
                                    story("The body on the floor turns visibly older in front of your eyes.\nThe face looks fifty, then ninety, then well over a hundred years old.")
                                    story("The skin rots and the eyes decompose as you watch.\nYou notice a movement coming from the creature's chest.")
                                    story("As the remnants of the Vampire decay,\na small black face breaks through its chest.")
                                    story("It resembles a small black shrew, but as it frees itself and unfurls its wings\nyou realise it is a bat. You lunge at it, but it flaps away into the darkness.")
                                    story("You search the whole chamber quickly\n(remember, there are several other coffins there!)\nand find 30 Gold Pieces, a book, and a Y-shaped stick.")
                                    vars.decision_104 = story("You may take these items if you will leave behind\none item of Equipment you are already carrying. Will you?")
                                    if vars.decision_104 == "YES":
                                        vars.decision_105 = story("Which item of equipment will you leave behind?")
                                        vars.equipment.append("Y-shaped stick")
                                        vars.equipment.append("book")
                                        vars.gold += 30
                                        print(vars.decision_105.title())
                                        print(vars.equipment)
                                        while vars.decision_105.title() not in vars.equipment:
                                            vars.decision_105 = story("You don't have that. Which piece of equipment will you choose from your pack?")
                                            vars.equipment.remove(vars.decision_105.title())
                                            vars.decision_105 = "NO"
                                            if vars.decision_105 == "NO":
                                                vars.decision_106 = story("You can leave through the west door. Do you want to take provisions here?")
                                                if vars.decision_106 == "YES":
                                                    take_provs()
                                                vars.decision_102 = "LEAVE"
                                elif vars.decision_103 == "DOOR":
                                    vars.decision_102 = "LEAVE"
                            if vars.decision_102 == "LEAVE":
                                story("You are in a narrow east-west corridor. Looking westwards\nyou can see a crossroads ahead. You go on to the crossroads.")
                                vars.decision_112 = story("Standing at the crossroads\nwill you go NORTH, WEST or SOUTH?")
                                if vars.decision_112 == "SOUTH":
                                    story("You are in a short passageway which comes to a dead end\nseveral metres ahead of you.")
                                    vars.decision_122 = story("Will you search for SECRET passageways, or return to the crossroads\nand either follow the passageway ahead to the NORTH or turn to the WEST?")
                                    if vars.decision_122 == "SECRET":
                                        vars.decision_122 = story("You find no secret passages. You return to the crossroads. Will you go NORTHwards or WESTwards?")
                                    if vars.decision_122 == "NORTH":
                                        vars.decision_112 = "NORTH"
                                    if vars.decision_122 == "WEST":
                                        vars.decision_112 = "WEST"
                                if vars.decision_112 == "WEST":
                                    story("You follow the passage westwards until it turns round a corner to the south.\nJust before the bend is a signpost which reads 'Under Construction'.")
                                    story("In front of you is the beginning of a stairway leading downwards.\nOnly three steps have been built so far.")
                                    story("A number of shovels, picks and other tools were lying on the ground\nby the steps but, as you turned the corner,\nthey suddenly flurried into action and began working on the steps.")
                                    story("You are now watching various tools digging and hammering\nas if being handled by invisible workers. A humming chant becomes louder\nand you recognise it as 'Heigh-ho, Heigh-ho, It's off to work we go...'")
                                    story("As you stand watching you start to chuckle - the scene is quite amusing.\nYou sit and watch and even manage to chat to some of the magical tools.")
                                    change_stats(1, 2)
                                    change_stats(0, 1)
                                    vars.decision_121 = story("Then you turn back up the passageway to the crossroads.\nDo you go NORTHwards or SOUTHwards?")
                                    if vars.decision_121 == "NORTH":
                                        vars.decision_112 = "NORTH"
                                    if vars.decision_121 == "SOUTH":
                                        story("You are in a short passageway which comes to a dead end several metres ahead of you.\nYou study the rock face but there appears to be no way through.")
                                        story("You return to the crossroads\nand this time continue straight ahead northwards.")
                                        vars.decision_112 = "NORTH"
                                if vars.decision_112 == "NORTH":
                                    story("You are following a passageway which leads ahead to the north.\nAfter several metres it bends sharply to the east.")
                                    story("You continue eastwards until you eventually\ncome across a narrow opening in the north wall.")
                                    vars.decision_113 = story("Will you GO through this opening or continue EASTwards?")
                                    if vars.decision_113 == "EAST":
                                        story("You continue along the passageway to the east.\nAfter some thirty metres it turns to the south.")
                                        story("Following it round the bend\nyou eventually come to a stop at a large armoured door.")
                                        vars.decision_120 = story("Will you try the DOOR or return along the passage and GO through the narrow opening?")
                                        if vars.decision_120 == "DOOR":
                                            story("The large solid door has no handle. You charge it but to no avail.\nThe door is not going to budge.")
                                            story("You decide to give up and go through the opening\nyou passed in the east-west passageway some way back.")
                                            vars.decision_113 = "GO"
                                        elif vars.decision_120 == "GO":
                                            vars.decision_113 = "GO"
                                    if vars.decision_113 == "GO":
                                        story("You climb through the opening and find yourself at the top of a narrow staircase\nleading downwards. Cautiously, you descend the stairs...")
                                        story("The narrow staircase is cut into the rock\nand there are about twenty steps leading down. At the bottom of the steps\na passageway leads you into a large open chamber.")
                                        story("The chamber stinks of putrefying flesh.\nThe smell is so bad that you are tempted to turn back.")
                                        story("You may either search the bodies, or tiptoe quietly through the room.")
                                        vars.decision_114 = story("Will you:\nSearch the FIRST body\nSearch the SECOND body\nSearch the THIRD body\nor TIPTOE through the room?")
                                        vars.search = False
                                        if vars.decision_114 == "TIPTOE":
                                            story("You tiptoe through the room, up a narrow staircase\nending up at the top of the stairs in a passage.")
                                            story("'That was easy,' you think, and you begin to have second thoughts\nabout whether it would have been worthwhile to search the bodies.")
                                            vars.decision_114 = story("Do you want to return and search the bodies,\nstarting with the THIRD or press ON?")
                                        if vars.decision_114 == "FIRST":
                                            vars.decision_114 = story("You find 5 Gold Pieces in the pockets of the corpse. Will you now\nSearch the SECOND body, search the THIRD body or TIPTOE through the room northwards.")
                                            vars.gold += 5
                                            vars.search = True
                                        if vars.decision_114 == "SECOND":
                                            story("As you move over towards the second body,\nyou accidentally kick the third corpse on the floor.")
                                            story("Its eyes flick open and it quickly sits up\nand slashes you with its long, sharp fongernails.")
                                            if stat_test(2):
                                                story("You are lucky, the creature misses.")
                                            else:
                                                story("You are unlucky, it has caught you across the leg.")
                                                change_stats(1, 1, "subtract")
                                            vars.decision_114 = "GHOUL"
                                        if vars.decision_114 == "THIRD":
                                            story("As you search the body, you try to avoid looking at the terrible face,\ngrey and decomposing. Maggots crawl from its nose and mouth.")
                                            story("You jump back startled when its eyes suddenly flick open!\nJust in time you avoid a vicious slash from its long sharp fingernails.")
                                            story("It quickly springs to its feet and eyes you\nwith a sadistic leer spreading across its mouth.")
                                            vars.decision_114 = "GHOUL"
                                        if vars.decision_114 == "GHOUL":
                                            story("The creature now standing before you is a semi-decayed man.\nHis quick eyes dart from side to side watching you.")
                                            story("His long tongue flashes out with a hissing noise. His teeth and nails are sharp\nand he doesn't seem to be afraid of your weapon. He is a GHOUL!")
                                            story("He has the ability to paralyse you if he scores four seperate wounds\non you during this battle, so beware!")
                                            vars.monster = [8, 7] #paralyses you if hits you 4 times. killed or paralysed, pg.64
                                            if fight("Ghoul"):
                                                story("The Ghoul twitches and dies at your feet.\nYou search its body and find little of interest.")
                                                vars.decision_115 = story("A couple of earrings, worth 1 Gold Piece between them,\nare in one of its pockets. Will you take these?")
                                                if vars.decision_115 == "YES":
                                                    vars.equipment.append("Earrings")
                                                if vars.search == True: #doens't work. need to not search twice
                                                    story("You search the first body and find 5 Gold Pieces.")
                                                    vars.gold += 5
                                                vars.decision_116 = story("Do you want to stop here,\nrest and take provisions?")
                                                if vars.decision_116 == "YES":
                                                    take_provs()
                                                change_stats(2, 2)
                                                vars.decision_117 = story("Will you press on NORTHwards\nor search the SECOND body?")
                                                if vars.decision_117 == "SECOND":
                                                    story("You search the pockets of the other body and find 8 Gold Pieces,\na bottle of liquid and an old piece of parchment. You take these items.")
                                                    vars.gold += 8
                                                    vars.decision_118 = story("Will you read the PARCHMENT or test the LIQUID?")
                                                    if vars.decision_118 == "PARCHMENT":
                                                        story("The parchment is well worn and almost illegible.\nIt is a map of some sort, headed 'The Maze of Zagor'.")
                                                        story("You can make little sense of it, although a room to the north is marked '...GER'\nand another to the east is marked 'SM...P...LE'.")
                                                        vars.equipment.append("Maze Map")
                                                        vars.decision_119 = story("You fold up the map and put it in your pocket. Do you wish to test the LIQUID or make your way NORTHwards?")
                                                        if vars.decision_119 == "LIQUID":
                                                            story("You swallow some of the liquid. The liquid is smooth and watery and, as you drink it,\nyou begin to glow. You feel euphoric and a little drunk at the same time.")
                                                            story("Your confidence grows and your weariness disappears.\nThe bottle contains HOLY WATER, blessed by the overpriest of Kaynlesh-Ma.")
                                                            story("It has restored your stamina almost to full strength.")
                                                            #2 less than initial stamina, unless it is already higher than this
                                                            #1 less than initial skill, unless already higher
                                                            change_stats(2, 4)
                                                            vars.decision_117 = "NORTH"
                                                        elif vars.decision_119 == "NORTH":
                                                            vars.decision_117 = "NORTH"
                                                    elif vars.decision_118 == "LIQUID":
                                                        story("You swallow some of the liquid. The liquid is smooth and watery and, as you drink it,\nyou begin to glow. You feel euphoric and a little drunk at the same time.")
                                                        story("Your confidence grows and your weariness disappears.\nThe bottle contains HOLY WATER, blessed by the overpriest of Kaynlesh-Ma.")
                                                        story("It has restored your stamina almost to full strength.")
                                                        #2 less than initial stamina, unless it is already higher than this
                                                        #1 less than initial skill, unless already higher
                                                        change_stats(2, 4)
                                                if vars.decision_117 == "NORTH":
                                                    vars.decision_114 = "ON"
                                                    story("You leave the chamber, walk down a short passage and reach a staircase going up.\nYou climb the stairs and arrive at the top in a passageway.")
                                                    story("At the top of the stairs the passageway turns sharply to the east.\nAs you pause to get your bearings, you hear a creaking in the rock behind you.")
                                                    story("You spin round in time to see a heavy portcullis drop\nto seal off the passageway behind you. Your only way now is forward!")
                                                    vars.checkpoint = 17
                                        if vars.decision_114 == "ON":
                                            story("You are following a passageway which leads ahead to the north.\nAfter several metres it bends sharply to the east.")
                                            story("You continue eastwards until you eventually\ncome across a narrow opening in the north wall.")
                                            vars.decision_137 = story("Will you GO through this opening or continue EASTwards?")
                                            if vars.decision_137 == "GO":
                                                vars.checkpoint = 15
                                                vars.decision_113 = "GO"
                                            elif vars.decision_137 == "EAST":
                                                story("You continue along the passageway to the east.\nAfter some thirty metres it turns to the south.")
                                                story("Following it around the bend you eventually\ncome to a stop at a large armoured door.")
                                                vars.decision_137 = story("Will you try the DOOR or would you prefer to return along the passage and GO through the narrow opening?")
                                                if vars.decision_137 == "GO":
                                                    vars.checkpoint = 15
                                                    vars.decision_113 = "GO"
                                                elif vars.decision_137 == "DOOR":
                                                    story("The large solid door has no handle. You charge it,\nbut to no avail. The door is not going to budge.")
                                                    story("You decide to give up and go through the opening\nyou passed in the east-west passageway some way back.")
                                                    vars.checkpoint = 15
                                                    vars.decision_113 = "GO"
                                                    