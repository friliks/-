#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from hero import Hero



def main():

    # Создаем героя
    player = Hero()
    player.create_character()
    
    # Главный игровой цикл
    adventure_continues = True
    while adventure_continues:
        if player.game_menu():
            print("\n" + "═" * 50)
            print("          ПУТЕШЕСТВИЕ ЗАКОНЧЕНО           ")
            print("Надеемся увидеть вас снова, искатель приключений!")
            print("═" * 50)
            adventure_continues = False

if __name__ == "__main__":
    main()