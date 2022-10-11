# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

i = 2021
while i > 0:
    sweets1 = int(input("Игрок 1 - введите количество конфет: "))
    if sweets1 > 28 or sweets1 < 0:
        raise ValueError("Играй по правилам")
    elif sweets1 < 29 and sweets1 > 0:
        if i - sweets1 == 0:
            print("Победил 1- й игрок.")
            break
        elif i - sweets1 <= 0:
            raise ValueError("Неверный ход")
        else:
            i = i - sweets1
            print(f"Осталось {i} конфет: ")
    sweets2 =int(input("Игрок 2 введите количество конфет: "))
    if sweets2 > 28 and sweets2 < 0:
        raise ValueError("Играй по правилам")
    elif sweets2 < 29 and sweets2 >= 0:
        if i - sweets2 == 0:
            print("Победил 2 игрок.")
            break
        elif i - sweets2 <= 0:
            raise ValueError("Неверный ход")
        else:
            i = i - sweets2
            print(f"Осталось {i} конфет")
    