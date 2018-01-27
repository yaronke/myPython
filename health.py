import random
import math

# 1 - easy
# 2- medium
# 3- hard

health = 50
difficulty = 1
potionHealth = int(random.randint(25,50) / difficulty)
print(potionHealth)

health = health + potionHealth
print(health)
