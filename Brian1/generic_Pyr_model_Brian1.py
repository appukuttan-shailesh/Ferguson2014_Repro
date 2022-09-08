'''
Brian(1) simulator implementation of CA1 PYR model
SciUnit-based model wrapper for both strong and weak adaptation
Implemented by: Shailesh Appukuttan (CNRS), August 2022

Original work: 
Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)
Simple, biologically-constrained CA1 pyramidal cell models 
using an intact, whole hippocampus context . 
F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) 
'''

import sciunit
import eFELunit.capabilities as cap
from brian import *

class CA1_Pyr_Brian1_Template(sciunit.Model,
                              cap.SomaReceivesCurrentProducesMembranePotential):
    '''
    Create a PYR model with the specified parameters
    '''

    def __init__(self, name="Brian1 CA1 Pyr Model", type=None, v_init=None, params=None):
        if type:
            # common params for all types
            self.vr = -61.8 * mV
            self.vt = -57.0 * mV
            self.c = -65.8 * mV
            self.vpeak = 22.6 * mV
            self.khigh = 3.3 * nS/mV
            self.b = 3 * nS
            if type == "strong":
                name = "Brian1 Strongly Adapting PYR Model"
                self.C = 115 * pF
                self.a = 0.0012 / ms
                self.d = 10 * pA
                self.klow = 0.1 * nS/mV
                self.Ishift = 0 * pA
            elif type == "weak1":
                name = "Brian1 Weakly Adapting PYR Model 1"
                self.C = 300 * pF
                self.a = 0.001 / ms
                self.d = 5 * pA
                self.klow = 0.5 * nS/mV
                self.Ishift = -45 * pA
            elif type == "weak2":
                name = "Brian1 Weakly Adapting PYR Model 2"
                self.C = 300 * pF
                self.a = 0.00008 / ms
                self.d = 5 * pA
                self.klow = 0.5 * nS/mV
                self.Ishift = -45 * pA
            else:
                raise Exception("Model type not recognized! Valid options are 'strong', 'weak1', 'weak2'")
        else:
            # for creating custom variant of model
            if params:
                self.vr = params['vr']
                self.vt = params['vt']
                self.c = params['c']
                self.vpeak = params['vpeak']
                self.b = params['b']
                self.C = params['C']
                self.a = params['a'],
                self.d = params['d']
                self.khigh = params['khigh']
                self.klow = params['klow']
                self.Ishift = params['Ishift']

        if v_init:
            self.name = name + "_" + str(v_init)
            self.v_init = v_init * mV
        else:
            self.name = name
            # default value for v_init
            self.v_init = -65.0 * mV
        sciunit.Model.__init__(self, self.name)

        # handle namespace for Brian
        locals().update(vars(self))
    
        pyr_eqs = """
            Iinj : amp
            stim_start : second
            stim_stop : second
            Iext=(t>=stim_start)*(t<stim_stop)*Iinj : amp
            k=(v<vt)*klow+(v>=vt)*khigh : (siemens/volt)
            du/dt = a*(b*(v-vr)-u) : amp
            dv/dt = (k*(v-vr)*(v-vt)+Ishift+Iext -u)/C : volt
        """
        self.model = NeuronGroup(1, model = pyr_eqs, reset ="v = c; u += d" , threshold="v>=vpeak")
        
        # neuron initial condition
        self.model.v = self.v_init
    
    def reset_model(self):
        # reset the simulation
        reinit()
        self.model.reinit()
        # neuron initial condition
        self.model.v = self.v_init

    def inject_soma_square_current(self, current):
        # specify stimulus current
        I_applied = current["amplitude"] * pA
        self.model.Iinj = I_applied
        self.model.stim_start = current["delay"] * ms
        self.model.stim_stop = (current["delay"] + current["duration"]) * ms

    def get_soma_vm(self, tstop, dt = 0.02):
        # run simulation and record membrane potential of neuron

        # Brian2 default dt is 0.1 * ms
        defaultclock.dt = dt * ms 

        # record membrane potential of neuron
        monitor_v = StateMonitor(self.model, 'v', record=True)

        # run simulation
        duration = tstop * ms + defaultclock.dt # to include final time step
        net = Network(self.model, monitor_v)
        net.run(duration)

        # return values
        return {'T': monitor_v.times/ms, 'V': monitor_v[0]/mV}  

    def run_sample_sim(self):
        # Brian1 default dt is 0.1 * ms
        defaultclock.dt = 0.02 * ms 

        # specify stimulus current
        I_applied = 140.0
        self.model.Iinj = I_applied * pA
        self.model.stim_start = 0 * ms
        self.model.stim_stop = 1000 * ms

        # record membrane potential of neuron
        monitor_v = StateMonitor(self.model, 'v', record=True)

        # run simulation
        duration = 1000 * ms + defaultclock.dt # to include final time step
        net = Network(self.model, monitor_v)
        net.run(duration)

        # generate plot
        plot(monitor_v.times/ms, monitor_v[0]/mV)
        xlabel("Time (ms)")
        ylabel("Membrane Potential (mV)")
        title('%s with %d pA input'%(self.name, I_applied))
        show()


# pyr = CA1_Pyr_Brian1_Template(type='strong')
# print(pyr.name)
# print(pyr.model)
# pyr.run_sample_sim()