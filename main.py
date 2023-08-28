import stats
import random

# Create the characters
Orderus = stats.CharacterStats(" Orderus ")
Orderus.name = " Orderus "
Orderus.health = random.randint(60, 90)
Orderus.strenght = random.randint(60, 90)
Orderus.defense = random.randint(40, 60)
Orderus.speed = random.randint(40, 60)
Orderus.luck = random.randint(25, 40)


Wild_Beast = stats.CharacterStats(" Wild Beast ")
Wild_Beast.name = " Wild Beast "
Wild_Beast.health = random.randint(60, 90)
Wild_Beast.strenght = random.randint(60, 90)
Wild_Beast.defense = random.randint(40, 60)
Wild_Beast.speed = random.randint(40, 60)
Wild_Beast.luck = random.randint(25, 40)


print(Orderus)
print(Wild_Beast)
