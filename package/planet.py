from package.constants import *
import pygame as pg


class Planet:

    def __init__(self, x: float, y: float, radius: float, colour: tuple, mass: float, name: str):
        """
        Planet Object to house the properties of each planet
        :param x:   x position (AU)
        :param y:   y position (AU)
        :param radius:  radius of the planet in the Sim (pixels) (Not real radius)
        :param colour: colour of the planet in the sim
        :param mass: mass of planet (earth masses)
        :param name: name of the planet
        """

        self.x = x*AU
        self.y = y*AU
        self.radius = radius
        self.colour = colour
        self.mass = mass * EARTH_MASS
        self.name = name

        self.orbit = []
        self.isSun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        # pygame sets 0,0 to top left corner
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        pg.draw.circle(win, self.colour, (x, y), self.radius)

    def __str__(self):
        return f"Planet: {self.name}, mass: {self.mass}, radius: {self.radius}"
