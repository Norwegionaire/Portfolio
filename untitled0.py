# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:27:22 2024

@author: engeb
"""

import matplotlib.pyplot as plt

#fig = plt.figure()

#fig, ax = plt.subplots(nrows=2,ncols=2)

fig, ax = plt.subplots(figsize=(3, 2))
ax.plot([0,1,2],[2,4,6])
ax.plot([0,1,2],[3,6,9])
plt.show()