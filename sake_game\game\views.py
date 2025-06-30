from .models import Sake, Player, SakeType

def display_sakes(sakes):
    for i, sake in enumerate(sakes, 1):
        print(f"{i}. {sake.name} ({sake.type.name}) - ${sake.price}")

def display_player(player):
    print(f"Player: {player.name} - Budget: ${player.budget}")
    print("Sakes:")
    for i, sake in enumerate(player.sakes, 1):
        print(f"{i}. {sake.name} ({sake.type.name})")