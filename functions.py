"""Contains all the functions which control sections of the game including setting up the screen and tutorials."""

from time import sleep, time
from random import randint
import pygame
from pygame.locals import *
import variables as vars
import constants as consts
from json import load, dumps, dump


def fight_tuto() -> None:
    """Explains how fighting works the first time the player enters a battle."""
    if not vars.fight_tuto_done:
        story(
            "When fighting monsters, 2 dice will be rolled for the monster\nand added to its Skill score to determine its Attack Strength.")
        story("You will do the same and whoever has\nthe higher Attack Strength will land a blow.")
        story("If the values are equal then\nyou have avoided each others' Attacks.")
        story(
            "If a blow is landed it will take away 2 Stamina and\nthis is repeated until you or the monster are dead.")
        story(
            "At some points you may be given the option of running away from a battle.\nIf you do the monster gets a hit on you as you flee.")
        vars.fight_tuto_done = True


def provs_tuto():
    """Explains what Provisions do the first time a player encounters them."""
    if vars.provs_tuto_done == False:
        return " which restore 4 Stamina points"
    vars.provs_tuto_done = True


def take_provs() -> None:
    """Changes stamina and removes a Provision"""
    if vars.provs > 0:
        vars.provs -= 1
        change_stats(1, 4)
    else:
        story("You have no Provisions left.")


