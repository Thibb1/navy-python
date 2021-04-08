#!/usr/bin/env python3
import random
import boat as bt

ALPHABET = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

def player_turn(M1, score_user):
    a = input("Case a attaquer: ")
    if (bt.check_input_case(a, M1)):
        return (0)
        x = int(a[1:]) - 1
        y = ord(a[0]) - ord('A')
        if (M1[y][x] >= 2):
            boat = M1[y][x]
            M1[y][x] = 1
            if (bt.coule(boat, M1)):
                print("Coulé")
                if (boat > 10):
                    boat -= 10
                score_user += 2 * boat
            else:
                score_user += 1
                print("Touché")

def loop_game(M1, M2):
    score_user = 25
    score_computer = 25
    case_hit_user = 0
    case_hit_computer = 0
    while (1):
        if (case_hit_computer == 17 or score_user == 0):
            break
        case_hit_user += player_turn(M1, score_user)
        score_user -= 1
        print(score_user)
        if (boat_hit_user != 17):
            case_hit_computer += player_turn(M1)

def main():
    # Creation des deux grilles
    M1 = []
    M2 = []
    for y in range(10):
        M1.append([])
        M2.append([])
        for x in range (10):
            M1[y].append(0)
            M2[y].append(0)
    # Placement des bateaux de l'ordinateur
    M1 = bt.computer_boat(M1)
    # Placement des bateaux de l'utilisateur
    #M2 = bt.user_boat(M2)
    # Affichage des grilles
    print("Grille de l'ordinateur:")
    bt.print_grid(M1, 1)
    print("Grille de l'utilisateur:")
    bt.print_grid(M2, 1)
    # Boucle de jeux
    # loop_game(M1, M2)


if __name__ == '__main__':
    main()