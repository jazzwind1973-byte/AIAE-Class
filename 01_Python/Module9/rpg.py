# RPG遊戲角色

import random
import time

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name =name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack
        self.defense = defense

    def info(self):
        print(
            f"Name : {self.name}\n"
            f"HP   : {self.hp:>5}\n"
            f"ATK  : {self.attack_power:>5}\n"
            f"DEF  : {self.defense:>5}\n"
        )

    def attack(self, target):
        defense_value = random.randint(1, target.defense)
        damage = max(0, self.attack_power - defense_value)
        target.hp -= damage
        
        print(f"{self.name}攻擊{target.name}!造成傷害{damage}，剩餘血量 {target.hp}/{target.max_hp}")

    def is_alive(self):
        return self.hp > 0

hero = Character("Hero", 100, 20, random.randint(1, 10))
monster = Character("slime" ,50, 10, random.randint(1, 10))

hero.info()
monster.info()

while hero.is_alive() and monster.is_alive():
    hero.attack(monster)

    if monster.is_alive():
        monster.attack(hero)
    else:
        print(f"{hero.name}Win")
    if not hero.is_alive():
        print(f"{monster.name} Win")
    time.sleep(3)#間隔一秒      
            
