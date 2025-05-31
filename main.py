"""The main file which contains the storyline and calls all the functions."""

import variables as v
from cp0 import checkpoint_0
from cp1 import checkpoint_1
from cp2 import checkpoint_2
from cp3 import checkpoint_3
from cp4 import checkpoint_4
from cp5 import checkpoint_5
from cp6 import checkpoint_6
from cp7 import checkpoint_7
from cp8 import checkpoint_8
from cp9 import checkpoint_9
from cp10 import checkpoint_10
from cp11 import checkpoint_11
from cp12 import checkpoint_12
from cp13 import checkpoint_13
from cp14 import checkpoint_14
from cp15 import checkpoint_15
from cp16 import checkpoint_16
from cp17 import checkpoint_17
from cp18 import checkpoint_18
from functions import *

if __name__ != "__main__":
    raise Exception

v.background = "mountain"
consts.screen.fill(consts.BLACK)
surf = pygame.image.load(f"./images/{v.background}.jpg").convert()
consts.screen.blit(surf, surf.get_rect())
decision_1 = story("Welcome to The Warlock of Firetop Mountain.\nWould you like to create a NEW account or LOAD an"
                   " existing one?")
if decision_1 == "NEW":
    while True:
        v.profile_name = story("What would you like to call it?", any_input=True).lower()
        with open("profile_list.json", "r") as file:
            profile_list = load(file)
        if v.profile_name in profile_list:
            story("That account already exists.")
        else:
            v.checkpoint = 0
            break
