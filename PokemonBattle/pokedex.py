import random
import csv

chart = []
with open("resources/CSV/pokedex.csv") as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)


def pok_index(pokemon: str) -> int:
    """takes a pokemon name and returns his index number"""
    file = open("resources/CSV/pokedex.csv", "r")
    c1 = csv.DictReader(file, delimiter=',')
    for li in c1:
        if li['Pokemon'] == pokemon:
            pok_nbr2 = int(li['Number'])-1
    return pok_nbr2


def pok_check(pokemon: int):
    """Takes a pokemon index number, checks if it exists and returns a boolean"""
    pok_nbr = pokemon - 1
    if chart[pok_nbr]['Pokemon'] != '':
        pok_check = True
    else:
        pok_check = False
    return pok_check


def atk(pokemon: str) -> int:
    """takes a pokemon string and returns his attack"""
    pokemon_nbr = pok_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    return atk


def speed(pokemon: str) -> int:
    """takes a pokemon string and returns his speed"""
    pokemon_nbr = pok_index(pokemon)
    speed = int(chart[pokemon_nbr]['Speed'])
    return speed


def types(pokemon: str) -> int:
    """takes a pokemon string and returns his type(s)"""
    l []
    pokemon_nbr = pok_index(pokemon)
    type1 = chart[pokemon_nbr]['Type 1']
    l.append(type1)
    if chart[pokemon_nbr]['Type 2'] != '':
        type2 = chart[pokemon_nbr]['Type 2']
        l.append(type2)
    return l


def defense(pokemon: str) -> int:
    """takes a pokemon string and returns his defense"""
    pokemon_nbr = pok_index(pokemon)
    defense = int(chart[pokemon_nbr]['Defense'])
    return defense


def HP(pokemon: str) -> int:
    """takes a pokemon string and returns his HP"""
    pokemon_nbr = pok_index(pokemon)
    HP = int(chart[pokemon_nbr]['HP'])
    return HP


def sprite(pokemon: str) -> str:
    """takes a pokemon string and returns the link of his sprite png"""
    pokemon_nbr = pok_index(pokemon)
    sprite_url = str(chart[pokemon_nbr]['PNG'])
    return sprite_url


def raw_dmg(pokemon: str) -> float:
    """takes a pokemon string and returns his raw damage (float)"""
    pokemon_nbr = pok_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    defense = int(chart[pokemon_nbr]['Defense'])
    raw_dmg = ((2.5 * atk) // (defense // 5))
    return raw_dmg


def fastest_pok(pokemon1: str, pokemon2: str) -> str:
    """takes 2 pokemon strings and returns the fastest pokemon"""
    fastestpok = ''
    randlist = [pokemon1, pokemon2]
    pokemon1_nbr = pok_index(pokemon1)
    pokemon2_nbr = pok_index(pokemon2)
    atksp1 = int(chart[pokemon1_nbr]['Speed'])
    atksp2 = int(chart[pokemon2_nbr]['Speed'])
    if atksp1 > atksp2:
        fastestpok = pokemon1
    elif atksp1 == atksp2:
        fastestpok = random.choice(randlist)
    return fastestpok

print(types('Charizard'))
