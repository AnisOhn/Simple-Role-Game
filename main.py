import random

# Nombre de points de vies 

user_health = enemy_health = 50

# Nombre de potions 

potions = 3

user_turn = True

while user_health > 0 and enemy_health > 0:

    # Tour du joueur

    if user_turn == True:
        print("Souhaitez vous attaquer ou prendre une potion ?")
        print("1. Attaquer")
        print("2. Prendre une potion")
        choice = int(input())

        # Si le joueur n'a plus de potions

        while choice == 2 and potions == 0:
            print("Vous n'avez plus de potions !")
            print("Souhaitez vous attaquer ou prendre une potion ?")
            print("1. Attaquer")
            print("2. Prendre une potion")
            choice = int(input())


         # Si le joueur attaque

        if choice == 1:

            
            user_damage = random.randint(5,10)
            enemy_health -= user_damage
            print(f"Vous avez attaqué et infligé {user_damage} de dégats !")
            if enemy_health > 0:
                print(f"Point de vies de l'ennemi restant : {enemy_health}")
            user_turn = False
            print("\n--------------------------------------------------\n")

            if enemy_health > 0:
                print("Au tour de l'ennemi...")


        elif choice == 2:
            potions -= 1
            potion_points = random.randint(15,50)
            user_health += potion_points
            print(f"Vous avez utilisé une potion, il vous reste {potions} potions...")
            print(f"Vous avez maintenant {user_health} points de vie")
            user_turn = False
            print("Au tour de l'ennemi...")
            print("\n--------------------------------------------------\n")

    else:
        enemy_damage = random.randint(5,15)
        user_health -= enemy_damage
        print(f"L'ennemi vous a infligé {enemy_damage}")
        if user_health > 0:
            print(f"Il vous reste {user_health} points de vie")
        user_turn = True
        continue


if enemy_health <= 0:
    print("Vous avez gagné ! fin de la partie")
if user_health <= 0:
    print("Vous avez perdu, fin de la partie")
