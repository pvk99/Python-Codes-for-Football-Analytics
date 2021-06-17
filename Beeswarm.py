#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:25:09 2021

@author: Varun
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from highlight_text import ax_text
import seaborn as sns

df = pd.read_csv('/Your Path/Filename.csv')
# df['Player'] = df['Player'].str.split('\\',expand=True)[0]

df2 = df.copy(deep=True)

background = '#003366'
textcolor = 'white'
fig, ax = plt.subplots(figsize=(10,5))

# Set up metrics
metrics = ['Prog Passes','Passes into final third','xA','Pass Completion%','Key passes','Passes into Penalty Box']
fig,axes = plt.subplots(3,2,figsize=(14,12))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)

mpl.rcParams['xtick.color'] = textcolor
mpl.rcParams['ytick.color'] = textcolor

counter=0
counter2=0
met_counter=0

#initial for loop
for i,ax in zip(df2['Name'],axes.flatten()):
    ax.patch.set_facecolor(background)
    
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    sns.swarmplot(x=metrics[met_counter],data=df2,ax=axes[counter,counter2],
                  zorder=1,color='grey')
    
    ax.set_xlabel(f'{metrics[met_counter]}',c=textcolor)
    
    for x in range(len(df2['Name'])):
        if df2['Name'][x] == 'Player1':
            ax.scatter(x=df2[metrics[met_counter]][x],y=0,s=100,c='#ff7f50',
                       zorder=3,label='Player1')
        if df2['Name'][x] == 'Player2':
            ax.scatter(x=df2[metrics[met_counter]][x],y=0,s=200,
                       c='#ffd633',zorder=2,label='Player2')
            
        if df2['Name'][x] == 'Player3':
            ax.scatter(x=df2[metrics[met_counter]][x],y=0,s=150,
                       c='#cc0000',zorder=2,label='Player3')
            

    
    met_counter+=1
    if counter2==0:
        counter2 = 1
        continue
    if counter2==1:
        counter2=0
        counter+=1
        
fig.suptitle('PLayer1 Vs Player 2 Vs Player 3', fontsize=16,color='white')
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right',labelcolor='black')
plt.savefig('/Your Path/FrenchLB.png',dpi=300)


