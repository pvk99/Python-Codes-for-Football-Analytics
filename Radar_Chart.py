#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:19:24 2021

@author: Varun
"""

import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar

df = pd.read_csv('/Your Path/MIdfielders.csv')
df['Player'] = df['Player'].str.split('\\',expand=True)[0]

df = df[(df['Player']=='Thomas Partey') | (df['Player']=='Pierre Højbjerg')].reset_index()

df = df.drop(['index','Rk','Nation','Pos','Squad','Born','Age'],axis=1)

params = list(df.columns)
params = params[1:]

# Add ranges to list of tuple pairs
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(df[params][x])
    a = a - (a*0.05)
    
    b = max(df[params][x])
    b = b + (b*0.05)
    
    ranges.append((a,b))

for x in range(len(df['Player'])):
    if df['Player'][x] == 'Pierre Højbjerg':
        a_values = df.iloc[x].values.tolist()
    
    if df['Player'][x] == 'Thomas Partey':
        b_values = df.iloc[x].values.tolist()

a_values = a_values[1:]
b_values = b_values[1:]

values = [a_values,b_values]

#title
title = dict(
    title_name = 'Pierre Højbjerg',
    title_color = '#132257',
    subtitle_name = 'Spurs',
    subtitle_color = '#132257',
    
    title_name_2 = 'Thomas Partey',
    title_color_2 = '#b2101d',
    subtitle_name_2 = 'Arsenal',
    subtitle_color_2 = '#b2101d',
    
    title_fontsize = 18,
    subtitle_fontsize = 15
    )

endnote = 'data via FBref/Statsbomb\nAll units are in per90'

radar = Radar()

fig,ax = radar.plot_radar(ranges=ranges,params=params,values=values,
                          radar_color=['#111B72','#b2101d'],alphas =[0.55,0.5   ],title=title,
                          image='/Your Path/Premier_League.png', 
                          image_coord=[0.464, 0.81, 0.1, 0.075],
                          endnote=endnote, compare=True)

