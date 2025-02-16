import random

class Player:
    def __init__(self, int, str, dex, con):
        self.int = int
        self.str = str
        self.dex = dex
        self.con = con
        self.hit_point = random.randint(1, 20) + con

    def damage(self):
        pass  # Placeholder for subclasses to override

    def take_damage(self, damage):
        self.hit_point -= damage
        if self.hit_point <= 0:
            return self.did_you_die()
        return f"Player hit points: {self.hit_point}"

    def did_you_die(self):
        if self.hit_point <= 0:
            return "Your hero has fallen"
        elif self.hit_point == 1:
            return "Your hero has blacked out"

class Wizard(Player):
    def __init__(self):
        super().__init__(int=25, str=1, dex=2, con= 50)

    def damage(self):
        dealt = self.int + random.randint(1, 20)
        return dealt

class Warlock(Player):
    def __init__(self):
        super().__init__(int=6, str=4, dex=6, con= 75)

    def damage(self):
        dealt = self.dex + self.str + self.int + random.randint(1, 20)
        return dealt

class Cleric(Player):
    def __init__(self):
        super().__init__(int=6, str=4, dex=6, con= 100)

    def damage(self):
        dealt = self.int + self.str + self.dex + random.randint(1, 20)
        return dealt

class Paladin(Player):
    def __init__(self):
        super().__init__(int=6, str=8, dex=6, con= 150)

    def damage(self):
        dealt = self.dex + self.str + random.randint(1, 20)
        return dealt

class Druid(Player):
    def __init__(self):
        super().__init__(int=4, str=4, dex=6, con=125)

    def damage(self):
        dealt = self.str + self.int + self.dex + random.randint(1, 20)
        return dealt

class Monster(Player):
    def __init__(self):
        super().__init__(int= 10, str=8, dex=6, con=30)

    def damage(self):
        dealt = self.str + random.randint(1, 20)
        if dealt <= 10:
            overall_damage_dealt = dealt
        elif dealt <= 15:
            overall_damage_dealt = dealt + 5
        else:
            overall_damage_dealt = dealt + 15
        return overall_damage_dealt

    def damage_taken(self, damage):
        inflicted_damage = damage - self.hit_point
        if inflicted_damage > 0:
            return self.did_you_die()
        return inflicted_damage

def choose_hero():
    while True:
        try:
            choice = int(input("Pick your hero: 1-Wizard 2-Warlock 3-Cleric 4-Paladin 5-Druid: "))
            if choice == 1:
                return Wizard()
            elif choice == 2:
                return Warlock()
            elif choice == 3:
                return Cleric()
            elif choice == 4:
                return Paladin()
            elif choice == 5:
                return Druid()
            else:
                print("Invalid choice. Please pick a valid hero.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def main_game_loop():
    monster = Monster()
    print("Welcome to the battle, heroes...")
    hero = choose_hero()

    while True:
        # Player turn
        player_damage = hero.damage()
        print(f"{hero.__class__.__name__} deals {player_damage} damage")
        monster.take_damage(player_damage)

        if monster.hit_point <= 0:
            print("Monster has been defeated!")
            break

        # Monster turn
        monster_damage = monster.damage()
        print(f"Monster deals {monster_damage} damage")
        result = hero.take_damage(monster_damage)
        print(result)

        if hero.hit_point <= 0:
            print(f"{hero.__class__.__name__} has fallen!")
            break

if __name__ == "__main__":
    main_game_loop()




        
    



    

    

 



    



       

    




