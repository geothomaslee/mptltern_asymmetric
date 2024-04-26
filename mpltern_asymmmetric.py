#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:09:13 2024

@author: thomaslee
"""

import matplotlib.pyplot as plt
import mpltern as mpl
import numpy as np


def main():
    # Synthetic data just as an example
    H2O = np.random.rand(1,5) * 10
    CO2 = np.random.rand(1,5) * 20
    St = np.random.rand(1,5) * 15
    
    # Calculating each axis
    top = np.divide(H2O,St)[0]
    left = np.divide(H2O,CO2)[0]
    right = np.divide(CO2,St)[0]
    
    # See explanation below for margin, but this tries to avoid any of the data
    # plotting directly on an axis
    margin = 0.1
    
    # Values are always normalized to ternary_sum, and you cannot limit
    # your axes to GREATER than the ternary_sum. I find it easiest to just use
    # the maximum value between all the different data values, plus a 10% margin
    # just so things don't get too tight
    ternary_sum = margin*np.max([np.max(top),np.max(left),np.max(right)])
    
    # Initiate an axis with the ternary projection and aforementioned
    # ternary sum
    ax = plt.subplot(projection='ternary',ternary_sum=ternary_sum)
    
    # Scattering the data
    # Auto plots as blue circles, but standard matplotlib plotting symbol rules
    # should work totally fine here
    ax.scatter(top,left,right,label='Synthetic Data')
    
    legend = ax.legend(loc='upper right',
                       handletextpad=0.3,
                       fontsize=8)
    
    # Correction here to offset the legend, otherwise it will plot on top of
    # the actual graph which sucks
    bb = legend.get_bbox_to_anchor().transformed(ax.transAxes.inverted())
    xOffset = 0.1
    bb.x0 += xOffset
    bb.x1 += xOffset
    legend.set_bbox_to_anchor(bb,transform = ax.transAxes)
    
    # For subscript and superscript, wrap the string in $ $, then _ for subscript 
    # and ^ for superscript, then wrap the text that needs to be in the script
    # with {}
    ax.set_tlabel('$H_{2}$O / $S_{t}$')
    ax.set_rlabel('$CO_{2}$ / $S_{t}$')
    ax.set_llabel('$H_{2}$O / $CO_{2}$')
    
    # Remove these lines and it will plot on the corner, tick1 makes it plot
    # along the axis
    ax.taxis.set_label_position('tick1')
    ax.laxis.set_label_position('tick1')
    ax.raxis.set_label_position('tick1')

    # This is order sensitive, make sure you do top, left, right
    ax.grid()
    
    plt.show()



if __name__ == '__main__':
    main()


