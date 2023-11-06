#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 3 10:14:15 2023

@author: liming
"""

import matplotlib.pyplot as plt
import numpy as np

D = np.linspace(0, 3E-10, 50)
def w_vdw(D):
    term1 = -((1.4E-20)/6) * ((2 * R * R) / ((4 * R + D) * D))
    term2 = -((1.4E-20)/6) * (2 * R * R) / ((2 * R + D) * (2 * R + D))
    term3 = -((1.4E-20)/6) * np.log(((4 * R + D) * D) / ((2 * R + D) * (2 * R + D)))
    return term1 + term2 + term3

for R in [1E-9, 10E-9, 50E-9, 100E-9, 200E-9, 1000E-9]:
    vdw_values = w_vdw(D)


    plt.figure(figsize=(8, 6))
    plt.plot(D, vdw_values, label='R = 50E-9')
    plt.title('Plot of Van der Waals potential as a function of D')
    plt.xlabel('D (distance)')
    plt.ylabel('w(D)vdw (potential energy)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()
