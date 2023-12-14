import numpy as np
import pygame as pg
import math
from package import planet as pl
from package.constants import *

pg.init()


WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planet Sim")




# create run loop to keep window open
# only closes on x button
def main():
    run = True

    #sets a max frame rate
    clock = pg.time.Clock()

    # add bodies to sim
    sun = pl.Planet(0, 0, 40, YELLOW, 1.989e30 / EARTH_MASS, "Sun")
    sun.isSun = True

    mercury = pl.Planet(-0.3871, 0, 6, GREY, 0.0553, "Mercury")

    venus = pl.Planet(-0.7233, 0, 14, GREEN, 0.8150, "Venus")

    earth = pl.Planet(-1, 0, 16, BLUE, 1, "Earth")

    mars = pl.Planet(-1.5237, 0, 8, RED, 0.1074, "Mars")



    planets: list = [sun,mercury,venus,earth,mars]


    while run:
        # max fps
        clock.tick(60)

        # fill screen with white
        # WIN.fill(WHITE)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pg.display.update()

    pg.quit()

