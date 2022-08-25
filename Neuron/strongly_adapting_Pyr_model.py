'''
NEURON simulator implementation of CA1 PYR model
Implemented by: Shailesh Appukuttan (CNRS), August 2022

Original work: 
Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)
Simple, biologically-constrained CA1 pyramidal cell models 
using an intact, whole hippocampus context . 
F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) 
'''

from neuron import h, gui

dummy_sec = h.Section()
model = h.Pyr(dummy_sec(0.5))

model.stim_start = 100
model.stim_stop = 900
model.Iinj = 100

t_vec = h.Vector()
i_vec = h.Vector()
v_vec = h.Vector()
t_vec.record(h._ref_t)
i_vec.record(model._ref_Iext)
v_vec.record(model._ref_vm)

h.tstop = 1000
h.v_init = model.v_init

h.run()

from matplotlib import pyplot
fig = pyplot.figure(figsize=(8,12))
def mouse_event(event):
   print('x: {} and y: {}'.format(event.xdata, event.ydata))
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)

pyplot.suptitle("Strongly adapting PYR model", fontsize=16, fontweight='bold')
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