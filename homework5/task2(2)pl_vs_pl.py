# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# player_va_player

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которые возьмете от 1 до 28: "))
    while x < 1 or x > 29:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x
    
def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперьу него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количетсво конфет на столе: "))
who_the_first = randint(0,2)
if who_the_first:
    print(f"первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")
    
counter1 = 0
counter2 = 0

while value > 28:
    if who_the_first:
        k = input_dat(player1)
        counter1 += k
        value -= k
        who_the_first = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player1)
        counter2 += k
        value -= k
        who_the_first = True
        p_print(player1, k, counter2, value)
        
if who_the_first:
    print(f"Выйграл {player1} !!!")
else:
    print(f"Выйграл {player2} !!!")
    