elif decision_1 == "LOAD":
    with open("profile_list.json", "r") as file:
        profile_list = load(file)
    while True:
        account = story("Which account would you like to use?", any_input=True).lower()
        if account in profile_list["profiles"]:
            with open("profiles/" + account + ".json", "r") as file:
                user_data = load(file)
            v.gold = user_data["gold"]
            v.provs = user_data["provs"]
            v.hero = user_data["hero"]
            v.init_hero = user_data["init_hero"]
            v.equipment = user_data["equipment"]
            v.river = user_data["river"]
            v.piranhas = user_data["piranhas"]
            v.fight_tuto_done = user_data["fight_tuto_done"]
            v.provs_tuto_done = user_data["provs_tuto_done"]
            v.checkpoint = user_data["checkpoint"]
            v.profile_name = user_data["profile_name"]
            v.decision_1 = user_data["decision_1"]
            v.decision_2 = user_data["decision_2"]
            v.decision_3 = user_data["decision_3"]
            v.decision_4 = user_data["decision_4"]
            v.decision_5 = user_data["decision_5"]
            v.decision_6 = user_data["decision_6"]
            v.decision_7 = user_data["decision_7"]
            v.decision_8 = user_data["decision_8"]
            v.decision_9 = user_data["decision_9"]
            v.decision_10 = user_data["decision_10"]
            v.decision_11 = user_data["decision_11"]
            v.decision_12 = user_data["decision_12"]
            v.decision_13 = user_data["decision_13"]
            v.decision_14 = user_data["decision_14"]
            v.decision_15 = user_data["decision_15"]
            v.decision_16 = user_data["decision_16"]
            v.decision_17 = user_data["decision_17"]
            v.decision_18 = user_data["decision_18"]
            v.decision_19 = user_data["decision_19"]
            v.decision_10 = user_data["decision_20"]
            v.decision_11 = user_data["decision_21"]
            v.decision_12 = user_data["decision_22"]
            v.decision_13 = user_data["decision_23"]
            v.decision_14 = user_data["decision_24"]
            v.decision_15 = user_data["decision_25"]
            v.decision_16 = user_data["decision_26"]
            v.decision_17 = user_data["decision_27"]
            v.decision_18 = user_data["decision_28"]
            v.decision_19 = user_data["decision_29"]
            v.decision_10 = user_data["decision_30"]
            v.decision_11 = user_data["decision_31"]
            v.decision_12 = user_data["decision_32"]
            v.decision_13 = user_data["decision_33"]
            v.decision_14 = user_data["decision_34"]
            v.decision_15 = user_data["decision_35"]
            v.decision_16 = user_data["decision_36"]
            v.decision_17 = user_data["decision_37"]
            v.decision_18 = user_data["decision_38"]
            v.decision_19 = user_data["decision_39"]
            v.decision_10 = user_data["decision_40"]
            v.decision_11 = user_data["decision_41"]
            v.decision_12 = user_data["decision_42"]
            v.decision_13 = user_data["decision_43"]
            v.decision_14 = user_data["decision_44"]
            v.decision_15 = user_data["decision_45"]
            v.decision_16 = user_data["decision_46"]
            v.decision_17 = user_data["decision_47"]
            v.decision_18 = user_data["decision_48"]
            v.decision_19 = user_data["decision_49"]
            v.decision_10 = user_data["decision_50"]
            v.decision_11 = user_data["decision_51"]
            v.decision_12 = user_data["decision_52"]
            v.decision_13 = user_data["decision_53"]
            v.decision_14 = user_data["decision_54"]
            v.decision_15 = user_data["decision_55"]
            v.decision_16 = user_data["decision_56"]
            v.decision_17 = user_data["decision_57"]
            v.decision_18 = user_data["decision_58"]
            v.decision_19 = user_data["decision_59"]
            v.decision_10 = user_data["decision_60"]
            v.decision_11 = user_data["decision_61"]
            v.decision_12 = user_data["decision_62"]
            v.decision_13 = user_data["decision_63"]
            v.decision_14 = user_data["decision_64"]
            v.decision_15 = user_data["decision_65"]
            v.decision_16 = user_data["decision_66"]
            v.decision_17 = user_data["decision_67"]
            v.decision_18 = user_data["decision_68"]
            v.decision_19 = user_data["decision_69"]
            v.decision_10 = user_data["decision_70"]
            v.decision_11 = user_data["decision_71"]
            v.decision_12 = user_data["decision_72"]
            v.decision_13 = user_data["decision_73"]
            v.decision_14 = user_data["decision_74"]
            v.decision_15 = user_data["decision_75"]
            v.decision_16 = user_data["decision_76"]
            v.decision_17 = user_data["decision_77"]
            v.decision_18 = user_data["decision_78"]
            v.decision_19 = user_data["decision_79"]
            v.decision_10 = user_data["decision_80"]
            v.decision_11 = user_data["decision_81"]
            v.decision_12 = user_data["decision_82"]
            v.decision_13 = user_data["decision_83"]
            v.decision_14 = user_data["decision_84"]
            v.decision_15 = user_data["decision_85"]
            v.decision_16 = user_data["decision_86"]
            v.decision_17 = user_data["decision_87"]
            v.decision_18 = user_data["decision_88"]
            v.decision_19 = user_data["decision_89"]
            v.decision_10 = user_data["decision_90"]
            v.decision_11 = user_data["decision_91"]
            v.decision_12 = user_data["decision_92"]
            v.decision_13 = user_data["decision_93"]
            v.decision_14 = user_data["decision_94"]
            v.decision_15 = user_data["decision_95"]
            v.decision_16 = user_data["decision_96"]
            v.decision_17 = user_data["decision_97"]
            v.decision_18 = user_data["decision_98"]
            v.decision_19 = user_data["decision_99"]
            break
        else:
            story("That account doesn't exist.")
            
cp_funcs = {
    0: checkpoint_0,
    1: checkpoint_1,
    2: checkpoint_2,
    3: checkpoint_3,
    4: checkpoint_4,
    5: checkpoint_5,
    6: checkpoint_6,
    7: checkpoint_7,
    8: checkpoint_8,
    9: checkpoint_9,
    10: checkpoint_10,
    11: checkpoint_11,
    12: checkpoint_12,
    13: checkpoint_13,
    14: checkpoint_14,
    15: checkpoint_15,
    16: checkpoint_16,
    17: checkpoint_17,
    18: checkpoint_18
}

while True:
    cp_funcs[v.checkpoint]()

# add animations when changing stats
# add sound
# add more images
# remove text box
# make shield work
# get rid of items with spaces
# cyclops photo
# remove items looking at wood cp10
# roll 2 dice not 1 for initial stamina
# remove item after vampire