def story(txt: str, timer: int = 0, escape: bool = False, any_input: bool = False) -> str:
    """
    Initialises the display and all the items on it.
    Allows the player to click to move on and to type if the game asks a question.
    :param txt: The main text which appears in the centre of the screen.
    """
    autosave()
    output = ""
    # cursor_flash = 0
    txt = txt.split("\n")
    equip_str = ""
    consts.screen.fill(consts.BLACK)
    surf = pygame.image.load("./images/" + vars.background + ".jpg").convert()
    consts.screen.blit(surf, surf.get_rect())
    for i in range(len(txt)):
        text = txt[i]
        blit_text(text, -1, consts.height // 2 + (i * 30), 40, outline=True, centerx=True)
    if txt[-1][-1] == "?" or vars.escape:
        pygame.draw.rect(consts.screen, consts.BLACK, Rect(449, 509, 402, 62), 4)
        pygame.draw.rect(consts.screen, consts.WHITE, Rect(450, 510, 400, 60))
    blit_text("Player", 10, 10, underline=True, colour=consts.GREEN, outline=True)
    blit_text("Skill: " + str(vars.hero[0]), 10, 35, colour=consts.GREEN, outline=True)
    blit_text("Stamina: " + str(vars.hero[1]), 10, 60, colour=consts.GREEN, outline=True)
    blit_text("Luck: " + str(vars.hero[2]), 10, 85, colour=consts.GREEN, outline=True)
    for item in vars.equipment:
        equip_str += item + ", "
    equip_str = equip_str[0:-2]
    blit_text("Gold: " + str(vars.gold), 10, 615, outline=True)
    blit_text("Provisions: " + str(vars.provs), 10, 640, outline=True)
    blit_text("Equipment: " + str(equip_str), 10, 665, outline=True)
    if vars.fighting:
        if len(vars.monster_name) < 6:
            blit_text(vars.monster_name, 1230, 10, underline=True, colour=consts.RED, outline=True)
        elif len(vars.monster_name) < 10:
            blit_text(vars.monster_name, 1190, 10, underline=True, colour=consts.RED, outline=True)
        elif len(vars.monster_name) < 14:
            blit_text(vars.monster_name, 1150, 10, underline=True, colour=consts.RED, outline=True)
        else:
            blit_text(vars.monster_name, 1110, 10, underline=True, colour=consts.RED, outline=True)
        blit_text("Skill: " + str(vars.monster[0]), 1210, 35, colour=consts.RED, outline=True)
        blit_text("Stamina: " + str(vars.monster[1]), 1174, 60, colour=consts.RED, outline=True)
    if vars.dice_num != 0:
        if vars.dice_num < 7:
            draw_dice(vars.dice_num)
        else:
            num = 0
            while vars.dice_num - num > 6:
                num = randint(1, 6)
            draw_dice(num, 575)
            draw_dice(vars.dice_num - num, 725)
        vars.dice_num = 0
    if vars.dice_num2 != 0:
        if vars.dice_num2 < 7:
            draw_dice(vars.dice_num2)
        else:
            num = 0
            while vars.dice_num2 - num > 6:
                num = randint(1, 6)
            draw_dice(num, 575)
            draw_dice(vars.dice_num2 - num, 725)
        vars.dice_num2 = 0
    pygame.display.flip()
    while True:
        # attempted flashing cursor
        # cursor_flash += 1
        # if cursor_flash % 2 == 1:
        #    pygame.draw.rect(consts.screen, consts.BLACK, Rect(651 + 7 * len(output), 519, 5, 42))
        #    pygame.draw.rect(consts.screen, consts.WHITE, Rect(652 + 7 * len(output), 520, 3, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()
                if txt[-1][-1] == "?" or vars.fighting:
                    if output not in consts.INPUTS and not any_input:
                        blit_text("Please enter either one of the words in capitals, YES or NO.", 0, 100, 40,
                                  outline=False, centerx=True)
                        output = ""
                        equip_str = ""
                        surf = pygame.image.load("./images/" + vars.background + ".jpg").convert()
                        consts.screen.blit(surf, surf.get_rect())
                        for i in range(len(txt)):
                            text = txt[i]
                            blit_text(text, -1, consts.height // 2 + (i * 30), 40, outline=True, centerx=True)
                        if txt[-1][-1] == "?":
                            pygame.draw.rect(consts.screen, consts.BLACK, Rect(449, 509, 402, 62), 4)
                            pygame.draw.rect(consts.screen, consts.WHITE, Rect(450, 510, 400, 60))
                        blit_text("Player", 10, 10, underline=True, colour=consts.GREEN, outline=True)
                        blit_text("Skill: " + str(vars.hero[0]), 10, 35, colour=consts.GREEN, outline=True)
                        blit_text("Stamina: " + str(vars.hero[1]), 10, 60, colour=consts.GREEN, outline=True)
                        blit_text("Luck: " + str(vars.hero[2]), 10, 85, colour=consts.GREEN, outline=True)
                        for item in vars.equipment:
                            equip_str += item + ", "
                        equip_str = equip_str[:-2]
                        blit_text("Gold: " + str(vars.gold), 10, 615, outline=True)
                        blit_text("Provisions: " + str(vars.provs), 10, 640, outline=True)
                        blit_text("Equipment: " + str(equip_str), 10, 665, outline=True)
                        if vars.fighting:
                            if len(vars.monster_name) < 6:
                                blit_text(vars.monster_name, 1250, 10, underline=True, colour=consts.RED, outline=True)
                            elif len(vars.monster_name) < 11:
                                blit_text(vars.monster_name, 1200, 10, underline=True, colour=consts.RED, outline=True)
                            else:
                                blit_text(vars.monster_name, 1150, 10, underline=True, colour=consts.RED, outline=True)
                            blit_text("Skill: " + str(vars.monster[0]), 1220, 35, colour=consts.RED, outline=True)
                            blit_text("Stamina: " + str(vars.monster[1]), 1174, 60, colour=consts.RED, outline=True)
                        if vars.dice_num != 0:
                            if vars.dice_num < 7:
                                draw_dice(vars.dice_num)
                            else:
                                if vars.dice_num - 6 < 1:
                                    num = randint(1, 6)
                                num = randint(6, vars.dice_num)
                                draw_dice(num, 575)
                                draw_dice(vars.dice_num - num, 725)
                            vars.dice_num = 0
                        if vars.dice_num2 != 0:
                            if vars.dice_num2 < 7:
                                draw_dice(vars.dice_num2, y=500)
                            else:
                                if vars.dice_num2 - 6 < 1:
                                    num = randint(1, 6)
                                num = randint(6, vars.dice_num2)
                                draw_dice(num, 575, 500)
                                draw_dice(vars.dice_num2 - num, 725, 500)
                            vars.dice_num2 = 0
                        pygame.display.flip()
                        continue
                return output
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(output) > 0:
                        output = output[: -1]
                        pygame.draw.rect(consts.screen, consts.BLACK, Rect(449, 509, 402, 62), 4)
                        pygame.draw.rect(consts.screen, consts.WHITE, Rect(450, 510, 400, 60))
                elif event.key in range(97, 123) or event.key in range(48, 58) or event.key == pygame.K_SPACE:
                    if len(output) < 20:
                        output += chr(event.key).upper()
                        pygame.draw.rect(consts.screen, consts.BLACK, Rect(449, 509, 402, 62), 4)
                        pygame.draw.rect(consts.screen, consts.WHITE, Rect(450, 510, 400, 60))
                blit_text(output, 645 - 9 * len(output), 528, 40, colour=consts.BLUE, outline=True)
            pygame.display.flip()
        if timer > 0:
            sleep(timer)
            return


def blit_text(txt: str, x: int, y: int, size: int = 30, underline: bool = False, colour: tuple = (255, 255, 255),
              outline: bool = False, centerx: bool = False) -> None:
    """Blits text to the screen.
    :param txt: The text to blit to the screen.
    :param x: The point on the x axis where the left side of the text goes.
    :param y: The point on the y axis where the top of the text goes.
    :param size: The size of the text.
    :param underline: Dictates whether the text is underlined or not.
    :param colour: The colour of the text.
    :param outline: Dictates whether the text is outlined or not.
    """
    font = pygame.font.SysFont(None, size)
    font.set_underline(underline)
    main_text = font.render(txt, True, colour)
    if centerx:
        x = consts.width // 2 - main_text.get_width() // 2
    if outline:
        outline_text = font.render(txt, True, consts.BLACK)
        consts.screen.blit(outline_text, (x, y + 1))
        consts.screen.blit(outline_text, (x, y - 1))
        consts.screen.blit(outline_text, (x - 1, y))
        consts.screen.blit(outline_text, (x + 1, y))
        consts.screen.blit(outline_text, (x + 1, y + 1))
        consts.screen.blit(outline_text, (x + 1, y - 1))
        consts.screen.blit(outline_text, (x - 1, y + 1))
        consts.screen.blit(outline_text, (x - 1, y - 1))
    consts.screen.blit(main_text, (x, y))


def draw_dice(die_num: int, x: int = 650, y: int = 10) -> None:
    """
    Draws a die on the screen with the correct number of spots.
    :param die_num: The number of spots on the dice.
    :param x: The point on the x-axis where the left side of the die is placed.
    :param y: The point on the y-axis where the top of the die is placed.
    """
    pygame.draw.rect(consts.screen, consts.WHITE, Rect(x - 50, 150, 100, 100))
    if die_num == 1:
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
    elif die_num == 2:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 3:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 4:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 5:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)
    elif die_num == 6:
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 175), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 200), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x - 25, 225), y)
        pygame.draw.circle(consts.screen, consts.BLACK, (x + 25, 225), y)


