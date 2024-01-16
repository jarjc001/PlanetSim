import pandas as pd
import csv


def start_dataframe(planets):
    dfList = []
    for planet in planets:
        df = pd.DataFrame(planet.datapoints,columns=["x","y","vx","vy","r","t"])
        df["name"] = planet.name
        dfList.append(df)

    return pd.concat(dfList)



def export_data(df):
    df.to_csv('orbit_data.csv', index=False)
    df.to_parquet('orbit_data.parquet')
