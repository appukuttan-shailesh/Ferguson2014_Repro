import sys
from turtle import delay

model_type = sys.argv[1]
current = { 
    "amplitude" : float(sys.argv[2]),
    "delay" : 100,
    "duration" : 1000 if float(sys.argv[2]) > 0 else 900
}
tstop = 1200 if float(sys.argv[2]) > 0 else 2000

from generic_Pyr_model_Brian1 import CA1_Pyr_Brian1_Template
model = CA1_Pyr_Brian1_Template(type = model_type)
model.inject_soma_square_current(current)
trace = model.get_soma_vm(tstop = tstop)
data = {}
data['t'] = trace["T"]
data['v'] = trace["V"]

import os
import pandas as pd
df = pd.DataFrame(data)
if current["amplitude"] > 0:
    filename = "data_Brian1_{}_depol_{}.xlsx".format(model_type, str(current["amplitude"]))
else:
    filename = "data_Brian1_{}_hyperpol_{}.xlsx".format(model_type, str(current["amplitude"]))
df.to_excel(os.path.join("data", filename), index = False)

print("** Completed **")