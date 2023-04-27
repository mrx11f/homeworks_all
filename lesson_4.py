
total_round = 0

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
def name(self, value):
    if value <= 0:
        self.__health = 0
    else:
        self.__health = value
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

    @damage.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    def apply_super_power(boss: Boss, heroes: list):
        pass

class Warrior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_power(boss: Boss, heroes: list):
        pass

class Medic(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "HEAL")

    def apply_super_power(boss: Boss, heroes: list):
        pass

class Magic(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "BOOST")

    def apply_super_power(boss: Boss, heroes: list):
        pass


def is_game_finished(boss: Boss, heroes: list):
    if boss.health <= 0:
        print("Heroes WON")
        return True
    
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
           all_heroes_dead = False

    if all_heroes_dead:
        print("Boss WON") 

    return all_heroes_dead

def print_statistic(boss: Boss, heroes: list):
    print(f"_____________{total_round} ROUND_____________")
    print(boss)
    for hero in heroes:
        print(hero) 



def boss_hit(boss, heroes: list):
    for hero in heroes:
        hero.health -= boss.damage

def heroes_hit(boss, heroes: list):
    for hero in heroes:
        boss.health -= hero.damage

def heroes_power(boss: Boss, heroes: list):
    for hero in heroes:
        hero.apply_super_power(boss, heroes)

def play_round(boss: Boss, heroes: list):
    global total_round
    a = 1 
    total_round +=1
    boss_hit(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_power(boss, heroes)
    print_statistic()



def start():
    boss = Boss("Antaras" , 2000, 50)

    warrior = Warrior("Varvar", 260, 10, "CRITICAL_DAMAGE")


    heroes = [warrior, ]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)

start()