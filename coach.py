class Coach:
    def __init__(self, name, formation):
        self.name = name
        self.formation = formation

    def show_tactic(self):
        print("\nCoach:", self.name)
        print("Formation:", self.formation)