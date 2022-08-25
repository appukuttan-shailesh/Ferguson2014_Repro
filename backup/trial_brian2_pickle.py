from brian2 import *

class SampleClass():
    def __init__(self, name="CA1 Pyr Model", type=None, params=None):
        model_eqs = """
            dv/dt = 0 : volt
        """
        self.model = NeuronGroup(1, model=model_eqs, 
                                reset='v = -65', 
                                threshold = 'v>=vpeak', 
                                method = 'euler')

myobj = SampleClass()

# import multiprocessing
import pathos.multiprocessing as multiprocessing
import functools

def myfunc(model, amp, tstop):
    print(model.name, amp, tstop)
    return model.v

amps = [0, 1, 2, 3, 4, 5]

pool = multiprocessing.Pool(multiprocessing.cpu_count() - 1, maxtasksperchild=1)
cclamp_ = functools.partial(myfunc, myobj.model, tstop = 1000)
results = pool.map(cclamp_, amps, chunksize=1)
print(results)