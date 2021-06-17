#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:39:17 2021

@author: Varun
"""

import pandas as pd
import numpy as np

from scipy import stats
import math

from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

df = pd.read_csv('/Your Path/FileName.csv')

# splitting player name column for fbref csv
# df['Player'] = df['Player'].str.split('\\',expand=True)[0]

df = df.drop(['#','Team'],axis=1).reset_index()

params = list(df.columns)
# print(params)
params = params[2:]

player = df.loc[df['Name']=='Sergio Reguilon'].reset_index()
player = list(player.loc[0])
player = player[3:]

values = []
for x in range(len(params)):
    values.append(math.floor(stats.percentileofscore(df[params[x]],player[x])))
    
# instantiate PyPizza class
baker = PyPizza(
    params=params,                  # list of parameters
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=1,              # linewidth for other circles
    other_circle_ls="-."            # linestyle for other circles
)

# plot pizza
fig, ax = baker.make_pizza(
    values,              # list of values
    figsize=(8, 8),      # adjust figsize according to your need
    param_location=110,  # where the parameters will be added
    kwargs_slices=dict(
        facecolor="#ff7f50", edgecolor="#000000",
        zorder=2, linewidth=1
    ),                   # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
        va="center"
    ),                   # values to be used when adding parameter
    kwargs_values=dict(
        color="black", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#ff7f50",
            boxstyle="round,pad=0.2", lw=1
        )
    )                    # values to be used when adding parameter-values
)

# add title
fig.text(
    0.515, 0.97, "Sergio Reguilon", size=18,
    ha="center", color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.942,
    "per 90 Percentile Rank vs PL Defenders | Season 2020-21",
    size=15,
    ha="center", color="#000000"
)

# add credits
CREDIT_1 = "data: From sofascore"


fig.text(
    0.99, 0.005, f"{CREDIT_1}", size=9,
    color="#000000",
    ha="right"
)

plt.show()
