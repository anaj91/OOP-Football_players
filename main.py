import json

class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_card, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_card = yellow_card
        self.red_card = red_cards

def get_football_players():
    with open("Football_players.json", "r") as football_players:
        Football_players = json.loads(football_players.read())
        return Football_players


while True:
    seznam = get_football_players()
    print("Enter data for a new football player.")

    first_name = input("Enter player\'s first name: ")
    last_name = input("Enter player\'s last name: ")
    height_cm = float(input("Enter player\'s height in centimeters: "))
    weight_kg = float(input("Enter player\'s weight in kilograms: "))
    goals = int(input("Enter number of goals player has scored: "))
    yellow_cards = int(input("Enter number of yellow cards player got: "))
    red_cards = int(input("Enter number of red cards player got: "))

    new_player = FootballPlayer(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, goals=goals, yellow_card=yellow_cards, red_cards=red_cards )
    seznam.append(new_player.__dict__)

    with open("Football_players.json", "w") as football_players:
        football_players.write(json.dumps(seznam))
    odgovor =input("Would you like to add another player(y/n)?")
    if odgovor == "n":
        break

