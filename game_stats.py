import json
from pathlib import Path

class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.ships_left = self.settings.starting_ship_count
        self.reset_stats()
        self.game_active = True 
        self.score = 0
        self.level = 1
        self.hi_score = 0
        self.init_saved_scores()

    def init_saved_scores(self):
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 0:
            try:
                contents = self.path.read_text()
                scores = json.loads(contents)
                self.hi_score = scores.get('hi_score', 0)
            except json.JSONDecodeError:
                print("Invalid JSON in score file. Resetting hi_score.")
                self.hi_score = 0
                self.save_scores()
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        scores = {'hi_score': self.hi_score}
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.ships_left = self.settings.starting_ship_count
        self.max_score = 0

    def update(self, collisions):
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()

    def update_level(self):
        self.level += 1