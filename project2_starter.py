"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Najee Shuler]
Date: [11-14-25]

AI Usage: AI helped with implementation of methods in all classes, ensuring correct use of inheritance (super()) and polymorphism (method overriding).
"""
#asked Gemini to debugg what was wrong with the first test case

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """

    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.max_health = health  # Useful for reference
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """
        Basic attack method that all characters can use.
        Damage is calculated based on strength.
        """
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} performs a basic strike, dealing {damage} damage to {target.name}.")

    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Remaining Health: {self.health}")

    def display_stats(self, *args, **kwargs):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"--- {self.name} ---")
        print(f"  Health: {self.health}/{self.max_health}")
        print(f"  Strength: {self.strength}")
        print(f"  Magic: {self.magic}")


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features (class, level).
    """

    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1

    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        """
        super().display_stats()
        print(f"  Class: {self.character_class}")
        print(f"  Level: {self.level}")


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Create a warrior with appropriate stats: high health, high strength, low magic.
        """
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific (extra physical damage).
        """
        base_damage = self.strength
        bonus_damage = 5
        total_damage = base_damage + bonus_damage
        target.take_damage(total_damage)
        print(
            f"🗡️ {self.name} attacks with a strong blow (Base {base_damage} + {bonus_damage} Bonus), dealing {total_damage} damage to {target.name}.")

    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = (self.strength * 2) + 10
        target.take_damage(damage)
        print(f"💥 {self.name} unleashes Power Strike, dealing massive {damage} physical damage to {target.name}!")


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Create a mage with appropriate stats: low health, low strength, high magic.
        """
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # Damage based on Magic * 1.5
        damage = int(self.magic * 1.5)
        target.take_damage(damage)
        print(
            f"✨ {self.name} zaps with an Arcane Bolt (Magic-based), dealing {damage} magical damage to {target.name}.")

    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # Damage based on Magic * 3
        damage = self.magic * 3
        target.take_damage(damage)
        print(f"🔥 {self.name} casts Fireball, dealing intense {damage} magical damage to {target.name}!")


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Create a rogue with appropriate stats: medium health, medium strength, medium magic.
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific (consistent, fast damage).
        Since 'random' is removed, we apply a small, guaranteed bonus damage.
        """
        base_damage = self.strength
        bonus_damage = 2  # Small, consistent bonus damage for finesse
        damage = base_damage + bonus_damage

        target.take_damage(damage)
        print(
            f"🗡️ {self.name} strikes with speed (Base {base_damage} + {bonus_damage} Bonus), dealing {damage} damage to {target.name}.")

    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit (double damage).
        """
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"🔪 {self.name} uses Sneak Attack! Guaranteed critical hit, dealing {damage} damage to {target.name}!")


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """

    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """
        Display information about this weapon.
        """
        print(f"Weapon: {self.name} (+{self.damage_bonus} Damage Bonus)")


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create one of each character type
    warrior = Warrior("Himmel")
    mage = Mage("Frieren")
    rogue = Rogue("Eisen")

    # Display their stats (Player.display_stats overrides Character.display_stats)
    print("\n📊 Character Stats (Testing Override):")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different logic):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        # The specific attack method executed depends on the character's actual class (Warrior, Mage, Rogue)
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
        dummy_target.max_health = 100  # Reset for safety

    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8) 

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Test the battle system
    print("\n⚔️ Testing Simple Battle System (Warrior vs Mage):")
    # Reset characters for a fresh fight
    warrior_battle = Warrior("Himmel") 
    mage_battle = Mage("Frieren")    
    battle = SimpleBattle(warrior_battle, mage_battle)
    battle.fight()

    print("\n✅ Testing complete!")
