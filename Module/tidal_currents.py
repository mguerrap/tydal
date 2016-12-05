import numpy as np

def tidal_currents(T,a1,a2,alpha,L,H,time):
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
    Outputs: u_t = depth average current at several times between 0 and 4T
    u_time = depth average current at time"""
    g = 9.81
    T = T*3600 #pass period to seconds
    w = 2*np.pi/T
    dt = T/100
    t = np.arange(0,4*T,dt)
    t_single = time*T
    u_t = g*a1/L*1/w*np.sin(w*t)-g*a2/L*1/w*np.sin(w*t+alpha)
    u_single = g*a1/L*1/w*np.sin(w*t_single)-g*a2/L*1/w*np.sin(w*t_single+alpha)

    return(u_t, u_single, t)

