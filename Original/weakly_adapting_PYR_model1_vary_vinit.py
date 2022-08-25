'''
Weakly adapting PYR model 1
@author: Ferguson et al. (2014) F1000Res. 
'''
import os, sys
from brian import *

output_directory = os.path.join(".", "data", "vary_v_init")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

v_init = float(sys.argv[1])
stim_amp = float(sys.argv[2])
stim_start = float(sys.argv[3])

defaultclock.dt = 0.02*ms

#Weakly adapting PYR parameters for model 1  
C=300 * pF
vr=-61.8 * mV
vpeak=22.6 * mV
c=-65.8 * mV
klow=0.5 * nS/mV
khigh=3.3  * nS/mV
a= 0.001 /ms
d=5 * pA
vt=-57.0 *mV
b=3 * nS

N=1   #number of cells
mean_Iapp=stim_amp #mean Iapplied input (pA) 
Ishift_raw=-45  #Ishift (pA)

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
PYR.v = v_init * mV
# PYR.v = rand(len(PYR))*0.01 -0.065

#record all spike times for the neuron group
PYR_v = StateMonitor(PYR, 'v', record=True)

#run for x seconds of simulated time
duration1 = stim_start * second
duration2 = 1.0 * second
duration3 = 0.1 * second + defaultclock.dt # to include t = 1200 ms

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
filename = "data_Original_WA1_vinit_" + str(v_init) + "_amp_" + str(stim_amp) + "_t_" + str(stim_start) + ".xlsx"
df.to_excel(os.path.join(output_directory, filename), index = False)

####make voltage plot####
plot(PYR_v.times/ms, PYR_v[0]/mV)
xlabel("Time (ms)")
ylabel("Membrane Potential (mV)")
title('Weakly adapting PYR model #1 with %d pA input and v_init=%0.1f mV'%(mean_Iapp, v_init))
show()