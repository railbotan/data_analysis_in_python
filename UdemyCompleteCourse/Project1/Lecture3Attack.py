import random
from Classes.Enemy import Enemy


enemy1 = Enemy(200, 60)
print(enemy1.get_hp())


enemy2 = Enemy(100, 150)
print(enemy2.get_hp())


'''


player_hp = 260
enemy_atk_low = 60
enemy_atk_high = 80

while player_hp > 0:
    dmg = random.randrange(enemy_atk_low, enemy_atk_high)
    player_hp -= dmg

    if player_hp < 30:
        player_hp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", player_hp)

    if player_hp > 30:
        continue

    print("You have low health. You have been teleported to nearest inn.")
    break

'''