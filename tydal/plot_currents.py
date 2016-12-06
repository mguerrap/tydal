import matplotlib.pyplot as plt
import numpy as np

from tidal_currents import tidal_currents

def plot_currents(T, a1, a2, alpha, N):
    """Plots results of analytical currents,
    plots a time series of u(t), and a dot
    in a specific velocity. Also plots an arrow
    showing the direction of the current and its magnitude
    Inputs: u = time series of u, created using tidal_currents.py
    t = time corresponding to that time series
    T = tidal period used
    t_single = time of location of dot"""
    [u, time] = tidal_currents(T, a1, a2, alpha)
    abs_u = np.absolute(u)
    max_u = np.amax(abs_u)
    u_single = u[N]
    t_single = time[N]
    fig, ax = plt.subplots(2, figsize={10, 4})
    # Arrow showing velocity
    ax[0].set_ylim([-0.5, 0.5])
    ax[0].set_xlim([-max_u-1, max_u+1])
    if u_single > 0:
        ax[0].arrow(0-u_single/2, 0, u_single, 0,
                    head_width=0.1, head_length=0.05, fc='g', ec='g')
        ax[0].text(0, -0.3, 'Flood', horizontalalignment='center', color='g',
        	       verticalalignment='center', fontsize=14, fontweight='bold')
    else:
        ax[0].arrow(0-u_single/2, 0, u_single, 0,
                    head_width=0.1, head_length=0.05, fc='r', ec='r')
        ax[0].text(0, -0.3, 'Ebb', horizontalalignment='center', color='r',
        	       verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(-max_u, 0.3, 'Ocean', horizontalalignment='center',
               verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(max_u, 0.3, 'Estuary', horizontalalignment='center',
               verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(0, 0.45, 'V = ' + str(round(u_single, 1)) + ' m/s',
               horizontalalignment='center', verticalalignment='center',
               fontsize=14, fontweight='bold')
    ax[0].axis('off')
    # Time Series
    ax[1].plot(time/3600, u, color='blue')
    ax[1].plot(t_single/3600, u_single, color='blue', marker='o', markersize=15)
    ax[1].set_xlabel('Time (hours)')
    ax[1].set_ylabel('Velocity (m/s)')
    ax[1].set_ylim([-2.5, 2.5])
    return
