from player import Player
from team import Team


def main():
    p1 = Player("Messi", "FW", 90)
    p2 = Player("Ronaldo", "ST", 91)
    p3 = Player("Mbappe", "LW", 89)
    p4 = Player("Modric", "CM", 88)
    p5 = Player("De Bruyne", "CM", 91)
    p6 = Player("Kante", "CDM", 87)
    p7 = Player("Hakimi", "RB", 85)
    p8 = Player("Van Dijk", "CB", 89)
    p9 = Player("Rudiger", "CB", 86)
    p10 = Player("Davies", "LB", 84)
    p11 = Player("Courtois", "GK", 90)

    team = Team("AITU FC")

    team.add_player(p1)
    team.add_player(p2)
    team.add_player(p3)
    team.add_player(p4)
    team.add_player(p5)
    team.add_player(p6)
    team.add_player(p7)
    team.add_player(p8)
    team.add_player(p9)
    team.add_player(p10)
    team.add_player(p11)

    team.show_players()

    team.save_to_file()

    print("\nSaved players:")
    team.load_from_file()

    team.average_rating()

    team.remove_player("Mbappe")

    team.show_players()

    team.team_statistics()


if __name__ == "__main__":
    main()
