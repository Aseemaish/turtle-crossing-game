from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True):
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)
