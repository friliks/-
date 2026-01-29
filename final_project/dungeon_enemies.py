#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *

dungeon_monsters = [
    'Гоблин-берсерк', 'Гном-землекоп', 'Пещерный скорпион', 
    'Могильный ходяч', 'Скелет-легионер', 'Пират глубин',
    'Фантом тьмы', 'Скелет-стрелок', 'Гоблин-карманщик',
    'Протоплазменная глыба', 'Каменный колосс', 'ПОВЕЛИТЕЛЬ БЕЗДНЫ'
]

class DungeonCreature:
    def __init__(self, creature_level, current_chamber):
        self.name = ''
        self.max_hp = 0
        self.current_hp = 0
        self.brutality = 0
        self.nimbleness = 0
        self.defence = 0
        self.depth_level = creature_level
        self.chamber_number = current_chamber
        self.knowledge_gain = 0
        self.wealth_drop = 0

    def determine_creature_type(self):
        fate_roll = randint(0, 100)

        if 0 <= fate_roll < 10:
            self.name = "Гоблин-берсерк"
            self.max_hp = 32
            self.brutality = 7
            self.nimbleness = 2
            self.defence = 2

        elif 10 <= fate_roll < 20:
            self.name = "Гном-землекоп"
            self.max_hp = 31
            self.brutality = 5
            self.nimbleness = 3
            self.defence = 2

        elif 20 <= fate_roll < 30:
            self.name = "Пещерный скорпион"
            self.max_hp = 20
            self.brutality = 5
            self.nimbleness = 7
            self.defence = 1

        elif 30 <= fate_roll < 40:
            self.name = "Могильный ходяч"
            self.max_hp = 28
            self.brutality = 5
            self.nimbleness = 1
            self.defence = 3

        elif 40 <= fate_roll < 50:
            self.name = "Скелет-легионер"
            self.max_hp = 24
            self.brutality = 7
            self.nimbleness = 2
            self.defence = 2

        elif 50 <= fate_roll < 60:
            self.name = "Пират глубин"
            self.max_hp = 28
            self.brutality = 9
            self.nimbleness = 4
            self.defence = 2

        elif 60 <= fate_roll < 70:
            self.name = "Фантом тьмы"
            self.max_hp = 38
            self.brutality = 5
            self.nimbleness = 4
            self.defence = 1

        elif 70 <= fate_roll < 80:
            self.name = "Скелет-стрелок"
            self.max_hp = 26
            self.brutality = 6
            self.nimbleness = 4
            self.defence = 1

        elif 80 <= fate_roll < 90:
            self.name = "Гоблин-карманщик"
            self.max_hp = 18
            self.brutality = 7
            self.nimbleness = 2
            self.defence = 3

        elif 90 <= fate_roll < 95:
            self.name = "Протоплазменная глыба"
            self.max_hp = 46
            self.brutality = 12
            self.nimbleness = 3
            self.defence = 4

        elif 95 <= fate_roll < 98:
            self.name = "Каменный колосс"
            self.max_hp = 79
            self.brutality = 13
            self.nimbleness = 1
            self.defence = 4

        else:
            self.name = "ПОВЕЛИТЕЛЬ БЕЗДНЫ"
            self.max_hp = 120
            self.brutality = 8
            self.nimbleness = 2
            self.defence = 7

        self.current_hp = self.max_hp
    
    def adjust_to_depths(self):
        self.determine_creature_type()

        # Адаптация к пройденным комнатам
        for _ in range(1):
            for _ in range(self.chamber_number):
                adaptation = randint(1, 4)

                if adaptation == 1:
                    self.max_hp += 2
                    self.current_hp += 2
                elif adaptation == 2:
                    self.brutality += 1
                elif adaptation == 3:
                    # Меньше брони
                    if randint(1, 4) == 1:
                        self.defence += 1
                else:
                    self.nimbleness += 1

        # Адаптация к глубине подземелья
        for _ in range(self.depth_level - 1):
            self.max_hp += 3
            self.current_hp += 3
            self.brutality += 1
            # Убираем рост брони от глубины
            self.nimbleness += 1
            
    def display_creature_info(self):
        self.adjust_to_depths()
        self.calculate_creature_rewards()

        print('┌────────────────────────────────────┐')
        print('│        ОПАСНЫЙ ПРОТИВНИК           │')
        print('├────────────────────────────────────┤')
        print(f'│ Существо: {self.name:22} │')
        print('├────────────────────────────────────┤')
        print(f'│ Жизненная сила: {self.current_hp:3}/{self.max_hp:<3} │')
        print(f'│ Мощь удара:     {self.brutality:3}           │')
        print(f'│ Проворство:     {self.nimbleness:3}           │')
        print(f'│ Защита:         {self.defence:3}           │')
        print('└────────────────────────────────────┘')
        
        return (self.current_hp, self.max_hp, self.brutality, 
                self.nimbleness, self.defence, self.knowledge_gain, 
                self.wealth_drop)
    
    def calculate_creature_rewards(self):
        if self.name in dungeon_monsters[:9]:
            self.knowledge_gain = 5 * self.depth_level
            self.wealth_drop = 8
            if self.name == "Пират глубин":
                self.wealth_drop = 15
            elif self.name == "Гоблин-карманщик":
                self.wealth_drop = 15
        elif self.name in dungeon_monsters[9:10]:
            self.knowledge_gain = 15 * self.depth_level
            self.wealth_drop = 40
        elif self.name in dungeon_monsters[10:]:
            self.knowledge_gain = 30 * self.depth_level
            self.wealth_drop = 75
            if self.name == "ПОВЕЛИТЕЛЬ БЕЗДНЫ":
                self.wealth_drop = randint(75, 150)