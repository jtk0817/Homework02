import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import seaborn as sns

# 파일 경로 변경
df0 = pd.read_csv('C:/Users/82105/Documents/GitHub/Homework02/RSMC_Best_Track_Data.csv')
df0['year'] = df0['Time of analysis'].apply(lambda x: int(x[0:4]))

print(df0)  # 데이터프레임 출력

print(df0.info())
print(df0.columns.tolist())

for y in range(2020, 2024):
    df = df0[df0['year'] == y].copy()
    geometry = [Point(xy) for xy in zip(df['Longitude of the center'], df['Latitude of the center'])]
    gdf = GeoDataFrame(df, geometry=geometry)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    gdf.plot(ax=world.plot(figsize=(12, 12)), color='orange', markersize=10)
    plt.title(str(y))
    plt.show()

print(df0.columns.tolist())
maxcols = ['Maximum sustained wind speed',
           'The longest radius of 50kt winds or greater',
           'The longest radius of 30kt winds or greater']
mincols = ['Central pressure']
print(len(maxcols))

for i in range(len(mincols)):
    df = df0[['Name of the storm', mincols[i]]].dropna()
    data = df.sort_values(mincols[i], ascending=True)[0:40]
    plt.figure(figsize=(15, 6))
    plt.title(mincols[i])
    g = sns.barplot(x=data['Name of the storm'], y=data[mincols[i]], color='seagreen', data=data)
    g.tick_params(axis='x', labelrotation=45)
    plt.show()
