# RPG - Role Play Game

import random
from time import sleep

total_rounds = 0


CRITICAL_DAMAGE = "CRITICAL_DAMAGE"
HEAL = "HEAL"
BOOST = "BOOST"
FRENZY = "FRENZY"
HACKING = "HACKING"
TAKE_DAMAGE = "TAKE_DAMAGE"

class GameEntity:
    def __init__(self, name, health, damage) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value <= 0:
            self.__health = 0
        else:
            self.__health = value
    
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self) -> str:
        return f"{self.name} health: {self.health} damage: {self.damage}"
    


class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)



class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability_type) -> None:
        super().__init__(name, health, damage)
        self.__super_ability_type = super_ability_type

    @property
    def super_ability_type(self):
        return self.__super_ability_type

    @super_ability_type.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    def apply_super_power(self, boss: Boss, heroes: list):
        pass
    

class Warrior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, CRITICAL_DAMAGE)

    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 5)
        boss.health -= self.damage*coef
        message = f"Warrior {self.name}, hits criticaly: {self.damage*coef}" \
            if coef else "Не нанес критический урон"
        print(message) 


class Medic(Hero):
    def __init__(self, name, health, damage, heal_point) -> None:
        super().__init__(name, health, damage, HEAL)
        self.__heal_point = heal_point

    def apply_super_power(self, boss: Boss, heroes: list):
        print(f"Medic {self.name}: {self.__heal_point} healed")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_point


class Magic(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, BOOST)

    def apply_super_power(self, boss: Boss, heroes: list):
        boost = random.randint(1, 5)
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost
        print(f"Magic {self.name}: {boost} boosted")

class Berserk(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, FRENZY)

    def apply_super_power(self, boss: Boss, heroes: list):
        frenzy = random.uniform(0, boss.damage)
        boss.health -= self.damage+frenzy

class Hacker(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, HACKING)
        self.hacking = False
        self.stolen_hp = HACKING
        
    def apply_super_power(self, boss: Boss, heroes: list):
           if self.hacking:
            self.hacking = False
            stolen_hp = boss.health - 20
            if stolen_hp > 0:
                random_hero = random.choice(heroes)
                random_hero.receive_healing(stolen_hp)
                print(f"{self.name} hacked {stolen_hp} HP from {boss.name} and transferred it to {random_hero.name}")
            else:
                boss.receive_damage(self.damage)
                self.hacking = True
                print(f"{self.name} attacked {boss.name} for {self.damage} damage and activated hacking mode")
        # for hero in heroes:           
        #     boss.health - 30
        # if hero.health > 0 and hero != self:
        #     hack = random.choice(heroes)
        #     print(f"Hacker")
            
class Golem(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, TAKE_DAMAGE)
        self.take_boss_damage = TAKE_DAMAGE 
        # self.take_d
    def take_boss_damage(self, damage):
        self.health -= damage
    
    def super_ability_type(self, damage, heroes):
        for hero in heroes:
            if isinstance(hero, Golem):
                continue
            hero.take_damage(damage/5)
    
    def show_info(self):
        print(f"{self.name}'s health: {self.health}")
    
    def take_damage(self, damage):
        self.health -= damage


def is_game_finished(boss: Boss, heroes: list):
    if boss.health <= 0:
        print("Heroes WON!")
        return True
    
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead



def print_statistic(boss: Boss, heroes: list):
    print(f"________ {total_rounds} ROUND ________")
    print(boss)
    for hero in heroes:
        print(hero)


def boss_hit(boss: Boss, heroes: list):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            hero.health -= boss.damage

def heroes_hit(boss: Boss, heroes: list):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            boss.health -= hero.damage

def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice([CRITICAL_DAMAGE, BOOST, HEAL, FRENZY, TAKE_DAMAGE])
    print(f"Boss blocked {boss_ability}")
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss_ability != hero.super_ability_type:
            hero.apply_super_power(boss, heroes)

def play_round(boss: Boss, heroes: list):
    print_statistic(boss, heroes)
    global total_rounds
    total_rounds += 1
    boss_hit(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_power(boss, heroes)
    


def start():
    boss = Boss("Antaras", 1000, 50)

    warrior = Warrior("Varvar", 260, 5)
    warrior_2 = Warrior("Terminator", 290, 10)
    medic = Medic("Aibolit", 220, 5, 15)
    medic_2 = Medic("Dr. Haos", 240, 10, 10)
    magic = Magic("Wisard", 290, 20)
    warrior_3 = Berserk("Berserk", 270, 10)
    warrior_4 = Hacker("Hacker", 220, 5)
    warrior_5 = Golem("Golem", 500, 3)

    heroes = [warrior, medic, medic_2, magic, warrior_2, warrior_3, warrior_4, warrior_5]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)
        # sleep(1)
        

    print_statistic(boss, heroes)


start()
