#Making a dice game using pandas and random libraries
import pandas as pd
import random
class DiceGame:
    def __init__(self, players):
        self.players = players
        self.scores = pd.DataFrame(0, index=players, columns=['Score'])

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        for player in self.players:
            roll = self.roll_dice()
            self.scores.at[player, 'Score'] += roll
            print(f"{player} rolled a {roll}. Total score: {self.scores.at[player, 'Score']}")

    def get_winner(self):
        winner = self.scores['Score'].idxmax()
        return winner, self.scores.at[winner, 'Score']
# Example usage
if __name__ == "__main__":
    players = ['Alice', 'Bob', 'Charlie']
    game = DiceGame(players)
    
    rounds = 5
    for _ in range(rounds):
        game.play_round()
    
    winner, score = game.get_winner()
    print(f"The winner is {winner} with a score of {score}!")
    
    