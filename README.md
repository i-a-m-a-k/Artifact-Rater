# Artifact-Rater
This is a program to rate the different artifacts obtained in Genshin Impact.

# Stat shortforms
The stat shortforms used in the code (and expected as input) are:

| Shortform |         Stat        |
|-----------|---------------------|
|   atk     |       Attack        |
|   atkp    |       Attack%       |
|   hp      |          HP         |
|   hpp     |          HP%        |
|   def     |       Defense       |
|   defp    |       Defense%      |
|   crit    |       Crit Rate     |
|   cdmg    |       Crit Dmg      |
|   er      |   Energy Recharge   |
|   em      |  Elemental Mastery  |
|   eled    | Elemental Dmg Bonus |
|   phyd    | Physical Dmg Bonus  |
|   heal    |    Healing Bonus    |

# How to use
Save both the files in the same directory (since `values.py` is a module) and run `rate.py`.
You can use a pre-defnied build, define a build in `values.py` or define a custom build at runtime using `custom` build. Input the other values according to the artifacts.

# Example output
```
upload ) python rate.py
Enter rarity: 5

Enter build (character name or 'custom'): albedo

Enter main stat and value(hp | atk | hpp | atkp | defp | em | er | phyd | eled | crit | cdmg | heal):
Stat:   atk
Val:    311

Enter sub stats and value(hp | atk | def | hpp | atkp | defp | em | er | crit | cdmg):
Stat:   atkp
Val:    9.3
Stat:   defp
Val:    21.1
Stat:   cdmg
Val:    14.8
Stat:   em
Val:    16

Weightage of substats:   {'defp': 3, 'crit': 2, 'cdmg': 2, 'def': 1, 'atkp': 1, 'atk': 1}
Levels of substats:      {'atkp': 2, 'defp': 4, 'cdmg': 3, 'em': 1}

Rating out of 100:  90.9090909090909
```
