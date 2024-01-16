from typing import List

from object_package.constants import *
import pygame as pg
import planet as pl
import math
import pandas as pd


class Dao:
    """
        to control data collection for the sim
    """

    def __init__(self, planets: List[pl.Planet]):
        """

        :param planets: the planets in sim
        will create 2 lists to store data
        planetNames -> list of planets used
        dataStore -> to store x,y,vx,vy,r (distance from star), t
        """

        # use a db for it maybe

        # store data as x,y,vx,vy,r,t for each body

        self.planetNames = list()
        self.dataStore = list()


        for planet in planets:
            self.planetNames.append(planet.name)
            self.dataStore.append(
                [planet
                 ]
            )



    def start_dataframe(self):
        """
        init the data
        :return:
        """
        pass

    def collect_data(self):
        pass


    def export_data(self) -> None:
        """
        convert into a dataframe then into sql, csv, or Parquet
        :return:
        """
        pass