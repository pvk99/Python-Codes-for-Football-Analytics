#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 12:50:32 2021

@author: Varun
"""

from mplsoccer import VerticalPitch, Pitch, add_image, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG
from matplotlib import rcParams
import numpy as np
import pandas as pd
from PIL import Image
from scipy.ndimage import gaussian_filter

from urllib.request import urlopen
from highlight_text import ax_text
import matplotlib.pyplot as plt


rcParams['text.color'] = '#c7d5cc'

df = pd.read_csv('/Your Path/Arsenaleventdata2021.csv')

plf = df[df['Player']=='Nicolas Pepe']
shots=plf[(plf['Type']=='MissedShots') | 
            (plf['Type']=='SavedShot') |
            (plf['Type']=='Goal')]

goals = shots[shots['Type']=='Goal']
ShoT = shots[shots['Type']=='SavedShot']
shb = shots[shots['Type']=='MissedShots']



#Pepe's Progressive Pass Receving Points
pif = df[(df['Recipient']=='Nicolas Pepe') & 
          (df['Type']=='Pass') & (df['Outcome']=='Successful')]

pif['A'] = np.sqrt(
          ((105 - pif['x']) ** 2) +
          ((68 - pif['y'])** 2)
          )

pif['B'] = np.sqrt(
          ((105 - pif['endX']) ** 2) +
          ((68 - pif['endY'])** 2)
          )

pif['Prog_pass'] = pif['B'] < pif['A']
          
progpass = pif[pif['Prog_pass']==True]

pitch = VerticalPitch(pitch_type='opta', line_zorder=1.0,
              line_color='white', pitch_color='black')
# fig, axs = pitch.draw()
fig, axs = pitch.grid(ncols=2,axis=False)
fig.set_facecolor("black")
# plot heatmap
bin_statistic = pitch.bin_statistic(progpass.endX, progpass.endY,
                                    statistic='count', bins=(15, 15))
bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], 1)
pcm = pitch.heatmap(bin_statistic, ax=axs['pitch'][0], cmap='hot', edgecolors='#191919')

# plot colorbar
ax_cbar = fig.add_axes((0.475, 0.17, 0.02, 0.5))
cbar = plt.colorbar(pcm, cax=ax_cbar)
cbar.outline.set_edgecolor('#e6e6e6')
cbar.ax.yaxis.set_tick_params(color='#e6e6e6')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

#plot shots
nodes1 = pitch.scatter(goals.x,goals.y,
                              s=50,color='#008000', label = 'Goal',
                              edgecolors='#323232',linewidth=1,alpha=1,
                              zorder=1.5,ax=axs['pitch'][1])

nodes2 = pitch.scatter(ShoT.x,ShoT.y,
                              s=50,color='#ff9900', label = 'Shot on Target',
                              edgecolors='#323232',linewidth=1,alpha=1,
                              zorder=1.5,ax=axs['pitch'][1])
        
nodes3 = pitch.scatter(shb.x,shb.y,
                              s=50,color='#ff3333', label = 'Missed Shots',
                              edgecolors='#323232',linewidth=1,alpha=1,
                              zorder=1.5,ax=axs['pitch'][1])

# nodes4 = pitch.scatter(shbp.pos_x,shbp.pos_y,
#                               s=50,color='#0000e6', label = 'Shot into the bar/post',
#                               edgecolors='#323232',linewidth=1,alpha=1,
#                               zorder=1.5,ax=axs['pitch'][1])        

legend = axs['pitch'][1].legend(facecolor='black', edgecolor='None',
                             loc='lower center', labelcolor = 'white', handlelength=4)

for text in legend.get_texts():
    text.set_fontsize(13)
    
URL = 'https://github.com/googlefonts/robotoslab/blob/main/fonts/static/RobotoSlab-Bold.ttf?raw=true'
URL2 = 'https://github.com/googlefonts/robotoslab/blob/main/fonts/static/RobotoSlab-Light.ttf?raw=true'
URL3 = "https://github.com/clxrse/open_mod/blob/main/Oxygen/Oxygen-Bold.ttf?raw=true"
font_regular = FontManager(URL2)
font_bold = FontManager(URL)
font_label = FontManager(URL3)
        
TITLE_STR1 = 'Nicolas Pepe - Progressive Pass Receiving Points & Shot Map'
TITLE_STR2 = '<Left Pitch> Heat Map of Progressive Pass Receiving Points and\n<Right Pitch> Different Shot Outcomes'
title1_text = axs['title'].text(0.5, 0.7, TITLE_STR1, fontsize=22, color='white',
                                ha='center', va='center',fontproperties=font_bold.prop)
highlight_text = [{'color': '#800610'},
                  {'color': '#08306b'}]
ax_text(0.5, 0.3, TITLE_STR2, ha='center', va='center', fontsize=18, color='white',
        highlight_textprops=highlight_text, ax=axs['title'], fontproperties=font_bold.prop)

axs['endnote'].text(1, 0.5, '@pvk_21', va='center', ha='right', fontsize=15,
                    color='white')

PL_LOGO_URL = 'https://www.snnow.ca/wp-content/uploads/2017/06/sn-now-epl-logo-white-small.png'
pl_logo = Image.open(urlopen(PL_LOGO_URL))
ax1_sb_logo = add_image(pl_logo, fig, left=0.6770,
                       # set the bottom and height to align with the endnote
                       bottom=axs['endnote'].get_position().y0,
                       height=axs['endnote'].get_position().height)

sb_logo = plt.imread('/Your Path/Arsenal-symbol.jpeg')
ax_sb_logo = add_image(sb_logo, fig, left=0.7370,
                       # set the bottom and height to align with the endnote
                       bottom=axs['endnote'].get_position().y0,
                       height=axs['endnote'].get_position().height)