def change_stats(stat: int, amount: int, operation: str = "") -> str:
    """Changes one of the player's stats by an amount.
    :param stat: The stat which will be changed.
    :param amount: How much the stat will be changed by.
    :param operation: What operation will be performed.
    """
    if operation == "subtract":
        if vars.hero[stat] - amount < 0:
            vars.hero[stat] = 0
            return story("You are dead.")
        vars.hero[stat] -= amount
        return ""
    num = vars.hero[stat] + amount
    if num > vars.init_hero[stat]:
        vars.hero[stat] = vars.init_hero[stat]
        return ""
    vars.hero[stat] += amount


def fight(name: str, escape_round: int = 99, rounds: int = 99) -> bool:
    """Controls fights between the player and a monster.
    :param name: The name of the player's opponent.
    :param escape_round: The round number from which the user has the choice to escape.
    :param rounds: The maximum number of rounds to be fought.
    """
    vars.fighting = True
    vars.monster_name = name
    round = 1
    vars.escape = round >= escape_round
    wounded = False
    for i in range(rounds):
        if vars.hero[1] > 0:
            if vars.monster[1] > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return False
                vars.hero_attack = randint(2, 12) + vars.hero[0]
                if story("Your Attack Strength is " + str(vars.hero_attack) + ".", 1, vars.escape) == "ESCAPE":
                    if vars.escape:
                        vars.escape = True
                        return True
                monster_attack = randint(2, 12) + vars.monster[0]
                story("The " + name + "'s Attack Strength is " + str(monster_attack) + ".", 1, vars.escape)
                if vars.hero_attack > monster_attack:
                    if vars.monster[1] - 2 < 0:
                        vars.monster[1] = 0
                    else:
                        vars.monster[1] -= 2
                    story("You land a blow.", 1, vars.escape)
                    if name == "Crocodile":
                        wounded = True
                elif vars.hero_attack < monster_attack:
                    change_stats(1, 2, "subtract")
                    story("The " + name + " lands a blow.", 1, vars.escape)
                else:
                    story("You avoid each other's blows.", 1, vars.escape)
                round += 1
            else:
                story("The " + name + " is dead.", 1, vars.escape)
                vars.fighting = False
                return True
        else:
            story("You are dead.", 999)
            return False
    return wounded


def stat_test(stat: int) -> bool:
    """Generates a random number between 2 and 12 and compares it to one of the player's stats."""
    if stat == 2:
        change_stats(2, 1, "subtract")
    dice_num = randint(2, 12)
    if dice_num <= vars.hero[stat]:
        return True
    return False


