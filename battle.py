import random
import main

# Simulate the battle between the characters


def battle(Orderus, Wild_Beast):
    round_number = 0
    while Orderus.health > 0 and Wild_Beast.health > 0:
        # Damage = Attacker strenght - Defender defense
        # If the defender is lucky, the damage will be 0

        # Calculate the damage without the luck reduction
        Orderus_damage = Orderus.strenght - Wild_Beast.defense
        Wild_Beast_damage = Wild_Beast.strenght - Orderus.defense

        # Initiate the skills of the characters
        Orderus_Rapid_Strike = 10
        Orderus_Magic_Shield = 20

        # Calculate the non-negative damage
        Orderus_damage = max(0, Orderus_damage)
        Wild_Beast_damage = max(0, Wild_Beast_damage)

        # If the damage is negative, the damage will be 0
        # if Orderus_damage < 0:
        #    Orderus_damage = 0
        # if Wild_Beast_damage < 0:
        #    Wild_Beast_damage = 0

        # The characters attack each other
        Wild_Beast.health -= Orderus_damage
        Orderus.health -= Wild_Beast_damage

        # Display the beginning of the battle
        round_number = round_number + 1
        string = f" Round {round_number} "
        output = string.center(50, "-") + "\n"
        print(output)

        # Display the damage
        print(f"{Orderus.name} attacks {Wild_Beast.name} with {Orderus_damage} damage")
        print(
            f"{Wild_Beast.name} attacks {Orderus.name} with {Wild_Beast_damage} damage"
        )

        # Check if the characters are lucky
        if Wild_Beast.luck > random.randint(0, 100):
            print("The Beast is lucky")
            Wild_Beast_damage = 0
        elif Orderus.luck > random.randint(0, 100):
            print("Orderus is lucky")
            Orderus_damage = 0

        # Check if Ordeus has the Rapid Strike skill
        if Orderus_Rapid_Strike > random.randint(0, 100):
            Orderus_damage = Orderus_damage * 2
            print("Orderus uses Rapid Strike")

        # Check if Ordeus has the Magic Shield skill
        if Orderus_Magic_Shield > random.randint(0, 100):
            Orderus_damage = Wild_Beast_damage / 2
            print("Orderus uses Magic Shield")

        # Display the health of the characters
        print(f"{Orderus.name} has {Orderus.health} health left")
        print(f"{Wild_Beast.name} has {Wild_Beast.health} health left")

        # Check if the characters are still alive
        if Orderus.health <= 0:
            print(f"{Orderus.name} is dead")
        if Wild_Beast.health <= 0:
            print(f"{Wild_Beast.name} is dead")


# Call the battle function
battle(main.Orderus, main.Wild_Beast)
