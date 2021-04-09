#!/usr/bin/env python3
import random
import boat as bt

ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

def player_turn(M1):
    a = input("Case a attaquer: ")
    if (bt.check_input_case(a, M1)):
        return (0)
    # Convertis l'user input (str) vers un nombre (int)
    x = int(a[1:]) - 1
    # Convertis la lettre par un nombre
    y = ord(a[0]) - ord('A')
    if (M1[y][x] >= 2):
        boat = M1[y][x]
        M1[y][x] = 1
        if (bt.coule(boat, M1)):
            if (boat > 10):
                boat -= 10
            print("%s Coulé +%d points" %(a, boat * 2))
            return (2 * boat)
        print("%s Touché +1 point" %a)
        return (1)
    elif (M1[y][x] == 1):
        print("Tricheur -10 points")
        return (-10)
    else:
        print("Raté")
        M1[y][x] = -1
    return (0)

def computer_turn(M2):
    print("L'ordinateur attaque la case ", end='')
    while (1):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Evite de tirer sur la même case
        if (M2[y][x] == 1 or M2[y][x] == -1):
            continue
        print("%c%d" %(ALPHABET[y], x + 1))
        if (M2[y][x] >= 2):
            boat = M2[y][x]
            M2[y][x] = 1
            if (bt.coule(boat, M2)):
                if (boat > 10):
                    boat -= 10
                print("Coulé +%d points" %(boat * 2))
                return (2 * boat)
            print("Touché +1 point")
            return (1)
        else:
            print("Raté")
            M2[y][x] = -1
        break
    return (0)

def loop_game(M1, M2):
    score_user = 25
    score_computer = 25
    case_hit_user = 0
    case_hit_computer = 0
    while (1):
        print("Grille de l'ordinateur:")
        bt.print_grid(M1, 0)
        print("Grille de l'utilisateur:")
        bt.print_grid(M2, 1)
        a = player_turn(M1)
        if (a > 0):
            case_hit_user += 1
        score_user = score_user + a - 1
        if (case_hit_user == 17):
            print("Le joueur a gagné avec %d points." %score_user)
            break
        if (score_user <= 0):
            print("L'ordinateur a gagné avec %d points." %score_computer)
            break
        a = computer_turn(M2)
        if (a > 0):
            case_hit_computer += 1
        score_computer = score_computer + a - 1
        if (case_hit_computer == 17):
            print("L'ordinateur a gagné avec %d points." %score_computer)
            break
        if (score_computer <= 0):
            print("Le joueur a gagné avec %d points." %score_user)
            break

def main():
    # Creation des deux grilles
    M1 = []
    M2 = []
    for y in range(10):
        M1.append([])
        M2.append([])
        for _ in range (10):
            M1[y].append(0)
            M2[y].append(0)
    # Placement des bateaux de l'ordinateur
    M1 = bt.computer_boat(M1)
    # Placement des bateaux de l'utilisateur
    M2 = bt.user_boat(M2)
    # Boucle de jeux
    loop_game(M1, M2)


if __name__ == '__main__':
    main()