import stats

# import random

# Create the characters
Orderus = stats.CharacterStats(" Orderus ")
Orderus.name = " Orderus "
for i in range(60, 90):
    Orderus.health = random.randint(60, 90)
Wild_Beast = stats.CharacterStats(" Wild Beast ")
Wild_Beast.name = " Wild Beast "
Wild_Beast.health = 100
Wild_Beast.strenght = 70
Wild_Beast.defense = 50
Wild_Beast.speed = 60
Wild_Beast.luck = 30

print(Orderus)
print(Wild_Beast)
