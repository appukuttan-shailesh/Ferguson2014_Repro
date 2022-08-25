'''
Strongly adapting PYR model
@author: Ferguson et al. (2014) F1000Res. 
'''
import sys
from brian import *

stim_amp = float(sys.argv[1])

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
mean_Iapp=stim_amp #mean Iapplied input
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

#set Ishift
PYR.Ishift = Ishift_raw*pA

#set initial conditions for each neuron
PYR.v = -65.0 * mV
# PYR.v = rand(len(PYR))*0.01 -0.065

#record all spike times for the neuron group
PYR_v = StateMonitor(PYR, 'v', record=True)

#run for x seconds of simulated time
if stim_amp > 0:
    duration1 = 0.1 * second
    duration2 = 1.0 * second
    duration3 = 0.1 * second + defaultclock.dt # to include t = 1000 ms
else:
    duration1 = 0.1 * second
    duration2 = 0.9 * second
    duration3 = 1.0 * second + defaultclock.dt # to include t = 1200 ms

net =Network(PYR,PYR_v) 

PYR.Iext = 0*pA
net.run(duration1)
#set excitatory drive 
PYR.Iext = mean_Iapp*pA
net.run(duration2)
PYR.Iext = 0*pA
net.run(duration3)

# create dict to store data
data = {}
data['t'] = PYR_v.times/ms
data['v'] = PYR_v[0]/mV

import os
import pandas as pd
df = pd.DataFrame(data)
if stim_amp > 0:
    filename = "data_Original_SA_depol_" + str(stim_amp) + ".xlsx"
else:
    filename = "data_Original_SA_hyperpol_" + str(stim_amp) + ".xlsx"
df.to_excel(os.path.join("data", filename), index = False)

####make voltage plot####
plot(PYR_v.times/ms, PYR_v[0]/mV)
xlabel("Time (ms)")
ylabel("Membrane Potential (mV)")
title('Strongly adapting PYR model with %d pA input'%(mean_Iapp))
show()