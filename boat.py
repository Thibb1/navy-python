#!/usr/bin/env python3
import random

BATEAUX = ("", "", "Sous-marin", "Contre-torpilleur", "Croiseur", "Porte-avions")
ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

def coule(boat, M):
    # Check si le bateaux est coulé
    boat_alive = 0
    for y in range(10):
        for x in range(10):
            if (M[y][x] == boat):
                boat_alive += 1
    # Si le nombre de case touchée est egal au nombre de cases du bateaux
    if (boat_alive == 0):
        return (1)
    return (0)

def check_boat_x(M, x, y, boat):
    # Verifie si le bateaux peux être placé verticalement
    for i in range(x, x + boat):
        if (M[y][i] == 1):
            return (1)
    return (0)

def check_boat_y(M, x, y, boat):
    # Verifie si le bateaux peux être placé horizontalement
    for i in range(y, y + boat):
        if (M[i][x] == 1):
            return (1)
    return (0)

def computer_boat(M1):
    # Choisit des placement de bateaux aléatoires
    boat = 2
    torpilleur_nb = 0
    while (boat <= 5):
        rotation = random.randint(0, 1)
        if (rotation == 1):
            x = random.randint(0, 9)
            y = random.randint(0, 10 - boat)
            if (check_boat_y(M1, x, y, boat)):
                continue
            for i in range(y, y + boat):
                M1[i][x] = boat + torpilleur_nb * 10
        else:
            x = random.randint(0, 10 - boat)
            y = random.randint(0, 9)
            if (check_boat_x(M1, x, y, boat)):
                continue
            for i in range(x, x + boat):
                M1[y][i] = boat + torpilleur_nb * 10
        if (torpilleur_nb == 0 and boat == 3):
            torpilleur_nb += 1
            continue
        boat += 1
    return (M1)

def print_grid(M, show_boats):
    # Affiche la grille des bateaux
    for y in range(10):
        print("----------------------------------------------------")
        for x in range(10):
            if (M[y][x] >= 2 and show_boats):
                print("| #  ", end='')
            elif (M[y][x] == 1):
                print("| X  ", end='')
            elif (M[y][x] == -1):
                print("| O  ", end='')
            else:
                print("| %c%d " %(ALPHABET[y], x + 1), end='')
        if (M[y][x] != 0 and show_boats):
            print(" ", end='')
        print("|")
    print("----------------------------------------------------")

def check_input_case(a, M):
    # Si l'input est incorrect alors l'utilisateur c'est trompé
    if (a == ''):
        return (1)
    if (len(a) < 2 or len(a) > 3):
        return (1)
    x = int(a[1:]) - 1
    y = ord(a[0]) - ord('A')
    if (x < 0 or x > 9):
        return (1)
    if (y < 0 or y > 9):
        return (1)
    return (0)

def check_input_place(a, M, rotation, boat):
    # Verifie le placement des bateaux de l'utilisateur
    if (len(a) < 2 or len(a) > 3):
        return (1)
    x = int(a[1:]) - 1
    y = ord(a[0]) - ord('A')
    if (x < 0 or x > 9):
        return (1)
    if (y < 0 or y > 9):
        return (1)
    if (rotation == 1):
        if (x > 10 - boat):
            return (1)
    elif (rotation == 0):
        if (y > 10 - boat):
            return (1)
    return (0)

def user_boat(M2):
    boat = 2
    torpilleur_nb = 0
    while (boat <= 5):
        print("%s:" %BATEAUX[boat])
        print_grid(M2, 1)
        a = input("Case de départ: ")
        rotation = input("Rotation[0: vertical, 1: horizontal]: ")
        if rotation == '':
            print("Mauvaise rotation")
            continue
        rotation = int(rotation)
        if (check_input_place(a, M2, rotation, boat)):
            print("Mauvaise case de départ")
            continue
        x = int(a[1:]) - 1
        y = ord(a[0]) - ord('A')
        if (rotation == 1):
            if (check_boat_x(M2, x, y, boat)):
                print("Mauvaise case de départ")
                continue
            for i in range(x, x + boat):
                M2[y][i] = boat + torpilleur_nb * 10
        elif (rotation == 0):
            if (check_boat_y(M2, x, y, boat)):
                print("Mauvaise case de départ")
                continue
            for i in range(y, y + boat):
                M2[i][x] = boat + torpilleur_nb * 10
        else:
            print("Mauvaise rotation")
            continue
        if (torpilleur_nb == 0 and boat == 3):
            torpilleur_nb += 1
            continue
        boat += 1
    return (M2)