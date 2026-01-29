#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import *
from dungeon_enemies import DungeonCreature

# Списки предметов
WEAPONS = ['Стальной клинок', 'Изогнутый кинжал', 'Дубовый лук', 'Острое копье', 'Тяжелая палица']
ARMOR = ['Пластинчатый доспех', 'Кольчужная рубаха', 'Укрепленная кожа']
CONSUMABLES = ['Флакон здоровья', 'Снадобье восстановления', 'Эликсир жизненных сил']

# Глобальный инвентарь
player_inventory = {'Оружие': '', 'Доспех': ''}
for slot in range(1, 6): 
    player_inventory[str(slot)] = ''

class Hero:
    def __init__(self):
        self.name = ""
        self.heritage = ""
        self.max_health = 0
        self.current_health = 0
        self.might = 0
        self.finesse = 0
        self.resilience = 0
        self.coins = 0
        self.dungeon_level = 1
        self.experience = 0
        self.exp_to_next = 5
        self.level = 1
        self.skill_points = 0
        self.stature = 0
        self.mass = 0
        self.chambers_cleared = 0

    def create_character(self):
        """Создание нового персонажа"""
        print("╔══════════════════════════════════════════╗")
        print("║          СОЗДАНИЕ ГЕРОЯ                 ║")
        print("╚══════════════════════════════════════════╝\n")
        
        self.name = input("Как зовут вашего искателя приключений?\n> ")
        
        print("\nВыберите ваше происхождение:")
        print("1. Человек (сбалансированный)")
        print("2. Лесной эльф (проворный)")
        print("3. Горный дворф (выносливый)")
        
        heritage_choice = input("\nВаш выбор (1-3): ")
        
        # Человек
        if heritage_choice == "1":
            self.heritage = "Человек"
            self.max_health = randint(85, 105)
            self.might = randint(7, 11)
            self.finesse = randint(6, 11)
            self.resilience = randint(2, 5)
            self.stature = randint(155, 205)
            self.mass = randint(65, 95)
            print(f"\n✓ {self.name}, Человек, готов к приключениям!")
        
        # Лесной эльф
        elif heritage_choice == "2":
            self.heritage = "Лесной эльф"
            self.max_health = randint(75, 95)
            self.might = randint(6, 10)
            self.finesse = randint(8, 14)
            self.resilience = randint(2, 4)
            self.stature = randint(180, 215)
            self.mass = randint(45, 75)
            print(f"\n✓ {self.name}, лесной эльф, чувствует зов приключений!")
        
        # Горный дворф
        elif heritage_choice == "3":
            self.heritage = "Горный дворф"
            self.max_health = randint(105, 135)
            self.might = randint(8, 13)
            self.finesse = randint(3, 7)
            self.resilience = randint(4, 7)
            self.stature = randint(105, 135)
            self.mass = randint(75, 105)
            print(f"\n✓ {self.name}, горный дворф, готов к тяжелым испытаниям!")
        
        else:
            print("Неверный выбор! Создаем человека по умолчанию.")
            self.heritage = "Человек"
            self.max_health = randint(85, 105)
            self.might = randint(7, 11)
            self.finesse = randint(6, 11)
            self.resilience = randint(2, 5)
            self.stature = randint(155, 205)
            self.mass = randint(65, 95)
        
        self.current_health = self.max_health
        
        # Стартовый подарок
        print(f"\n🎁 Вам вручают стартовое снаряжение!")
        if self.heritage == "Человек":
            player_inventory['Оружие'] = "Простой меч(+1)"
            print("Вы получаете: Простой меч(+1)")
        elif self.heritage == "Лесной эльф":
            player_inventory['Оружие'] = "Охотничий лук(+1)"
            print("Вы получаете: Охотничий лук(+1)")
        else:
            player_inventory['Доспех'] = "Горняцкая кираса(+1)"
            print("Вы получаете: Горняцкая кираса(+1)")
        
        input("\nНажмите Enter, чтобы начать путешествие...")
        self.display_character_sheet()

    def display_character_sheet(self):
        """Показывает характеристики героя"""
        print("\n" + "═" * 50)
        print("           ЛИЧНАЯ КАРТА ИСКАТЕЛЯ           ")
        print("═" * 50)
        print(f" 📛 Имя: {self.name}")
        print(f" 🏺 Происхождение: {self.heritage}")
        print("─" * 50)
        print(f" ⭐ Уровень: {self.level}")
        print(f" 📊 Опыт: {self.experience}/{self.exp_to_next}")
        print("─" * 50)
        print(f" ❤️  Здоровье: {self.current_health}/{self.max_health}")
        print(f" 💪 Сила: {self.might}")
        print(f" 🦅 Ловкость: {self.finesse}")
        print(f" 🛡️  Стойкость: {self.resilience}")
        print("─" * 50)
        print(f" 📏 Рост: {self.stature} см")
        print(f" ⚖️  Вес: {self.mass} кг")
        print(f" 💰 Богатство: {self.coins} золотых")
        print("═" * 50)

    def improve_attributes(self):
        """Прокачка характеристик"""
        while self.skill_points > 0:
            print(f"\nОчков улучшения: {self.skill_points}")
            print("Что желаете улучшить?")
            print("1. Жизненную силу (+15 HP)")
            print("2. Мышечную мощь (+2 силы)")
            print("3. Гибкость тела (+2 ловкости)")
            print("4. Крепость духа (+2 стойкости)")
            print("5. Завершить улучшения")
            
            choice = input("Ваш выбор: ")
            
            if choice == "1":
                self.max_health += 15
                self.current_health += 15
                self.skill_points -= 1
                print("✓ Жизненная сила увеличена!")
            
            elif choice == "2":
                self.might += 2
                self.skill_points -= 1
                print("✓ Мышечная мощь усилена!")
            
            elif choice == "3":
                self.finesse += 2
                self.skill_points -= 1
                print("✓ Гибкость тела улучшена!")
            
            elif choice == "4":
                self.resilience += 2
                self.skill_points -= 1
                print("✓ Крепость духа укреплена!")
            
            elif choice == "5":
                break
            
            else:
                print("Неверный выбор!")

    def check_inventory(self):
        """Показывает инвентарь"""
        print("\n" + "═" * 50)
        print("             СУМКА ПУТЕШЕСТВЕННИКА          ")
        print("═" * 50)
        print(f" ⚔️  Вооружение: {player_inventory['Оружие'] or 'Нет'}")
        print(f" 🛡️  Защита: {player_inventory['Доспех'] or 'Нет'}")
        print(f" 💰 Сокровища: {self.coins} золотых")
        print("─" * 50)
        print(" 📦 Содержимое сумки:")
        
        empty_slots = 0
        for i in range(1, 6):
            item = player_inventory[str(i)]
            if not item:
                empty_slots += 1
                print(f"   {i}. [Пустая ячейка]")
            else:
                print(f"   {i}. {item}")
        
        print(f"\n 📍 Свободного места: {empty_slots}/5")
        print("═" * 50)

    def store_item(self, item_to_store):
        """Добавляет предмет в инвентарь"""
        for i in range(1, 6):
            if not player_inventory[str(i)]:
                player_inventory[str(i)] = item_to_store
                print(f"✓ Предмет добавлен: {item_to_store}")
                return True
        
        print("⚠️  Сумка переполнена!")
        print("1. Выбросить что-то")
        print("2. Оставить предмет")
        
        choice = input("Ваше решение: ")
        if choice == "1":
            print("\nЧто выбросить?")
            for j in range(1, 6):
                print(f"{j}. {player_inventory[str(j)] or '[Пусто]'}")
            
            try:
                slot = input("Номер ячейки: ")
                if player_inventory[slot]:
                    print(f"Выброшено: {player_inventory[slot]}")
                    player_inventory[slot] = item_to_store
                    return True
            except:
                pass
        
        return False

    def manage_gear(self):
        """Управление экипировкой и предметами"""
        print("\n" + "─" * 40)
        print("        УПРАВЛЕНИЕ СНАРЯЖЕНИЕМ        ")
        print("─" * 40)
        
        # Проверяем наличие предметов
        has_items = any(player_inventory[str(i)] for i in range(1, 6))
        
        if not has_items:
            print("Ваша сумка пуста.")
            input("\nНажмите Enter...")
            return
        
        # Показываем предметы
        print("Ваши предметы:")
        for i in range(1, 6):
            item = player_inventory[str(i)]
            if item:
                print(f"{i}. {item}")
        
        print("0. Вернуться назад")
        
        try:
            selection = int(input("\nВыберите предмет: "))
            if selection == 0:
                return
            
            selected_item = player_inventory[str(selection)]
            if not selected_item:
                print("В этой ячейке ничего нет!")
                return
            
            print(f"\nПредмет: {selected_item}")
            
            # Оружие
            if any(weapon in selected_item for weapon in WEAPONS):
                print("1. Вооружиться")
                print("2. Выбросить")
                print("3. Оставить")
                
                action = input("Действие: ")
                
                if action == "1":
                    # Снимаем старое оружие
                    if player_inventory['Оружие']:
                        self.remove_gear_bonuses(player_inventory['Оружие'])
                    
                    player_inventory['Оружие'] = selected_item
                    self.apply_gear_bonuses(selected_item)
                    player_inventory[str(selection)] = ''
                    print(f"✓ Вооружен: {selected_item}")
                
                elif action == "2":
                    player_inventory[str(selection)] = ''
                    print("✓ Предмет выброшен")
            
            # Броня
            elif any(armor in selected_item for armor in ARMOR):
                print("1. Надеть")
                print("2. Выбросить")
                print("3. Оставить")
                
                action = input("Действие: ")
                
                if action == "1":
                    # Снимаем старую броню
                    if player_inventory['Доспех']:
                        self.remove_gear_bonuses(player_inventory['Доспех'])
                    
                    player_inventory['Доспех'] = selected_item
                    self.apply_gear_bonuses(selected_item)
                    player_inventory[str(selection)] = ''
                    print(f"✓ Облачен в: {selected_item}")
                
                elif action == "2":
                    player_inventory[str(selection)] = ''
                    print("✓ Предмет выброшен")
            
            # Расходники
            elif selected_item in CONSUMABLES:
                print("1. Использовать")
                print("2. Выбросить")
                print("3. Оставить")
                
                action = input("Действие: ")
                
                if action == "1":
                    if selected_item == 'Флакон здоровья':
                        heal = 15
                    elif selected_item == 'Снадобье восстановления':
                        heal = 40
                    else:  # Эликсир жизненных сил
                        heal = 85
                    
                    old_health = self.current_health
                    self.current_health = min(self.max_health, self.current_health + heal)
                    healed = self.current_health - old_health
                    
                    print(f"✓ Восстановлено {healed} HP!")
                    player_inventory[str(selection)] = ''
                
                elif action == "2":
                    player_inventory[str(selection)] = ''
                    print("✓ Предмет выброшен")
        
        except:
            print("Ошибка в выборе!")

    def apply_gear_bonuses(self, gear_item):
        """Применяет бонусы от экипировки"""
        bonus = self.extract_enhancement(gear_item)
        
        if 'клинок' in gear_item.lower() or 'меч' in gear_item.lower():
            self.might += 3 + (bonus * 2)
        elif 'кинжал' in gear_item.lower():
            self.might += 1 + (bonus * 2)
            self.finesse += 2 + (bonus * 2)
        elif 'лук' in gear_item.lower():
            self.finesse += 3 + (bonus * 2)
        elif 'копье' in gear_item.lower():
            self.might += 2 + (bonus * 2)
            self.resilience += 1 + (bonus * 2)
        elif 'палица' in gear_item.lower():
            self.finesse += 1 + (bonus * 2)
            self.resilience += 2 + (bonus * 2)
        elif 'доспех' in gear_item.lower() or 'кираса' in gear_item.lower():
            self.resilience += 5 + bonus
        elif 'рубаха' in gear_item.lower():
            self.resilience += 3 + bonus
            self.finesse += 1 + bonus
        elif 'кожа' in gear_item.lower():
            self.resilience += 2 + bonus
            self.finesse += 3 + bonus

    def remove_gear_bonuses(self, gear_item):
        """Снимает бонусы от экипировки"""
        bonus = self.extract_enhancement(gear_item)
        
        if 'клинок' in gear_item.lower() or 'меч' in gear_item.lower():
            self.might -= 3 + (bonus * 2)
        elif 'кинжал' in gear_item.lower():
            self.might -= 1 + (bonus * 2)
            self.finesse -= 2 + (bonus * 2)
        elif 'лук' in gear_item.lower():
            self.finesse -= 3 + (bonus * 2)
        elif 'копье' in gear_item.lower():
            self.might -= 2 + (bonus * 2)
            self.resilience -= 1 + (bonus * 2)
        elif 'палица' in gear_item.lower():
            self.finesse -= 1 + (bonus * 2)
            self.resilience -= 2 + (bonus * 2)
        elif 'доспех' in gear_item.lower() or 'кираса' in gear_item.lower():
            self.resilience -= 5 + bonus
        elif 'рубаха' in gear_item.lower():
            self.resilience -= 3 + bonus
            self.finesse -= 1 + bonus
        elif 'кожа' in gear_item.lower():
            self.resilience -= 2 + bonus
            self.finesse -= 3 + bonus

    def extract_enhancement(self, item_name):
    
        return 0

    def gain_experience(self):
        """Проверка повышения уровня"""
        if self.experience >= self.exp_to_next:
            self.level += 1
            self.experience -= self.exp_to_next
            self.exp_to_next = int(self.exp_to_next * 1.8)
            self.skill_points += 3
            
            print("\n" + "★" * 50)
            print("             УРОВЕНЬ ПОВЫШЕН!             ")
            print("★" * 50)
            print(f"Теперь вы {self.level} уровня!")
            print(f"+3 очка улучшения")
            
            # Автоматический рост характеристик
            self.max_health += 12
            self.current_health += 12
            self.might += 2  # Автоматический прирост силы
            print(f"+12 к максимальному здоровью")
            print(f"+2 к силе (автоматически)")
            
            input("\nНажмите Enter, чтобы продолжить...")
            return True
        return False

    def game_menu(self):
        """Главное меню игры"""
        if self.current_health <= 0:
            print("\n💀 ВАШЕ ПУТЕШЕСТВИЕ ОКОНЧЕНО...")
            return self.game_over()
        
        self.gain_experience()
        self.check_dungeon_progress()
        
        print("\n" + "═" * 50)
        print(f"   УРОВЕНЬ ПОДЗЕМЕЛЬЯ: {self.dungeon_level}")
        print(f"   ПРОЙДЕНО КОМНАТ: {self.chambers_cleared}")
        print("═" * 50)
        print(f" ❤️  Здоровье: {self.current_health}/{self.max_health}")
        print(f" 💰 Богатство: {self.coins} золотых")
        print(f" ⚔️  Вооружен: {player_inventory['Оружие'] or 'Нет'}")
        print(f" 🛡️  Защищен: {player_inventory['Доспех'] or 'Нет'}")
        print("─" * 50)
        print(" Ваши действия:")
        print(" 1. 🚶 Продолжить исследование")
        print(" 2. 🎒 Проверить снаряжение")
        print(" 3. 📊 Посмотреть характеристики")
        print(" 4. 📦 Управление предметами")
        print(" 5. 🚪 Покинуть подземелье")
        print("═" * 50)
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            self.explore_chamber()
        elif choice == "2":
            self.check_inventory()
            input("\nНажмите Enter...")
        elif choice == "3":
            self.display_character_sheet()
            input("\nНажмите Enter...")
        elif choice == "4":
            self.manage_gear()
        elif choice == "5":
            return True
        else:
            print("Неверный выбор!")
        
        return False

    def explore_chamber(self):
        """Исследование новой комнаты"""
        self.chambers_cleared += 1
        
        chamber_types = ['боевая комната', 'комната сокровищ', 'комната отдыха']
        left_chamber = choice(chamber_types)
        right_chamber = choice(chamber_types)
        
        print(f"\nВы стоите на развилке подземных ходов...")
        print(f"🔦 Слева: {left_chamber}")
        print(f"🔦 Справа: {right_chamber}")
        
        print("\nКуда направитесь?")
        print("1. Налево")
        print("2. Направо")
        
        direction = input("Направление: ")
        
        if direction == "1":
            chosen_path = left_chamber
        elif direction == "2":
            chosen_path = right_chamber
        else:
            print("Вы заблудились и возвращаетесь назад!")
            return
        
        print(f"\nВы входите в {chosen_path}...")
        
        if chosen_path == 'боевая комната':
            self.combat_encounter()
        elif chosen_path == 'комната сокровищ':
            self.treasure_vault()
        else:
            self.safe_haven()

    def combat_encounter(self):
        """Боевая встреча"""
        print("\n" + "⚔" * 25)
        print("          СХВАТКА С ЧУДОВИЩЕМ         ")
        print("⚔" * 25)
        
        foe = DungeonCreature(self.dungeon_level, self.chambers_cleared)
        foe_health, foe_max_health, foe_power, foe_speed, foe_armor, foe_exp, foe_gold = foe.display_creature_info()
        
        foe_current_health = foe_health
        
        while self.current_health > 0 and foe_current_health > 0:
            print(f"\n❤️  Ваше здоровье: {self.current_health}/{self.max_health}")
            print(f"💀 Здоровье {foe.name}: {foe_current_health}/{foe_max_health}")
            print("\nВаши действия:")
            print("1. Атаковать")
            print("2. Использовать предмет")
            print("3. Попытаться парировать")
            
            action = input("Выбор: ")
            
            if action == "1":
                # Проверка уклонения противника
                if foe_speed > self.finesse and randint(1, 20) <= min(foe_speed - self.finesse, 8):
                    print(f"{foe.name} ловко уворачивается!")
                else:
                    # Атака героя
                    base_damage = self.might
                    min_damage = max(4, base_damage // 2)
                    
                    damage = base_damage - foe_armor
                    if damage < min_damage:
                        damage = min_damage
                    
                    if randint(1, 10) == 1:
                        damage *= 2
                        print("⚡ СМЕРТОНОСНЫЙ УДАР! ⚡")
                    
                    foe_current_health -= damage
                    print(f"Вы наносите {damage} урона!")
            
            elif action == "2":
                self.manage_gear()
                continue
            
            elif action == "3":
                print("Вы готовитесь к парированию...")
                if randint(1, 100) <= self.finesse * 6:
                    print("Вы в идеальной защитной стойке!")
                    continue
                else:
                    print("Не удалось сконцентрироваться!")
            
            else:
                print("Неверное действие!")
                continue
            
            # Атака противника
            if foe_current_health > 0:
                print(f"\n{foe.name} контратакует!")
                
                if self.finesse > foe_speed and randint(1, 20) <= min(self.finesse - foe_speed, 8):
                    print("Вы парируете атаку!")
                else:
                    enemy_damage = foe_power - self.resilience
                    min_enemy_damage = max(3, foe_power // 3)
                    
                    if enemy_damage < min_enemy_damage:
                        enemy_damage = min_enemy_damage
                    
                    if randint(1, 20) == 1:
                        enemy_damage *= 2
                        print("💥 Чудовище наносит сокрушительный удар! 💥")
                    
                    self.current_health -= enemy_damage
                    print(f"{foe.name} наносит вам {enemy_damage} урона!")
        
        if self.current_health <= 0:
            print(f"\n💀 {foe.name} одержал победу...")
        else:
            print(f"\n🎉 {foe.name} повержен!")
            self.experience += foe_exp
            self.coins += foe_gold
            print(f"Получено: {foe_exp} опыта")
            print(f"Найдено: {foe_gold} золотых")
            
            # Шанс на добычу
            if randint(1, 100) <= 45:
                self.find_loot()
        
        input("\nНажмите Enter, чтобы продолжить...")

    def treasure_vault(self):
        """Комната с сокровищами"""
        print("\n" + "💰" * 25)
        print("           ТАЙНИК СОКРОВИЩ            ")
        print("💰" * 25)
        
        print("\nПеред вами древний ларец, покрытый пылью веков...")
        print("1. Открыть ларец")
        print("2. Пройти мимо")
        
        choice = input("Ваше решение: ")
        
        if choice == "1":
            if randint(1, 100) <= 75:
                print("\nЛарец открывается со скрипом...")
                self.find_loot()
            else:
                print("\n💣 ЛАРЕЦ ЗАМКНУТ НА ЛОВУШКУ!")
                trap_damage = randint(8, 20)
                self.current_health -= trap_damage
                print(f"Вы получаете {trap_damage} урона от ловушки!")
                
                if self.current_health <= 0:
                    print("Ловушка оказалась смертельной!")
        
        input("\nНажмите Enter, чтобы продолжить...")

    def safe_haven(self):
        """Комната отдыха"""
        print("\n" + "🕯️" * 25)
        print("           УБЕЖИЩЕ ОТДЫХА             ")
        print("🕯️" * 25)
        
        recovery = int(self.max_health * 0.35)
        previous_health = self.current_health
        self.current_health = min(self.max_health, self.current_health + recovery)
        
        print(f"\nВы находите спокойное место для отдыха...")
        print(f"Восстановлено {self.current_health - previous_health} HP")
        print(f"Теперь у вас {self.current_health}/{self.max_health} здоровья")
        
        if self.skill_points > 0:
            print(f"\nУ вас есть {self.skill_points} очков улучшения")
            print("Хотите улучшить характеристики? (да/нет)")
            if input("> ").lower() in ['да', 'д', 'yes', 'y']:
                self.improve_attributes()
        
 
        
        input("\nНажмите Enter, чтобы продолжить...")

    def check_dungeon_progress(self):
        """Проверка перехода на новый уровень подземелья"""
        if self.chambers_cleared >= 6 * self.dungeon_level:
            self.dungeon_level += 1
            print("\n" + "🌟" * 50)
            print("          НОВЫЙ УРОВЕНЬ ПОДЗЕМЕЛЬЯ!         ")
            print("🌟" * 50)
            print(f"Вы достигли {self.dungeon_level} уровня подземелья!")
            print("Все раны залечены, силы восстановлены!")
            
            self.current_health = self.max_health
            self.skill_points += 2
            level_bonus = self.dungeon_level * 25
            self.coins += level_bonus
            
            print(f"+2 очка улучшения")
            print(f"+{level_bonus} золотых за прохождение уровня")
            
            input("\nНажмите Enter, чтобы продолжить...")

    def find_loot(self):
        """Находка лута"""
        print("\n🎁 ВЫ ОБНАРУЖИЛИ ЦЕННУЮ НАХОДКУ!")
        
        loot_type = randint(1, 100)
        
        if loot_type <= 40:  # Оружие
            item = choice(WEAPONS)
            enhancement = self.dungeon_level + randint(0, 1)
            enhanced_item = f"{item}(+{enhancement})"
            print(f"Найдено: {enhanced_item}")
            self.store_item(enhanced_item)
        
        elif loot_type <= 70:  # Броня
            item = choice(ARMOR)
            enhanced_item = f"{item}(+{self.dungeon_level})"
            print(f"Найдено: {enhanced_item}")
            self.store_item(enhanced_item)
        
        else:  # Расходники
            potion_roll = randint(1, 100)
            if potion_roll <= 55:
                item = CONSUMABLES[0]
            elif potion_roll <= 85:
                item = CONSUMABLES[1]
            else:
                item = CONSUMABLES[2]
            print(f"Найдено: {item}")
            self.store_item(item)

    def game_over(self):
        """Экран окончания игры"""
        print("\n" + "⚰️" * 50)
        print("            ИТОГИ ПУТЕШЕСТВИЯ           ")
        print("⚰️" * 50)
        print(f" Искатель приключений: {self.name}")
        print(f" Происхождение: {self.heritage}")
        print(f" Достигнутый уровень: {self.level}")
        print(f" Исследовано подземелий: {self.dungeon_level}")
        print(f" Покорено комнат: {self.chambers_cleared}")
        print(f" Накоплено богатств: {self.coins} золотых")
        print("─" * 50)
        
        if self.coins >= 1000:
            print(" 💎 ВЕЛИКИЙ СОКРОВИЩЕИСКАТЕЛЬ!")
        elif self.coins >= 500:
            print(" 🏆 ДОСТОЙНЫЙ ИССЛЕДОВАТЕЛЬ!")
        elif self.coins >= 100:
            print(" 🥈 НЕПЛОХОЙ ДОБЫТЧИК!")
        else:
            print(" 🪙 НАЧАЛО ПУТИ...")
        
        print("═" * 50)
        
        print("\n1. Начать новое приключение")
        print("2. Завершить игру")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            # Сброс игры
            global player_inventory
            player_inventory = {'Оружие': '', 'Доспех': ''}
            for i in range(1, 6):
                player_inventory[str(i)] = ''
            
            self.__init__()
            self.create_character()
            return False
        else:
            return True