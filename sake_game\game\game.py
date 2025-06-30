from .models import Sake, Player, SakeType
from .views import display_sakes, display_player

def create_sakes():
    return [
        Sake("Dassai 50", SakeType.JUNMAI, 50),
        Sake("Dewazakura", SakeType.GINJO, 70),
        Sake("Juyondai", SakeType.DAIGINJO, 100),
    ]

def create_player(name, budget):
    return Player(name, budget)

def play_game():
    sakes = create_sakes()
    player = create_player("Sake Lover", 200)

    while True:
        print("\nSakes:")
        display_sakes(sakes)
        print("\nPlayer:")
        display_player(player)

        choice = input("Enter the number of the sake to buy (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        try:
            choice = int(choice)
            sake = sakes[choice - 1]
            if player.budget >= sake.price:
                player.sakes.append(sake)
                player.budget -= sake.price
                sakes.remove(sake)
                print(f"You bought {sake.name} for ${sake.price}!")
            else:
                print("You don't have enough budget!")
        except (ValueError, IndexError):
            print("Invalid choice!")

    print("\nGame Over!")
    display_player(player)