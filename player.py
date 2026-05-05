class Player:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = rating

    def __str__(self):
        return f"{self.name} - {self.position} ({self.rating})"



