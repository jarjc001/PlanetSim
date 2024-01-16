from object_package.constants import *
import pygame as pg
import math


class Planet:
    """
    Object for each planet
    Will control the physics and the drawing of it
    """

    def __init__(self, x: float, y: float, radius: float, colour: tuple, mass: float, name: str, isSun: bool = False):
        """
        Planet Object to house the properties of each planet
        :param isSun:
        :param x:   x position (AU)  (normally the Semimajor axis)
        :param y:   y position (AU)
        :param radius:  radius of the planet in the Sim (pixels) (Not real radius)
        :param colour: colour of the planet in the sim
        :param mass: mass of planet (earth masses)
        :param name: name of the planet
        """

        self.x = x * AU
        self.y = y * AU
        self.radius = radius
        self.colour = colour
        self.mass = mass * EARTH_MASS
        self.name = name

        # store data as x,y,vx,vy,t for each body
        self.datapoints = []

        self.orbit = []
        self.isSun = isSun
        self.distance_to_sun = 0

        if isSun:
            self.y_vel = 0
        else:
            self.y_vel = self.cal_orbit_vel()
        self.x_vel = 0

    # def __init__(self, x: float, y: float,
    #              radius: float, colour: tuple,
    #              mass: float, name: str,
    #              x_vel: float = 0, y_vel: float = 0):
    #     """
    #     Planet Object to house the properties of each planet
    #     :param x:   x position (AU)  (normally the Semimajor axis)
    #     :param y:   y position (AU)
    #     :param radius:  radius of the planet in the Sim (pixels) (Not real radius)
    #     :param colour: colour of the planet in the sim
    #     :param mass: mass of planet (earth masses)
    #     :param name: name of the planet
    #     """
    #
    #     self.x = x * AU
    #     self.y = y * AU
    #     self.radius = radius
    #     self.colour = colour
    #     self.mass = mass * EARTH_MASS
    #     self.name = name
    #
    #     self.orbit = []
    #     self.isSun = False
    #     self.distance_to_sun = 0
    #
    #     self.x_vel = x_vel
    #     self.y_vel = y_vel

    def draw(self, win):
        # pygame sets 0,0 to top left corner
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        pg.draw.circle(win, self.colour, (x, y), self.radius)

        ####################################
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + (WIDTH / 2)
                y = y * SCALE + (HEIGHT / 2)
                updated_points.append((x, y))

            pg.draw.lines(win, self.colour, False, updated_points, 1)

    def attraction(self, other):
        """
        Method to cal the force from other bodies in system
        :param other: other body
        :return: force x and y components
        """
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.isSun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets, time):
        total_fx = 0
        total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += (total_fx / self.mass) * TIMESTEP
        self.y_vel += (total_fy / self.mass) * TIMESTEP

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))
        self.cal_orbit_radius()
        # store data as x,y,vx,vy,r,t for each body
        self.datapoints.append([self.x,self.y,self.x_vel,self.y_vel,self.distance_to_sun,time*TIMESTEP])




    def cal_orbit_radius(self):
        self.distance_to_sun = math.sqrt(self.x ** 2 + self.y ** 2)

    def cal_orbit_vel(self):
        # Standard gravitational parameter
        mu = G * (SUN_MASS + self.mass)
        self.distance_to_sun = math.sqrt(self.x ** 2 + self.y ** 2)
        return math.sqrt(mu / abs(self.distance_to_sun))

    def __str__(self):
        return f"Planet: {self.name}, mass: {self.mass}, radius: {self.radius}"
