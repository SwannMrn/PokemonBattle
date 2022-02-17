import random
import csv

chart = []
with open("resources/CSV/pokedex.csv") as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)

chart2 = []
with open("resources/CSV/pok_moves.csv") as f2:
    c2 = csv.DictReader(f2, delimiter=',')
    for line2 in c2:
        chart2.append(line2)

chart3 = []
with open("resources/CSV/pok_type_chart.csv") as f3:
    c3 = csv.DictReader(f3, delimiter=',')
    for line3 in c3:
        chart3.append(line3)


def pok_index(pokemon: str) -> int:
    """takes a pokemon's name and returns his index number"""
    file = open("resources/CSV/pokedex.csv", "r")
    c1 = csv.DictReader(file, delimiter=',')
    for li in c1:
        if li['Pokemon'] == pokemon:
            pok_nbr = int(li['Number'])-1
    return pok_nbr


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


def types(pokemon: str) -> list:
    """takes a pokemon string and returns his type(s)"""
    l = []
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


def type_coef(pokemon: str, type: int)-> int:
    pok_types = types(pokemon)
    type1 = pok_types[type]
    if type1 == 'Bug':
        coef = 0
    elif type1 == 'Dark':
        coef = 1
    elif type1 == 'Dragon':
        coef = 2
    elif type1 == 'Electric':
        coef = 3
    elif type1 == 'Fairy':
        coef = 4
    elif type1 == 'Fighting':
        coef = 5
    elif type1 == 'Fire':
        coef = 6
    elif type1 == 'Flying':
        coef = 7
    elif type1 == 'Ghost':
        coef = 8
    elif type1 == 'Grass':
        coef = 9
    elif type1 == 'Ground':
        coef = 10
    elif type1 == 'Ice':
        coef = 11
    elif type1 == 'Normal':
        coef = 12
    elif type1 == 'Poison':
        coef = 13
    elif type1 == 'Psychic':
        coef = 14
    elif type1 == 'Rock':
        coef = 15
    elif type1 == 'Steel':
        coef = 16
    elif type1 == 'Water':
        coef = 17
    return coef


def attacks(pokemon: str)-> list:
    """takes a pokemon's name and returns his 4 attacks, depending on his type"""
    move_list = []
    pok_types = types(pokemon)
    if len(pok_types) == 1:
        coef1 = type_coef(pokemon, 0)
        for x in range(4):
            nbr1 = (4 * coef1) + x
            move = chart2[nbr1]['Name']
            move_list.append(move)
    elif len(pok_types) == 2:
        coef1 = type_coef(pokemon, 0)
        coef2 = type_coef(pokemon, 1)
        for y in range(2):
            nbr1 = (4 * coef1) + y
            nbr2 = (4 * coef2) + y
            move = chart2[nbr1]['Name']
            move2 = chart2[nbr2]['Name']
            move_list.append(move)
            move_list.append(move2)
    return move_list


def power(move: str)-> int:
    power = 0
    for line5 in range(len(chart2)):
        if chart2[line5]['Name'] == move:
            power = int(chart2[line5]['Power'])
    return power


def effect(move: str)-> int:
    for line5 in range(len(chart2)):
        if chart2[line5]['Name'] == move:
            move_effect = chart2[line5]['Effect']
    return move_effect


def effectdesc(move: str)-> int:
    for line5 in range(len(chart2)):
        if chart2[line5]['Name'] == move:
            effectdesc = chart2[line5]['EffectDesc']
    return effectdesc


def accuracy(move: str)-> int:
    for line5 in range(len(chart2)):
        if chart2[line5]['Name'] == move:
            moveaccuracy = int(chart2[line5]['Accuracy'])
    return moveaccuracy


def effectprob(move: str)-> int:
    for line5 in range(len(chart2)):
        if chart2[line5]['Name'] == move:
            effectprob = chart2[line5]['EffectProb']
    return effectprob


def dmg(pokemon: str, move: str) -> int:
    """takes a pokemon string and returns his raw damage (float)"""
    pokemon_nbr = pok_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    pwr = power(move)
    dmg = (atk + pwr) // 13 + random.randint(0, 4)
    return dmg


def type_weak_or_strong(pok1: str, pok2: str):
    """takes a pokemon string and returns his attack"""
    pok1_type = types(pok1)[0]
    pok2_type = types(pok2)[0]
    li1 = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']
    for y in range(18):
        if pok1_type == li1[y]:
            pok1ind = y
    pok1_coef = float(chart3[pok1ind][pok2_type])
    return pok1_coef


def pokemon_list():
    poklist = []
    for x in range(len(chart)):
        poklist.append(chart[x]['Pokemon'])
    return poklist
