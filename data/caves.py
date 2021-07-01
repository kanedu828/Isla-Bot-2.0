import random
from enum import Enum
from copy import copy


class Drop(Enum):
    GOLD = 'gold'
    ITEM = 'item'
    EQUIPMENT = 'equipment'
    EXP = 'exp'


class Rarity(Enum):
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'


class Cave:
    _drops = [None, Rarity.COMMON, Rarity.RARE, Rarity.EPIC, Rarity.LEGENDARY]

    _caves = [
        {
            'name': 'Developer Cave',
            'level_requirement': 1,
            'exp': 100,
            'drop_odds': [0, 1, 0, 0, 0],
            Rarity.COMMON: [(Drop.EQUIPMENT, 1000)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1100)],
            'current_quantity': 0,
            'max_quantity': 0,
        },
        {
            'name': 'Beginner Cave',
            'level_requirement': 1,
            'exp': 1,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1100)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Amateur Cave',
            'level_requirement': 5,
            'exp': 4,
            'drop_odds': [0.2, 0.4, 0.3, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Dark Cave',
            'level_requirement': 10,
            'exp': 10,
            'drop_odds': [0.85, 0.10, 0.03, 0.01, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 1), (Drop.EXP, 5)],
            Rarity.RARE: [(Drop.GOLD, 5), (Drop.EXP, 10)],
            Rarity.EPIC: [(Drop.GOLD, 150), (Drop.EQUIPMENT, 2100), (Drop.EQUIPMENT, 5100), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [
                (Drop.GOLD, 200),
                (Drop.EQUIPMENT, 1300),
                (Drop.EQUIPMENT, 6100),
                (Drop.EQUIPMENT, 3100),
                (Drop.EQUIPMENT, 4100)
            ],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Talisman Cave',
            'level_requirement': 10,
            'exp': 10,
            'drop_odds': [0.85, 0.10, 0.03, 0.01, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 15), (Drop.EXP, 15)],
            Rarity.RARE: [(Drop.GOLD, 100), (Drop.EXP, 100)],
            Rarity.EPIC: [(Drop.GOLD, 600), (Drop.EXP, 150), (Drop.EQUIPMENT, 1400), (Drop.EQUIPMENT, 1300)],
            Rarity.LEGENDARY: [(Drop.GOLD, 1000), (Drop.EXP, 200), (Drop.EQUIPMENT, 6300), (Drop.EQUIPMENT, 1400)],
            'current_quantity': 100,
            'max_quantity': 100,
        },
        {
            'name': 'Bogdan Cave',
            'level_requirement': 13,
            'exp': 6,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.GOLD, 3)],
            Rarity.RARE: [(Drop.GOLD, 8)],
            Rarity.EPIC: [(Drop.GOLD, 40)],
            Rarity.LEGENDARY: [(Drop.GOLD, 300), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Ice Cave',
            'level_requirement': 20,
            'exp': 8,
            'drop_odds': [0.4, 0.3, 0.20, 0.095, 0.005],
            Rarity.COMMON: [(Drop.GOLD, 5)],
            Rarity.RARE: [(Drop.GOLD, 13)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Ice Cave 2',
            'level_requirement': 25,
            'exp': 10,
            'drop_odds': [0.4, 0.3, 0.285, 0.01, 0.005],
            Rarity.COMMON: [(Drop.GOLD, 5)],
            Rarity.RARE: [(Drop.GOLD, 13)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 6200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200), (Drop.EQUIPMENT, 1400)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Beetle Cave',
            'level_requirement': 30,
            'exp': 15,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.EXP, 5)],
            Rarity.RARE: [(Drop.GOLD, 12)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200), (Drop.EQUIPMENT, 3200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Lillard Cave',
            'level_requirement': 50,
            'exp': 30,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.EXP, 7)],
            Rarity.RARE: [(Drop.GOLD, 14)],
            Rarity.EPIC: [(Drop.GOLD, 75)],
            Rarity.LEGENDARY: [(Drop.GOLD, 605), (Drop.EQUIPMENT, 5200), (Drop.EQUIPMENT, 4200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Ender Cave',
            'level_requirement': 100,
            'exp': 1200,
            'drop_odds': [0.4, 0.3, 0.20, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 300)],
            Rarity.RARE: [(Drop.GOLD, 500)],
            Rarity.EPIC: [(Drop.GOLD, 1000)],
            Rarity.LEGENDARY: [(Drop.GOLD, 5000), (Drop.EQUIPMENT, 2200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
    ]

    def __init__(self, cave):
        self.cave = cave

    @classmethod
    def from_cave_name(cls, cave_name: str):
        for cave in Cave._caves:
            if cave['name'] == cave_name:
                return cls(cave)
        return None

    def mine_cave(self, luck=0):
        '''
            Returns a two tuple of the drop.
            (DropType, DropValue)
            or
            (None, None)
        '''
        if self.cave['current_quantity'] > 0:
            self.cave['current_quantity'] -= 1
        elif self.cave['current_quantity'] == 0:
            return (None, None)
        drop_odds = copy(self.cave['drop_odds'])
        drop_odds[4] += luck / 10000
        drop_odds[3] += luck / 10000
        drop_quality = random.choices(Cave._drops, drop_odds)[0]
        if drop_quality:
            drop = random.choice(self.cave[drop_quality])
            return drop
        else:
            return (None, None)

    @staticmethod
    def populate_caves():
        for cave in Cave._caves:
            cave['current_quantity'] = cave['max_quantity']

    @staticmethod
    def set_cave_quantity(cave_name: str, quantity: int):
        for cave in Cave._caves:
            if cave['name'].lower() == cave_name.lower():
                quantity = min(cave['max_quantity'], int(quantity))
                cave['current_quantity'] = quantity
                return True
        return False

    @staticmethod
    def list_caves_by_level(level=0):
        '''
            Returns a formatted string of all the caves that meet the level requirement.
        '''
        sorted_caves = sorted(Cave._caves, key=lambda cave: cave['level_requirement'])
        sorted_caves = filter(lambda cave: cave['level_requirement'] <= level, sorted_caves)
        caves_list = [
            f'`{cave["name"]}` **Level Requirement:** `{cave["level_requirement"]}`'
            for cave
            in sorted_caves
            if not cave['current_quantity'] == 0
        ]
        return caves_list

    @staticmethod
    def verify_cave(cave_name: str):
        for cave in Cave._caves:
            if cave['name'] == cave_name:
                return True
        return False
