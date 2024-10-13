import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

    
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
game_is_on = True
screen.onkeypress(player.player_up,"Up")
while game_is_on:
    count=1
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in  car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    #detect successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()
