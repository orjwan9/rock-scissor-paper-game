#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(["rock", "paper", "scissors"])


class humanplayer(Player):
    def move(self):

        while True:
            x = input("pleas input one of them 'rock, paper, scissors '")
            if x in moves:
                break

        return x


class ReflectPlayer(Player):
    def __init__(self):
        self.reflectmove = "rock"

    def learn(self, my_move, their_move):
        self.reflectmove = their_move

    def move(self):
        return self.reflectmove


class CyclePlayer(Player):
    def __init__(self):
        self.flag = 0
        self.cyclemove = 0

    def move(self):

        if self.flag == 0:

            self.cyclemove = "rock"
            self.flag += 1

        elif self.flag == 1:
            self.cyclemove = "paper"
            self.flag += 1

        elif self.flag == 2:
            self.cyclemove = "scissors"
            self.flag += 1

        else:
            self.cyclemove = "rock"
            self.flag -= 3
        return self.cyclemove


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def beats(self, one, two):

        if one == two:
            print("no winnr")

        elif (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        ):
            self.p1score += 1
        else:
            self.p2score += 1

        return self.p1score, self.p2score

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        self.p2.learn(move2, move1)
        self.beats(move1, move2)

    def play_game(self):
        print("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()
            if self.p1score == 2 or self.p2score == 2:
                break
            print(f"Score:Player1 {self.p1score},Player2 {self.p2score}")
            quit = input(
                " to end the game input quite,press Enter  to continue "
            )
            if quit == "quite":
                break
        print("Game over!")
        if self.p1score > self.p2score:
            print("winner is humanplayer")
        elif self.p1score == self.p2score:
            print("No winner")
        else:
            print("winner is computer player ")


if __name__ == "__main__":
    game = Game(humanplayer(), ReflectPlayer())
    game.play_game()
