'''
NEURON simulator implementation of CA1 PYR model
SciUnit-based model wrapper for both strong and weak adaptation
Implemented by: Shailesh Appukuttan (CNRS), August 2022

Original work: 
Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)
Simple, biologically-constrained CA1 pyramidal cell models 
using an intact, whole hippocampus context . 
F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) 
'''

import os
from pathlib import Path
import sciunit
import eFELunit.capabilities as cap
from neuron import h, gui

class CA1_Pyr_Neuron_Template(sciunit.Model,
                              cap.SomaInjectsCurrentProducesMembranePotential):
    '''
    Create a PYR model with the specified parameters
    '''

    def __init__(self, name="NEURON CA1 Pyr Model", type=None, v_init=None, params=None, mod_files_path=None):
        if type:
            # common params for all types
            self.vr = -61.8 # mV
            self.vt = -57.0 # mV
            self.c = -65.8 # mV
            self.vpeak = 22.6 # mV
            self.khigh = 3.3 # nS/mV
            self.b = 3 # nS
            if type == "strong":
                name = "NEURON Strongly Adapting PYR Model"
                self.Cm = 115 # pF
                self.a = 0.0012 # /ms
                self.d = 10 # pA
                self.klow = 0.1 # nS/mV
                self.Ishift = 0 # pA
            elif type == "weak1":
                name = "NEURON Weakly Adapting PYR Model 1"
                self.Cm = 300 # pF
                self.a = 0.001 # /ms
                self.d = 5 # pA
                self.klow = 0.5 # nS/mV
                self.Ishift = -45 # pA
            elif type == "weak2":
                name = "NEURON Weakly Adapting PYR Model 2"
                self.Cm = 300 # pF
                self.a = 0.00008 # /ms
                self.d = 5 # pA
                self.klow = 0.5 # nS/mV
                self.Ishift = -45 # pA
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
                self.Cm = params['Cm']
                self.a = params['a'],
                self.d = params['d']
                self.khigh = params['khigh']
                self.klow = params['klow']
                self.Ishift = params['Ishift']

        if v_init:
            self.name = name + "_" + str(v_init)
            self.v_init = v_init # mV
        else:
            self.name = name
            # default value for v_init
            self.v_init = -65.0 # mV
        sciunit.Model.__init__(self, self.name)

        if not mod_files_path:
            mod_files_path = Path(__file__).absolute().parent
        self.mod_files_path = mod_files_path
        self.libpath = os.path.join(self.mod_files_path, 'x86_64/.libs/libnrnmech.so')
        self.compile_mod_files()
        if str(mod_files_path) != str(os.getcwd()):
            self.load_mod_files()

        self.dummy_sec = h.Section()
        self.model = h.Pyr(self.dummy_sec(0.5))

        # set model parameters
        self.model.vr = self.vr
        self.model.vt = self.vt
        self.model.c = self.c
        self.model.vpeak = self.vpeak
        self.model.b = self.b
        self.model.Cm = self.Cm
        self.model.a = self.a
        self.model.d = self.d
        self.model.khigh = self.khigh
        self.model.klow = self.klow
        self.model.Ishift = self.Ishift

        # neuron initial condition
        self.model.v_init = self.v_init
        h.v_init = self.v_init

    def compile_mod_files(self):
        if self.mod_files_path is None:
            raise Exception(
                "Please give the path to the mod files (eg. mod_files_path = \'/home/models/CA1_pyr/mechanisms/\') as an argument to the ModelLoader class")
        if os.path.isfile(os.path.join(self.mod_files_path, self.libpath)) is False:
            print(os.path.isfile(os.path.join(self.mod_files_path, self.libpath)))
            os.system("cd " + "\'" + str(self.mod_files_path) +
                      "\'" + "; nrnivmodl")

    def load_mod_files(self):
        status = h.nrn_load_dll(os.path.join(self.mod_files_path, self.libpath))
        print("nrn_load_dll: {}".format("success" if status==1 else "fail"))

    def reset_model(self):
        # neuron initial condition
        self.model.v_init = self.v_init # mV
        h.v_init = self.v_init # mV

    def inject_soma_square_current(self, current):
        # specify stimulus current
        I_applied = current["amplitude"]
        self.model.Iinj = I_applied
        self.model.stim_start = current["delay"]
        self.model.stim_stop = current["delay"] + current["duration"]

    def get_soma_vm(self, tstop, dt = 0.02):
        # run simulation and record membrane potential of neuron

        # NEURON default dt is 0.025 * ms
        h.dt = dt

        # record membrane potential of neuron
        t_vec = h.Vector()
        v_vec = h.Vector()
        t_vec.record(h._ref_t)
        v_vec.record(self.model._ref_vm)

        # run simulation
        h
        h.tstop = tstop
        h.run()
    
        # return values
        return {'T': t_vec.to_python(), 'V': v_vec.to_python()}  

    def run_sample_sim(self):
        self.model.stim_start = 100
        self.model.stim_stop = 900
        self.model.Iinj = 100

        t_vec = h.Vector()
        i_vec = h.Vector()
        v_vec = h.Vector()
        t_vec.record(h._ref_t)
        i_vec.record(self.model._ref_Iext)
        v_vec.record(self.model._ref_vm)

        h.tstop = 1000
        h.v_init = self.model.vm

        h.run()

        from matplotlib import pyplot
        fig = pyplot.figure(figsize=(8,12))
        pyplot.suptitle(self.name, fontsize=16, fontweight='bold')

        pyplot.subplot(2,1,1)
        pyplot.plot(t_vec, i_vec)
        pyplot.margins(x=0.0, y=0.1)
        pyplot.title('Current Input')
        pyplot.xlabel('Time (s)')
        pyplot.ylabel('Input Stimulus (pA)')

        pyplot.subplot(2,1,2)
        pyplot.plot(t_vec, v_vec)
        pyplot.margins(x=0.0, y=0.1)
        pyplot.title('Voltage Response')
        pyplot.xlabel('Time (s)')
        pyplot.ylabel('Membrane Potential (mV)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.92)
        pyplot.show()


# pyr = CA1_Pyr_Neuron_Template(type='strong')
# print(pyr.name)
# print(pyr.model)
# pyr.run_sample_sim()