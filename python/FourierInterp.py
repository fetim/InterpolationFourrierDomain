#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:00:16 2017

@author: felipe
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

incr_sampling = 20
dt = 0.01
Nt = 100


t = np.linspace(0.0,dt*Nt,Nt)
y = np.exp(-100*(t-0.3)*(t-0.3))

plt.figure(1)
plt.plot(t,y,color='k',linestyle='dashed',marker='o')
plt.show()

Y = scipy.fftpack.rfft(y)


X = np.linspace(0.0,1.0/(2.0*dt),Nt/2)

Y_ex = np.append(Y,np.zeros(incr_sampling*Nt))

plt.figure(2)

plt.plot(X,2.0/Nt*np.abs(Y[:Nt/2]))
plt.show()

y_interp = (incr_sampling+1)*scipy.fftpack.irfft(Y_ex)
t_interp = np.linspace(0.0,dt*Nt,(incr_sampling+1)*Nt)

plt.figure(1)
plt.plot(t,y,color='k',linestyle='dashed',marker='o')
plt.plot(t_interp,y_interp,color='r',marker='o')
plt.show()
