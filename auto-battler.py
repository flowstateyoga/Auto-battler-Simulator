import random

class Character:
    """Represents a battle character with elemental abilities and stats."""
    # Separate element data from display
    ELEMENTS = ["fire", "water", "earth", "air"]
    
    ELEMENT_DISPLAY = {
        "fire": ("🔥", "\033[91m"),    # Red
        "water": ("💧", "\033[94m"),   # Blue
        "earth": ("🪨", "\033[93m"),   # Yellow
        "air": ("༄", "\033[97m")       # White
    }
    
    ABILITIES = {
        "fire": {"fireball": 10, "firestorm": 20, "fire cross": 30, "true fireball": 40},
        "water": {"waterball": 10, "water blade": 20, "tsunami": 30, "waterfall": 40},
        "earth": {"stone barrage": 10, "stone hedge": 20, "stone tomb": 30, "earthquake": 40},
        "air": {"wind blade": 10, "wind strike": 20, "wind barrage": 30, "tornado": 40}
    }
    
    RESET = "\033[0m"
    
    def __init__(self, name):
        """Initialize a character with random stats and element."""
        self.name = name
        self.hp = random.randint(50, 100)
        self.attack = random.randint(5, 25)
        self.defense = random.randint(5, 50)
        self.luck = random.randint(1, 10)
        self.element = random.choice(self.ELEMENTS)
        
        # Get abilities and display info
        abilities = self.ABILITIES[self.element]
        self.sorted_abilities = sorted(abilities.items(), key=lambda x: x[1])
        self.emoji, self.color = self.ELEMENT_DISPLAY[self.element]
        
        # Pre-calculate luck weights
        luck_bonus = self.luck / 10.0
        self.ability_weights = [1 + (i * luck_bonus) for i in range(len(self.sorted_abilities))]
    
    def choose_ability(self):
        """Select an ability based on luck-weighted probabilities."""
        return random.choices(self.sorted_abilities, weights=self.ability_weights)[0]
    
    def get_effectiveness(self, target_element):
        """Calculate damage multiplier based on element matchup."""
        # Air is neutral against all elements
        if self.element == "air" or target_element == "air":
            return 1.0
        
        # Rock-paper-scissors system
        effectiveness = {
            ("fire", "earth"): 1.5,
            ("earth", "water"): 1.5,
            ("water", "fire"): 1.5,
        }
        
        return effectiveness.get((self.element, target_element), 1.0)
    
    def attack_target(self, target):
        """Attack target with chosen ability, applying element effectiveness."""
        ability_name, ability_damage = self.choose_ability()
        base_damage = ability_damage + self.attack
        effectiveness = self.get_effectiveness(target.element)
        damage = int(base_damage * effectiveness)
        actual_damage = max(1, damage - target.defense)
        target.hp -= actual_damage
        return ability_name, actual_damage, effectiveness
    
    def is_alive(self):
        return self.hp > 0
    
    def colorize(self, text):
        """Apply element color to text."""
        return f"{self.color}{text}{self.RESET}"
    
    def display_name(self):
        return f"{self.element} {self.emoji}"

class AutoBattler:
    """Manages battles between two characters."""
    def __init__(self, player1_name, player2_name):
        """Initialize battle with two characters."""
        self.player1 = Character(player1_name)
        self.player2 = Character(player2_name)
    
    def display_stats(self):
        """Display both players' stats with element colors."""
        for player in (self.player1, self.player2):
            print(f"\n{player.colorize(f'{player.name} Stats:')}")
            print(player.colorize(
                f"HP: {player.hp}, Attack: {player.attack}, Defense: {player.defense}, "
                f"Luck: {player.luck}, Element: {player.display_name()}"
            ))
    
    def battle(self):
        """Execute turn-based battle until one character is defeated."""
        print(f"\n{self.player1.name} ({self.player1.colorize(self.player1.display_name())}) vs "
              f"{self.player2.name} ({self.player2.colorize(self.player2.display_name())})")
        print("Battle begins!\n")
        
        round_num = 1
        while self.player1.is_alive() and self.player2.is_alive():
            print(f"Round {round_num}:")
            
            # Determine turn order with probability of (50/50)
            attacker, defender = (self.player1, self.player2) if random.random() < 0.5 else (self.player2, self.player1)
            
            # First attack
            ability, damage, effectiveness = attacker.attack_target(defender)
            effectiveness_text = " (Super effective!)" if effectiveness > 1.0 else ""
            print(attacker.colorize(f"{attacker.name} goes first! Uses {ability} for {damage} damage!{effectiveness_text}"))
            print(defender.colorize(f"{defender.name} HP: {defender.hp}"))
            
            # Counter-attack if defender survives
            if defender.is_alive():
                ability, damage, effectiveness = defender.attack_target(attacker)
                effectiveness_text = " (Super effective!)" if effectiveness > 1.0 else ""
                print(defender.colorize(f"{defender.name} uses {ability} for {damage} damage!{effectiveness_text}"))
                print(attacker.colorize(f"{attacker.name} HP: {attacker.hp}"))
            
            print()
            round_num += 1
        
        return self.player1 if self.player1.is_alive() else self.player2

def main():
    """Main game loop."""
    player1_name = input("Enter player 1 name: ")
    player2_name = input("Enter player 2 name: ")
    
    game = AutoBattler(player1_name, player2_name)
    game.display_stats()
    
    input("\nPress Enter to continue to battle...")
    
    winner = game.battle()
    print(winner.colorize(f"{winner.name} wins!"))
    print(winner.colorize(f"Element: {winner.display_name()}, HP remaining: {winner.hp}"))

if __name__ == "__main__":
    main()