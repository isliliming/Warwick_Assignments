# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:42:47 2023

@author: Liming Li
"""

import numpy
import veusz.embed as veusz

g1 = veusz.Embedded('test01')
g1.EnableToolbar()

g1.To(g1.Add('page'))
g1.To(g1.Add('graph'))
g1.Add('xy', marker='tiehorz', MarkerFill__color='green')

g1.Set('x/autoExtend', False)
g1.Set('x/autoExtendZero', False)

g1.Zoom(0.8)

# create data and plot
for i in range(10):
    x = numpy.arange(0 + i/2., 7. + i/2., 0.05)
    y = numpy.sin(x)
    
    x_data_name = f'x{i}'
    y_data_name = f'y{i}'
    
    g1.SetData(x_data_name, x)
    g1.SetData(y_data_name, y)
    
    g1.Add('xy', xData=x_data_name, yData=y_data_name, marker='tiehorz', MarkerFill__color='green')

    

    



