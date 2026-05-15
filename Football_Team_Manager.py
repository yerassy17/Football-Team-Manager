from player import Player
from team import Team


def main():
    p1 = Player("Messi", "FW", 90)
    p2 = Player("Ronaldo", "ST", 91)
    p3 = Player("Mbappe", "LW", 89)

    team = Team("AITU FC")

    team.add_player(p1)
    team.add_player(p2)
    team.add_player(p3)

    team.show_players()

    team.save_to_file()

    print("\nSaved players:")
    team.load_from_file()


if __name__ == "__main__":
    main()
