from brian import *

class SampleClass():
    def __init__(self, name="CA1 Pyr Model", type=None, params=None):
        tau = 20 * msecond        # membrane time constant
        Vt = -50 * mvolt          # spike threshold
        Vr = -60 * mvolt          # reset value
        El = -60 * mvolt          # resting potential
        model_eqs = """
            dV/dt = -(V-El)/tau : volt
        """
        self.model = NeuronGroup(1, model=model_eqs, 
                                reset='Vr', 
                                threshold = 'Vt')

myobj = SampleClass()

import multiprocessing
# import pathos.multiprocessing as multiprocessing
import functools

def myfunc(model, amp, tstop):
    print(model.name, amp, tstop)
    return model.v

amps = [0, 1, 2, 3, 4, 5]

pool = multiprocessing.Pool(multiprocessing.cpu_count() - 1, maxtasksperchild=1)
cclamp_ = functools.partial(myfunc, myobj.model, tstop = 1000)
results = pool.map(cclamp_, amps, chunksize=1)
print(results)