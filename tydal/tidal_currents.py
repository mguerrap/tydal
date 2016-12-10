import numpy as np

def tidal_currents(T,a1,a2,alpha):
    """Function estimates a depth averaged velocity
    for a simple tidal channel
    Inputs: T = Tide period (hours)
    a1 = tidal amplitude ocean side (m)
    a2 = tidal amplitude estuary side (m)
    alpha = a phase difference in degrees (º)
    L = channel length (m)
    H = channel depth (m) 
    time = time at which to estimate the current,
    a number between 0 and 1, it corresponds to a stage in the tide
    Outputs: u_t = depth average current at several times between 0 and 4T"""
    g = 9.81
    L = 200000
    H = 200
    T = T*3600 #pass period to seconds
    w = 2*np.pi/T
    dt = T/100
    t = np.arange(0,4*T,dt)
    u_t = g*a1/L*1/w*np.sin(w*t)-g*a2/L*1/w*np.sin(w*t+alpha)
    return(u_t, t)

