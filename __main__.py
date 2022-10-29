import os
import random

from casting.actor import Actor
from casting.artifact import Artifact
from casting.cast import Cast

from directing.director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.color import Color
from shared.point import Point


#refresh movement speed
FRAME_RATE = 10
#display windows size
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
#display font size
FONT_SIZE = 20
#number of cols and rows to create artifacts
COLS = 60
ROWS = 40
#Game caption
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
#number of each artifacts to create
GEM_ARTIFACTS = 10
ROCK_ARTIFACTS = 10



def main():
    
    # create the cast
    cast = Cast()
    
    # create the score banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    #x = int(MAX_X / 2)
    #y = int(MAX_Y / 2)
    #player starting position
    x = int(450)
    y = int(580)
    position = Point(x, y)

    player = Actor()
    player.set_text("##")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
    # create the artifacts gems and rocks

    for g in range(GEM_ARTIFACTS):
        #text = chr(random.randint(33, 126))

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        # random rgb# to generate random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gems = Artifact()
        gems.set_text("*")
        gems.set_font_size(FONT_SIZE)
        gems.set_color(color)
        gems.set_position(position)
        cast.add_actor("gems", gems)
    
    for r in range(ROCK_ARTIFACTS):
        x = random.randint(2, COLS - 1)
        y = random.randint(2, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        rocks = Artifact()
        rocks.set_text("O")
        rocks.set_font_size(FONT_SIZE)
        rocks.set_color(color)
        rocks.set_position(position)
        cast.add_actor("rocks", rocks)
        
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()