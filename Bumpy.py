#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:36:32 2021

@author: Varun
"""

import json
from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from highlight_text import fig_text

from mplsoccer import Bumpy, FontManager, add_image

epl = Image.open(
    urlopen("https://github.com/andrewRowlinson/mplsoccer-assets/blob/main/epl.png?raw=true")
)

season_dict = pd.read_csv('/Your Path/FPL.csv')

phase = ['September','October','November','Decemeber','January','February','March','April','May']

highlight_dict = {
    "Player1" : "#FF0000",
    "Player2" : "#008000",
    "Player3" : "#0000FF",
    "Player4" : "#FFFFFF",
    "Player5" : "#800080",
    }

bumpy = Bumpy(
    scatter_color="#282A2C", line_color="#252525",  # scatter and line colors
    rotate_xticks=90,  # rotate x-ticks by 90 degrees
    ticklabel_size=17, label_size=30,  # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True,  # plot the labels
    alignment_yvalue=0.1,  # y label alignment
    alignment_xvalue=0.065  # x label alignment
)

fig, ax = bumpy.plot(
    x_list=phase,  # match-day or match-week
    y_list=np.linspace(1, 20, 20).astype(int),  # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.5,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict,  # team to be highlighted with their colors
    figsize=(20, 16),  # size of the figure
    x_label='Phase', y_label='Position',  # label name
    ylim=(-0.1, 23),  # y-axis limit
    lw=2.5,   # linewidth of the connecting lines
)

#Title & Subtitle
TITLE = "SSN Fantasy Premier League 2020/21 phase-wise standings:"
SUB_TITLE = "A comparison between different players"

fig.text(0.09, 0.95, TITLE, size=29, color="#F2F2F2")

fig_text(
    0.09, 0.94, SUB_TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": '#FF0000'}, {"color": '#008000'}, {"color": '#0000FF'}, 
                         {"color": '#FFFFFF'}, {"color": '#800080'}],
    size=25, fig=fig
)

fig = add_image(
     epl,
     fig,  # figure
     0.02, 0.9,  # left and bottom dimensions
     0.08, 0.08  # height and width values
)

