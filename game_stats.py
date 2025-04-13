class GameStats:
    def __init__(self, ship_limit) -> None:
        self.ships_left = ship_limit
        self.bullets_fired = 0
        self.aliens_destroyed = 0
        