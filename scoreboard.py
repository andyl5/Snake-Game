from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.home()
        self.write(arg="Game Over!", move=False, align="center", font=("Arial", 24, "normal"))