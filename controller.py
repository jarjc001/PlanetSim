import numpy as np
import pygame as pg
import math
from object_package import planet as pl
from object_package.constants import *

pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planet Sim")


# create run loop to keep window open
# only closes on x button
def main():
    run = True
    time = 0

    # sets a max frame rate
    clock = pg.time.Clock()

    # add bodies to sim
    sun = pl.Planet(0, 0, 20, YELLOW, (SUN_MASS / EARTH_MASS), "Sun", True)

    mercury = pl.Planet(-0.3871, 0, 3, GREY, 0.0553, "Mercury")

    venus = pl.Planet(-0.7233, 0, 6, GREEN, 0.8150, "Venus")

    earth = pl.Planet(-1, 0, 6, BLUE, 1, "Earth")

    mars = pl.Planet(-1.5237, 0, 5, RED, 0.1074, "Mars")

    jupiter = pl.Planet(-5.2028, 0, 12, ORANGE, 317.894, "Jupiter")

    saturn = pl.Planet(-9.5388, 0, 11, GOLD, 95.184, "Saturn")

    uranus = pl.Planet(-19.1914, 0, 9, TEAL, 14.537, "Uranus")

    neptune = pl.Planet(-30.0611, 0, 10, NAVY, 17.132, "Neptune")

    planets: list = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # set_up_time = pg.time.get_ticks()
    frame_counter = 0

    while run:
        # max fps
        clock.tick(FRAME_RATE)
        # #time += clock.get_time()
        # time = pg.time.get_ticks() - set_up_time

        frame_counter += 1


        # refresh
        WIN.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets,frame_counter)
            planet.draw(WIN)

        pg.display.update()

    pg.quit()
