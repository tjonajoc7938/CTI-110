# Christos Tjonajong
# 4/16/25
# P5HW
# Creates a simple game

import random


def create_character():     # Creates the player's character
    character = {"name": input("\U0001FAC5 What is your character's name? "),
                 "max_health": int(input("\u2764\ufe0f How much health does you character have? "))
                 }
    while character["max_health"] < 10:  # Ensures logic in enemy generation does not result in 0
        character["max_health"] = int(input("\u2764\ufe0f Please enter a number that is at least 10: "))
    character["attack"] = int(input("\U0001F5E1\uFE0F How much damage does your character do? "))
    while character["attack"] < 10:
        character["attack"] = int(input("\U0001F5E1\uFE0F Please enter a number that is at least 10: "))
    character["icon"] = "\U0001FAC5"  # Sets icon for the player
    character['health'] = character['max_health']   # Creates variable based on max_health for tower_combat()
    return character  # Returns character information for use in other functions


def display_character(character):  # Displays the character's attributes
    print(character)


def make_enemy(floor, character):  # Generates enemies based on the floor, with stats based on the player
    if 1 <= floor <= 4:

        enemy = {
            "name": "Ant",
            "health": round(1 * character["attack"]),
            "attack": round(0.05 * character["max_health"]),
            "icon": "\U0001F41C",
            "until_attack": 1,  # How many turns until the enemy attacks
            "max_until": 1  # Stores until_attack statically for use with tower_combat()
        }
        return enemy
    elif floor == 5:
        enemy = {
            "name": "Aranea, The Weaver",
            "health": round(2 * character["attack"]),
            "attack": round(0.1 * character["max_health"]),
            "icon": "\U0001F577\uFE0F",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif 6 <= floor <= 9:
        enemy = {
            "name": "Shrimp",
            "health": round(1.5 * character["attack"]),
            "attack": round(0.15 * character["max_health"]),
            "icon": "\U0001F990",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif floor == 10:
        enemy = {
            "name": "Cancrorum, The Crusher",
            "health": round(3 * character["attack"]),
            "attack": round(0.2 * character["max_health"]),
            "icon": "\U0001F980",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif 11 <= floor <= 14:
        enemy = {
            "name": "Lizard",
            "health": round(2.25 * character["attack"]),
            "attack": round(0.2 * character["max_health"]),
            "icon": "\U0001F98E",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif floor == 15:
        enemy = {
            "name": "Serpens, The Consumer",
            "health": round(4 * character["attack"]),
            "attack": round(0.3 * character["max_health"]),
            "icon": "\U0001F40D",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif 16 <= floor <= 19:
        enemy = {
            "name": "Ghost",
            "health": round(2.5 * character["attack"]),
            "attack": round(0.25 * character["max_health"]),
            "icon": "\U0001F47B",
            "until_attack": 2,
            "max_until": 2
        }
        return enemy
    elif floor == 20:
        enemy = {
            "name": "Osseus, The Forgotten",
            "health": round(5 * character["attack"]),
            "attack": round(0.4 * character["max_health"]),
            "icon": "\U0001F480",
            "until_attack": 3,
            "max_until": 3
        }
        return enemy
    elif 21 <= floor <= 24:
        enemy = {
            "name": "Zombie",
            "health": round(3.5 * character["attack"]),
            "attack": round(0.3 * character["max_health"]),
            "icon": "\U0001F9DF",
            "until_attack": 3,
            "max_until": 3
        }
        return enemy
    elif floor == 25 or floor == 0:
        enemy = {
            "name": "King Brutus, The Traitor",
            "health": round(6 * character["attack"]),
            "attack": round(0.5 * character["max_health"]),
            "icon": "\U0001F934",
            "until_attack": 4,
            "max_until": 4
        }
        return enemy
    elif floor == 26:
        enemy = {
            "name": "end",
            "health": 0,
            "attack": 0,
            "icon": "",
            "until_attack": 0,
            "max_until": 0
        }
        return enemy  # Returns the enemy for use in other functions


def tower_combat(floor, enemy, character):  # Controls the game's combat
    turn = 0
    block = False
    while enemy['health'] > 0 and character['health'] > 0:  # Runs while either character is alive
        print(f"\nFloor: {floor}")
        print(f"{character['name']:<10} {enemy['name']}")  # Information relies on create_character() and make_enemy()
        print(f"{character['icon']:<10}{enemy['icon']}")
        print(f"{character['health']:<10} {enemy['health']}")
        print(f"Turn: {turn:<10}Turns until enemy attacks: {enemy['until_attack'] - 1}")
        choice = input("\nAttack(1) or Block(2)? ")
        while choice != "1" and choice != "2":  # Str rather than int to avoid error if "attack" or "block" is entered
            print("\nInvalid Input!")
            choice = input("Please type 1 for Attack or 2 for Block. ")
        if choice == "1":
            print(f"\nYou attack the enemy!")
            crit = random.randint(0, 6)  # Random chance to deal double damage
            if crit == 5:
                print("\n\U0001F4A5 Critical Hit! \U0001F4A5")
                enemy['health'] -= character['attack'] * 2
            else:
                enemy['health'] -= character['attack']  # Enemy takes damage based on player's attack
            block = False  # Prevents block from being True when attack is selected
            enemy['until_attack'] -= 1
            turn += 1  # Helps player keeps track of how many turns until the enemy attacks
        elif choice == "2":
            print("\nYou block next turn's attack.")
            block = True
            enemy['until_attack'] -= 1
            turn += 1
        if enemy['until_attack'] == 0:
            if enemy['health'] > 0:
                if block:
                    print("\nYou blocked the enemy's attack!")  # Blocking negates all damage done to player
                elif not block:
                    print("\nThe enemy attacks you!")
                    character['health'] -= enemy['attack']  # PLayer takes damage based on enemy's attack
            enemy['until_attack'] = enemy['max_until']
    if enemy['health'] <= 0:
        print("\nFloor Cleared!")
        food = random.randint(0, 6)  # Random chance to heal
        if food == 5:
            print("\nYou found a health drop! \U0001F357")
            print(f"+{round(character['max_health'] * 0.20)} health")
            character['health'] += round(character['max_health'] * 0.20)


def story(floor, enemy, character):  # Controls what enemies say when they enter the game
    if floor == 0:
        print(f"\n{character['icon']:<10}{enemy['icon']}")  # Icons rely on create_character() and make_enemy()
        input("King Brutus: The princess is stuck at the top of the tower! (Press Enter to continue)")
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: I trust that you, my child, can save her. (Press Enter to continue)")
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: Climb the 25 floors, and save her! (Press Enter to continue)")

    elif floor == 5:
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("Aranea: I'll squash you like the bug you are! (Press Enter to continue)")
    elif floor == 10:
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("Cancrorum: The claws you love so much will be your end! (Press Enter to continue)")
    elif floor == 15:
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("Serpens: You'll ssserve great as an appetizzzer! (Press Enter to continue)")
    elif floor == 20:
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("Osseus: How could the king forget me? (Press Enter to continue)")
    elif floor == 25:
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: I didn't think you'd get so far. (Press Enter to continue)")
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: There is no princess! (Press Enter to continue)")
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: I lured you here to get rid of you once and for all! (Press Enter to continue)")
        print(f"\n{character['icon']:<10}{enemy['icon']}")
        input("King Brutus: This kingdom must come to an end! (Press Enter to continue)")


def defeat_text(floor, enemy, character):  # Controls text that appears when certain enemies are defeated
    if floor == 5:
        if enemy['health'] <= 0:
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("Aranea: What about my babies... (Press Enter to continue)")
    elif floor == 10:
        if enemy['health'] <= 0:
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("Cancrorum: Alas, my kind is gone... (Press Enter to continue)")
    elif floor == 15:
        if enemy['health'] <= 0:
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("Serpens: Thisss unbearable hunger is finally over... (Press Enter to continue)")
    elif floor == 20:
        if enemy['health'] <= 0:
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("Osseus: He can't be trusted... (Press Enter to continue)")
    elif floor == 25:
        if enemy['health'] <= 0:
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: All this power was corrupting me. (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: Not caring about the insects... (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: Hunting the sea life... (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: Starving the reptiles... (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: Leaving my aid Osseus to rot... (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: Even wanting to kill my own child. (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: I pray that you won't suffer the same fate. (Press Enter to continue)")
            print(f"\n{character['icon']:<10}{enemy['icon']}")
            input("King Brutus: The kingdom is now in your hands. \U0001F451(Press Enter to continue)")


def main():
    floor = 0  # Defines floor parameter for use in functions
    hero = create_character()
    display_character(hero)
    enemy = make_enemy(floor, hero)
    story(floor, enemy, hero)
    while floor != 26 and hero['health'] > 0:  # Runs while game has not ended
        floor += 1
        enemy = make_enemy(floor, hero)  # Runs first since other functions rely on enemy that is returned
        story(floor, enemy, hero)
        tower_combat(floor, enemy, hero)
        defeat_text(floor, enemy, hero)  # Runs last so that text appears before next enemy is generated
    if floor == 26:  # End condition when player is alive at the end
        print("\nYou are now the ruler!")
        print("\n\U0001F451 You win! \U0001F451")
    if hero['health'] <= 0:  # End condition when player dies
        print("\nYou Died! \U0001F480")


main()  # Calls main function to run the game
