'''
Strongly adapting PYR model
@author: Ferguson et al. (2014) F1000Res. 
'''
import sys
from brian import *
import numpy as np

v_init = float(sys.argv[1])

defaultclock.dt = 0.02*ms

#Strongly adapting PYR parameters
C=115 * pF
vr=-61.8 * mV
vpeak=22.6 * mV
c=-65.8 * mV
klow=0.1 * nS/mV
khigh=3.3  * nS/mV
a=0.0012 /ms
d=10 * pA
vt=-57.0 *mV
b=3 * nS

N=1   #number of cells
Ishift_raw=0  # Ishift

time=0

#cell eqns
pyr_eqs = """
Iext  : amp
Ishift : amp
k=(v<vt)*klow+(v>=vt)*khigh : (siemens/volt)
du/dt = a*(b*(v-vr)-u)            : amp
dv/dt = (k*(v-vr)*(v-vt)+Ishift+Iext -u)/C : volt
"""

#define neuron group
PYR = NeuronGroup(N, model=pyr_eqs, reset ="v = c; u += d" , threshold="v>=vpeak")


#record all spike times for the neuron group
PYR_v = StateMonitor(PYR, 'v', record=True)

# F-I curve range and step size
stim_min = -50.0
stim_max = 300.0
stim_step = 10.0

#run for x seconds of simulated time
duration = 1 * second + defaultclock.dt # to include t = 1000 ms

net =Network(PYR,PYR_v)

# create dict to store data
data = {}

for stim_inj in np.arange(stim_min, stim_max+1, stim_step):
    print("I = {}".format(stim_inj))
    
    # reset the simulation
    reinit()

    #set initial conditions for each neuron
    PYR.v = v_init * mV
    # PYR.v = rand(len(PYR))*0.01 -0.065

    #set Ishift
    PYR.Ishift = Ishift_raw*pA

    #set excitatory drive 
    PYR.Iext = stim_inj*pA    

    # run simulation for specified stimulus
    net.run(duration)

    if stim_inj == stim_min:
        data['t'] = PYR_v.times/ms
    data[stim_inj] = PYR_v[0]/mV

import os
import pandas as pd
df = pd.DataFrame(data)
df.to_excel(os.path.join("data", "data_Original_SA_FI_" + str(v_init) + ".xlsx"), index = False)

print("** Completed **")