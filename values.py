'''
Artifact Rater for Genshin Impact
Copyright (C) 2021  "iamak21@protonmail.ch"

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

"Includes possible values of all stats and character builds."


class Mainstats:
    "Stores the values for all main stats"
    hp = [[717, 1530, 2342, 3155, 3967, 4780], [645, 1377, 2108, 2839, 3571]]
    atk = [[47, 100, 152, 205, 258, 311], [42, 90, 137, 185, 232]]

    hpp = [[7, 14.9, 22.8, 30.8, 38.7, 46.6], [6.3, 13.4, 20.6, 27.7, 34.8]]
    atkp = [[7, 14.9, 22.8, 30.8, 38.7, 46.6], [6.3, 13.4, 20.6, 27.7,
                                                34.8]]  #hp%
    defp = [[8.7, 18.6, 28.6, 38.5, 48.4, 58.3], [7.9, 16.8, 25.7, 34.6, 43.5]]
    em = [[28, 60, 91, 123, 155, 187], [25, 54, 82, 111, 139]]
    er = [[7.8, 16.6, 25.4, 34.2, 43.0, 51.8], [7.0, 14.9, 22.8, 30.8, 38.7]]

    ele_dmg = [[7, 14.9, 22.8, 30.8, 38.7, 46.6],
               [6.3, 13.4, 20.6, 27.7, 34.8]]  #hp%
    phy_dmg = [[8.7, 18.6, 28.6, 38.5, 48.4, 58.3],
               [7.9, 16.8, 25.7, 34.6, 43.5]]  #def%

    crit = [[4.7, 10, 15.4, 20.7, 26, 31.1], [4.2, 9, 13.7, 18.5, 23.2]]
    cdmg = [[9.3, 19.9, 30.5, 41.1, 51.6, 62.2], [8.4, 17.9, 27.4, 36.9, 46.4]]
    heal = [[5.4, 11.5, 17.6, 23.7, 29.8, 35.9], [4.8, 10.3, 15.8, 21.3, 26.8]]


class Substats:
    "Stores the values for all sub stats"
    hp = [[209, 239, 269, 299], [167, 191, 215, 239]]
    atk = [[14, 16, 18, 19], [11, 12, 14, 16]]
    defn = [[16, 19, 21, 23], [13, 15, 17, 19]]

    hpp = [[4.1, 4.7, 5.3, 5.8], [3.3, 3.7, 4.2, 4.7]]
    atkp = [[4.1, 4.7, 5.3, 5.8], [3.3, 3.7, 4.2, 4.7]]
    defp = [[5.1, 5.8, 6.6, 7.3], [4.1, 4.7, 5.3, 5.8]]

    em = [[16, 19, 21, 23], [13, 15, 17, 19]]
    er = [[4.5, 5.2, 5.8, 6.5], [3.6, 4.1, 4.7, 5.2]]
    crit = [[2.7, 3.1, 3.5, 3.9], [2.2, 2.5, 2.8, 3.1]]
    cdmg = [[5.4, 6.2, 7, 7.8], [4.4, 5, 5.6, 6.2]]


class CharBuilds:
    "Stores all the pre-defined character builds"

    albedo = {'defp': 3, 'crit': 2, 'cdmg': 2, 'def': 1, 'atkp': 1, 'atk': 1}
    #TODO:Other builds.
