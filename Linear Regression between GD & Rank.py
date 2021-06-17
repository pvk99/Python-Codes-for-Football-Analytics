#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:41:25 2021

@author: Varun
"""

#Independent Variable : Goal Differential; Dependent Variable : League Position

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import add_image

from sklearn.linear_model import LinearRegression

df = pd.read_csv('/Your Path/ISL_League_Rank _2014-2020.csv')

y = df.Rk
x = df.GD.values.reshape(-1,1)

# print(x.shape,y.shape)

model = LinearRegression().fit(x,y)
r_sq = model.score(x,y)
intercept = model.intercept_
slope = model.coef_

y_pred = intercept + slope*x

fig,ax = plt.subplots(figsize=(8,8))
ax.set_facecolor('#ffffb3')

plt.scatter(x,y)

plt.plot(x,y_pred,c='red')

plt.ylim(0.5,11.5)
plt.yticks([1,2,3,4,5,6,7,8,9,10,11])
plt.gca().invert_yaxis()

plt.xlabel('Goal Differential')
plt.ylabel('League Rank')

plt.title('Evaluating the relationship between Goal Differential & League Rank (2014-2020)')

logo = plt.imread('/Your Path/ISL Logo.png')
ax_image = add_image(logo, fig, left=0.78, bottom=0.12, width=0.12, interpolation='hanning')

plt.annotate('@pvk_21', (0,0), (40, -26), xycoords='axes fraction', textcoords='offset points', va='bottom')