import sys
from math import floor
from bisect import bisect
from values import Mainstats as main, Substats as sub, CharBuilds

###################################  Defining variables  ###################################

m_dict = {'hp' : main.hp, 'atk' : main.atk, 'hpp' : main.hpp,
             'atkp' : main.atkp, 'defp' : main.defp, 'em' : main.em,
             'er' : main.er, 'eled' : main.ele_dmg, 'phyd' : main.phy_dmg,
             'crit' : main.crit, 'cdmg' : main.cdmg, 'heal' : main.heal}

s_dict = {'hp' : sub.hp, 'atk' : sub.atk, 'def' : sub.defn,
            'hpp' : sub.hpp, 'atkp' : sub.atkp, 'defp' : sub.defp,
            'em' : sub.em, 'er' : sub.er, 'crit' : sub.crit, 'cdmg' : sub.cdmg}

STAT_STR = '\x1b[1;35;40m' + 'Stat:\t' + '\x1b[0m'
VAL_STR = '\x1b[1;34;40m' + 'Val:\t' + '\x1b[0m'

MAX_RATING = 3

#builds, character builds need to be imported from library
cust_stats = dict()
#only albedo is present since only albedo is defined in 'values.py'
builds = {'albedo':CharBuilds.albedo, 'custom':cust_stats}

###################################  Defining functions  ###################################

def main_stat(rarity, stat, val):
    """Calculates level of the artifact based on main stat."""
    index = rarity - 5

    arr = m_dict[stat]
    arr = arr[index]

    return bisect(arr, val)-1



def sub_stat(rarity, stat, val):
    """Calculates the number of times the substat was rolled while levelling up."""
    index = rarity - 5
    level = 0

    arr = s_dict[stat]
    arr = arr[index]

    while val > 0:
        #ind will contain index of stat if it is added to arr and sorted
        ind = bisect(arr, val) - 1
        if ind == -1:
            return level+1

        val -= arr[ind]
        level += 1

    return level



def input_cust():
    """Inputs custom values and updates the cust_stats accordingly."""
    print('\nInput custom build:')

    inp = input('Stats with weight 3 (comma separated):\t')
    inp_arr = inp.split(',')
    for i in inp_arr:
        cust_stats.update({i.strip(): 3})

    inp = input('Stats with weight 2 (comma separated):\t')
    inp_arr = inp.split(',')
    for i in inp_arr:
        cust_stats.update({i.strip(): 2})

    inp = input('Stats with weight 1 (comma separated):\t')
    inp_arr = inp.split(',')
    for i in inp_arr:
        cust_stats.update({i.strip(): 1})



def rate(m_stat, sub_dict, build, rarity):
    """Rates the artifact at L20 only."""
    if build == 'custom' and not bool(cust_stats):
        print("Error: Custom build empty.")
        return -1

    arr = builds[build]
    quality = 0

    for i, j in sub_dict.items():
        if i in arr.keys():
            quality += arr[i] * j


    #Main stat has more (8x) weightage than substats. Flower and Feather are exempt.
    count = 0
    for key in arr.keys():
        if arr[key] == MAX_RATING:
            count += 1

    if count < 2:
        divisor = 4*MAX_RATING + rarity*(MAX_RATING-1)

    #since only 1 possible max rating sub
    elif count == 2 and m_stat in arr.keys() and \
         arr[m_stat] == MAX_RATING:
        divisor = 4*MAX_RATING + rarity*(MAX_RATING-1)

    #since neither eled, phyd or heal can be substats
    elif count == 2 and 'eled' in arr.keys() and \
         arr['eled'] == MAX_RATING and m_stat != 'eled':
        divisor = 4*MAX_RATING + rarity*(MAX_RATING-1)

    elif count == 2 and 'phyd' in arr.keys() and \
         arr['phyd'] == MAX_RATING and m_stat != 'phyd':
        divisor = 4*MAX_RATING + rarity*(MAX_RATING-1)

    elif count == 2 and 'heal' in arr.keys() and \
         arr['heal'] == MAX_RATING and m_stat != 'heal':
        divisor = 4*MAX_RATING + rarity*(MAX_RATING-1)

    else:
        divisor = (4+rarity-1)*MAX_RATING

    #flower/feather
    if m_stat in ('atk', 'hp'):
        return quality*100/divisor

    quality += 32 * arr[m_stat] #32 = 8*4 (4 for max level of substat)
    return quality*100/(divisor + 32 * arr[m_stat])



def pred(rarity, m_stat, level, sub_dict, build):
    """Predicts all further rolls and then takes weighted mean based on the probability."""
    if floor(level/4) == rarity:
        rating = rate(m_stat, sub_dict, build, rarity)
        return rating

    if floor(level/4) < rarity: #predicts possible stats and weighs them based on probability
        rating  = 0
        temp_dict = sub_dict

        for i in temp_dict.keys():
            temp_dict[i] += 1
            rating += pred(rarity, m_stat, level+4, temp_dict, build)*0.25
            temp_dict[i] -= 1

        return rating

###################################  Taking input  ###################################

inp_rarity = int(input('Enter rarity: '))

inp_build = input('\nEnter build (character name or \'custom\'): ').lower()
if inp_build not in builds.keys():
    print('Error: Character build not defined.')
    sys.exit(0)

if inp_build == 'custom':
    input_cust()

print('\nEnter main stat and value'
      '(hp | atk | hpp | atkp | defp | em | er | phyd | eled | crit | cdmg | heal):')
m_stat = input(STAT_STR).lower()
m_val = float(input(VAL_STR))

print('\nEnter sub stats and value'
      '(hp | atk | def | hpp | atkp | defp | em | er | crit | cdmg):')
s_stat1 = input(STAT_STR).lower()
s_val1 = float(input(VAL_STR))

s_stat2 = input(STAT_STR).lower()
s_val2 = float(input(VAL_STR))

s_stat3 = input(STAT_STR).lower()
s_val3 = float(input(VAL_STR))

s_stat4 = input(STAT_STR).lower()
s_val4 = float(input(VAL_STR))

#inp_sub_dict will hold all the substats with their levels
inp_sub_dict = { s_stat1 : sub_stat(inp_rarity, s_stat1, s_val1),
             s_stat2 : sub_stat(inp_rarity, s_stat2, s_val2),
             s_stat3 : sub_stat(inp_rarity, s_stat3, s_val3),
             s_stat4 : sub_stat(inp_rarity, s_stat4, s_val4) }


## Print the build and substat level.
build_dict = builds[inp_build]
print('\nWeightage of substats:\t', build_dict)
print('Levels of substats:\t', inp_sub_dict)
##


out_rating = pred(inp_rarity,m_stat,
              main_stat(inp_rarity, m_stat, m_val)*4,
              inp_sub_dict, inp_build)

if out_rating > 66.7:
    RATING_STR = '\x1b[1;32;40m' + str(out_rating) + '\x1b[0m'
elif out_rating > 33.3:
    RATING_STR = '\x1b[1;33;40m' + str(out_rating) + '\x1b[0m'
else:
    RATING_STR = '\x1b[1;31;40m' + str(out_rating) + '\x1b[0m'
print('\nRating out of 100: ' ,RATING_STR)
