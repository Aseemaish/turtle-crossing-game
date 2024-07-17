import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
game_is_on = True

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.level_up()
        car.level_up()


screen.exitonclick()


