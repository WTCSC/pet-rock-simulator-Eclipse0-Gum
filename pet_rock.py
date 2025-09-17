import time
import sys

# Helper functions
def dramatic_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_pet_name():
    dramatic_print("Hey There! Welcome to your pet rock game, I expect you to do a very good job. Now let's get started.")
    time.sleep(1.5)
    return input("What are you gonna name your pet rock?")
pet_name = get_pet_name()

stats = {
    "happiness": 5,
    "hunger": 5
}

def display_stats(name, stats):
    dramatic_print(f"\n--- Your Pet Rock, {name} ---")
    time.sleep(0.05)
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}/10")

def display_menu(name):
    dramatic_print(f"\nWhat do you want {name} to do?")
    time.sleep(0.05)
    dramatic_print("1. Make your pet eat some food")
    time.sleep(0.05)
    dramatic_print("2. Make your pet play with you")
    time.sleep(0.05)
    dramatic_print("3. Do absolutely nothing")
    time.sleep(0.05)
    dramatic_print("4. Leave the game")
    time.sleep(0.05)
    return input("Your Choice: ")
        
while True:
    display_stats(pet_name, stats)       
    choice = display_menu(pet_name)

    if choice == "1":
        dramatic_print(f"You make {pet_name} eat some food.")
        stats["hunger"] -= 2
        stats["happiness"] -= 1

    elif choice == "2":
        dramatic_print(f"You make {pet_name} play.")
        stats["happiness"] += 2
        stats["hunger"] += 1

    elif choice == "3":
        dramatic_print(f"You decide to do absolutely nothing with {pet_name}.")
        stats["happiness"] -= 1
        stats["hunger"] += 1

    elif choice == "4":
        dramatic_print("Goodbye Friend! Thanks for playing (This doesn't save your progress loser).")
        break   

    else:
        dramatic_print("That wasn’t a valid choice!")

    
    stats["hunger"] += 1
    stats["happiness"] -= 1
    
        
    if stats["hunger"] >= 10:
        dramatic_print(f"Oh no! {pet_name} starved... better luck next time =)")
        break
    elif stats["happiness"] <= 0:
        dramatic_print(f"Oh no! {pet_name} became too sad... be a better friend punk")
        break
