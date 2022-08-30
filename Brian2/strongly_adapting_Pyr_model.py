'''
Brian2 implementation of strongly adapting CA1 PYR model
Implemented by: Shailesh Appukuttan (CNRS), August 2022

Original work: 
Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)
Simple, biologically-constrained CA1 pyramidal cell models 
using an intact, whole hippocampus context . 
F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) 
'''

from brian2 import *

# Brian2 default dt is 0.1 * ms
defaultclock.dt = 0.02 * ms 

#Strongly adapting model parameters
vr = -61.8 * mV
vt = -57.0 * mV
c = -65.8 * mV
vpeak = 22.6 * mV
Cm = 115 * pF
a = 0.0012 / ms
b = 3 * nS
d = 10 * pA
khigh = 3.3 * nS/mV
klow = 0.1 * nS/mV

I_shift = 0 * pA
I_applied = 100 * pA

model_eqs = """
    Iext  : amp
    Ishift : amp
    k=(int(v<vt)*klow)+(int(v>=vt)*khigh) : siemens/volt
    du/dt = a*(b*(v-vr)-u)            : amp
    dv/dt = (k*(v-vr)*(v-vt)+Ishift+Iext -u)/Cm : volt
"""

thres_eq = 'v>=vpeak'

reset_eqs = '''
    v = c
    u += d
'''

# create a single neuron
model = NeuronGroup(1, model = model_eqs, reset = reset_eqs , threshold = thres_eq, method = 'euler')

# neuron initial condition
model.v = -65.0 * mV
# model.v = vr

# specify stimulus current
model.Iext = I_applied
model.Ishift = I_shift

# record membrane potential of neuron
monitor_v = StateMonitor(model, 'v', record=True)

# run simulation
duration = 1000 * ms + defaultclock.dt # to include final time step
run(duration)

# generate plot
plot(monitor_v.t/ms, monitor_v[0].v/mV)
xlabel("Time (ms)")
ylabel("Membrane Potential (mV)")
title('Strongly adapting model model with %d pA input'%(I_applied))
show()