def autosave() -> None:
    account_data = {"gold": vars.gold, "provs": vars.provs, "hero": vars.hero, "init_hero": vars.init_hero,
                    "equipment": vars.equipment, "river": vars.river, "piranhas": vars.piranhas,
                    "fight_tuto_done": vars.fight_tuto_done, "provs_tuto_done": vars.provs_tuto_done,
                    "checkpoint": vars.checkpoint, "profile_name": vars.profile_name,
                    "decision_1": vars.decision_1, "decision_2": vars.decision_2, "decision_3": vars.decision_3,
                    "decision_4": vars.decision_4, "decision_5": vars.decision_5,
                    "decision_6": vars.decision_6, "decision_7": vars.decision_7, "decision_8": vars.decision_8,
                    "decision_9": vars.decision_9, "decision_10": vars.decision_10,
                    "decision_11": vars.decision_11, "decision_12": vars.decision_12, "decision_13": vars.decision_13,
                    "decision_14": vars.decision_14, "decision_15": vars.decision_15,
                    "decision_16": vars.decision_16, "decision_17": vars.decision_17, "decision_18": vars.decision_18,
                    "decision_19": vars.decision_19, "decision_20": vars.decision_20,
                    "decision_21": vars.decision_21, "decision_22": vars.decision_22, "decision_23": vars.decision_23,
                    "decision_24": vars.decision_24, "decision_25": vars.decision_25,
                    "decision_26": vars.decision_26, "decision_27": vars.decision_27, "decision_28": vars.decision_28,
                    "decision_29": vars.decision_29, "decision_30": vars.decision_30,
                    "decision_31": vars.decision_31, "decision_32": vars.decision_32, "decision_33": vars.decision_33,
                    "decision_34": vars.decision_34, "decision_35": vars.decision_35,
                    "decision_36": vars.decision_36, "decision_37": vars.decision_37, "decision_38": vars.decision_38,
                    "decision_39": vars.decision_39, "decision_40": vars.decision_40,
                    "decision_41": vars.decision_41, "decision_42": vars.decision_42, "decision_43": vars.decision_43,
                    "decision_44": vars.decision_44, "decision_45": vars.decision_45,
                    "decision_46": vars.decision_46, "decision_47": vars.decision_47, "decision_48": vars.decision_48,
                    "decision_49": vars.decision_49, "decision_50": vars.decision_50,
                    "decision_51": vars.decision_51, "decision_52": vars.decision_52, "decision_53": vars.decision_53,
                    "decision_54": vars.decision_54, "decision_55": vars.decision_55,
                    "decision_56": vars.decision_56, "decision_57": vars.decision_57, "decision_58": vars.decision_58,
                    "decision_59": vars.decision_59, "decision_60": vars.decision_60,
                    "decision_61": vars.decision_61, "decision_62": vars.decision_62, "decision_63": vars.decision_63,
                    "decision_64": vars.decision_64, "decision_65": vars.decision_65,
                    "decision_66": vars.decision_66, "decision_67": vars.decision_67, "decision_68": vars.decision_68,
                    "decision_69": vars.decision_69, "decision_70": vars.decision_70,
                    "decision_71": vars.decision_71, "decision_72": vars.decision_72, "decision_73": vars.decision_73,
                    "decision_74": vars.decision_74, "decision_75": vars.decision_75,
                    "decision_76": vars.decision_76, "decision_77": vars.decision_77, "decision_78": vars.decision_78,
                    "decision_79": vars.decision_79, "decision_80": vars.decision_80,
                    "decision_81": vars.decision_81, "decision_82": vars.decision_82, "decision_83": vars.decision_83,
                    "decision_84": vars.decision_84, "decision_85": vars.decision_85,
                    "decision_86": vars.decision_86, "decision_87": vars.decision_87, "decision_88": vars.decision_88,
                    "decision_89": vars.decision_89, "decision_90": vars.decision_90,
                    "decision_91": vars.decision_91, "decision_92": vars.decision_92, "decision_93": vars.decision_93,
                    "decision_94": vars.decision_94, "decision_95": vars.decision_95,
                    "decision_96": vars.decision_96, "decision_97": vars.decision_97, "decision_98": vars.decision_98,
                    "decision_99": vars.decision_99
                    }
    save = dumps(account_data)
    if vars.profile_name != "":
        with open("profiles/" + vars.profile_name + ".json", "w") as save_file:
            save_file.write(save)
    with open("profile_list.json", "r") as file:
        profile_list = load(file)
    if vars.profile_name not in profile_list["profiles"]:
        profile_list["profiles"].append(vars.profile_name)
    save = dumps(profile_list)
    with open("profile_list.json", "w") as file:
        file.write(save)


def enter_key_pressed():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("enter pressed")
                return True


if __name__ == "__main__":
    raise Exception

pygame.init()
