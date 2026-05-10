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