import sys
import os
import random
import time
import numpy as np

current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
sys.path.append(current_directory)
import pokedex as pok

# delay printing (like in pokemon games)
def delay_print(s: str):
    # prints one char at a time
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


class Pokemon:
    def __init__(self, name, health='===================='):
        # save variables as attributes
        self.name = name
        self.type = pok.types(name)[0]
        self.moves = pok.attacks(name)
        self.attack = pok.atk(name)
        self.defense = pok.defense(name)
        self.speed = pok.speed(name)
        self.health = health
        self.HP = pok.HP(name)
        self.bars = 20  # amount of health bars

    def print_stats(self):
        print(f"Name: {self.name}\nType: {self.type}\nMoves: {self.moves}\nAtk: {self.attack}\nDef: {self.defense}\nSpeed: {self.speed}\nHealth: {self.health}")

    def fight(self, Pokemon2):
        # Two pokemon fight each other
        # Print info on fight
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print(self.type, "TYPE")
        print(self.HP, " | HP")
        print(self.attack, " | ATTACK")
        print(self.defense, " | DEFENSE")
        print(self.speed, " | SPEED")
        print("\n-----VS-----")
        print(f"\n{Pokemon2.name}")
        print(Pokemon2.type, "TYPE")
        print(Pokemon2.HP, " | HP")
        print(Pokemon2.attack, " | ATTACK")
        print(Pokemon2.defense, " | DEFENSE")
        print(Pokemon2.speed, " | SPEED")

        time.sleep(2)

        # type advantages
        coeff = pok.type_weak_or_strong(self.name, Pokemon2.name)
        # if pokemon2 type normal effectiveness
        if coeff == 1:
            str1_atk = "...\n"
            str2_atk = "...\n"

        # Pokemon2 type > pokemon type
        if coeff == 0.5:
            Pokemon2.attack *= 2
            Pokemon2.defense *= 2
            self.attack /= 2
            self.defense /= 2
            str1_atk = "It's not very effective...\n"
            str2_atk = "It's super effective!\n"

        # Pokemon 2 type < pokemon type
        if coeff == 2:
            self.attack *= 2
            self.defense *= 2
            Pokemon2.attack /= 2
            Pokemon2.defense /= 2
            str1_atk = "It's super effective!\n"
            str2_atk = "It's not very effective...\n"

        # fighting loop (while pokemons have health)
        turn = 0
        while (self.bars > 0) and (Pokemon2.bars > 0):
            turn += 1
            print(f"-----------Turn {turn}------------\n")
            # print the health of each pokemon
            print(f"{self.health}\tHP\t{self.name}\n")
            print(f"{Pokemon2.health}\tHP\t{Pokemon2.name}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Pick a move. >>> "))
            cur_move = self.moves[index-1]
            delay_print(f"{self.name} used {cur_move}!\n")
            time.sleep(0.5)
            delay_print(str1_atk)

            # dmg calculation
            dmg = pok.dmg(self.name, self)
            Pokemon2.HP -= dmg
            Pokemon2.bars -= round(dmg/(Pokemon2.HP/20))
            Pokemon2.health = ""

            # add health back and def
            for j in range(int(Pokemon2.bars)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"{self.health}\tHP\t{self.name}\n")
            print(f"{Pokemon2.health}\tHP\t{Pokemon2.name}\n")
            time.sleep(0.5)

            # Check if pokemon alive
            money = np.random.choice(5000)
            if Pokemon2.bars <= 0:
                delay_print("\n... " + Pokemon2.name + f" fainted.  Opponent paid you ₱{money}.")
                break

            if self.bars <= 0:
                delay_print("\n... " + self.name + f" fainted.  Opponent paid you ₱{money}.")

            # Pokemon2 turn
            print(f"Go {Pokemon2.name}!")
            index = random.randint(1, 4)
            cur_move = Pokemon2.moves[index - 1]
            delay_print(f"{Pokemon2.name} used {cur_move}!\n")
            time.sleep(1)
            delay_print(str2_atk)

            # dmg calculation
            dmg = pok.dmg(self.name, self)
            self.HP -= dmg
            self.bars -= round(dmg/(self.HP/20))
            self.health = ""

            # add health back and def
            for j in range(int(self.bars)):
                self.health += "="

            time.sleep(1)
            print(f"{self.health}\tHP\t{self.name}\n")
            print(f"{Pokemon2.health}\tHP\t{Pokemon2.name}\n")
            time.sleep(0.5)

            # Check if pokemon alive
            if Pokemon2.bars <= 0:
                delay_print("\n... " + Pokemon2.name + f" fainted.  Opponent paid you ₱{money}.\n")
                break

            if self.bars <= 0:
                delay_print("\n... " + self.name + f" fainted.  You paid the opponent ₱{money}.\n")



lis1 = pok.pokemon_list()
apok1 = input("Choose your pokemon! (names only, uppercase at the beginning) >>> ")
apok2 = random.choice(lis1)

Pokemon.fight(Pokemon(apok1), Pokemon(apok2))

