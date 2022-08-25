# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import pandas as pd
import matplotlib.pyplot as plt

model_type = sys.argv[1]
v_init = float(sys.argv[2])
stim_amp = float(sys.argv[3])

def extract_FI_data(filepath, col):
    '''
    Extract and return spike data from excel sheet
    '''
    xlsx_data = pd.read_excel(filepath)
    trace = {
        "T": xlsx_data["t"],
        "V": xlsx_data[col],
    }
    return trace

if model_type == "strong":
    filename = "data_Original_SA_FI_"
elif model_type == "weak1":
    filename = "data_Original_WA1_FI_"
elif model_type == "weak2":
    filename = "data_Original_WA2_FI_"
else:
    raise Exception ("Invalid model type")
filename = filename + str(v_init) + ".xlsx"
filepath = os.path.join(".", "data", filename)
trace = extract_FI_data(filepath, stim_amp)

# plot data and save figure
plt.figure(figsize=(5, 3))
fig = plt.gcf()
plt.plot(trace["T"], trace["V"], '-r')
plt.title("Model: {}, v_init: {} mV, stim_amp: {} pA".format(model_type, v_init, stim_amp))
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
# plt.xlim(0.0, 1200.0)
# plt.ylim(-80, 30)
fig.tight_layout()
fig_name = os.path.join(".", "data", "model_{}_vinit_{}_stim{}.pdf".format(model_type, str(v_init), str(stim_amp)))
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()