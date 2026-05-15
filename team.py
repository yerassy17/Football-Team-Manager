class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        print(f"\nTeam: {self.name}")

        for player in self.players:
            print(player)

    def save_to_file(self):
        with open("players.txt", "w") as file:
            for player in self.players:
                file.write(f"{player.name},{player.position},{player.rating}\n")

    def load_from_file(self):
        with open("players.txt", "r") as file:
            for line in file:
                name, position, rating = line.strip().split(",")
                print(f"{name} - {position} - {rating}")


