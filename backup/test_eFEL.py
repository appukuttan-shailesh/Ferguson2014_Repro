# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import efel

simulator = sys.argv[1]
model = sys.argv[2]
potential = sys.argv[3]
feature = sys.argv[4]

def extract_eFEL_feature(filepath, feature):
    '''
    Extract and return spike data from excel sheet
    '''
    xlsx_data = pd.read_excel(filepath)
    efel.reset()
    efel.setDoubleSetting('interp_step', 0.01)
    # efel.setDoubleSetting('Threshold', 10) # default: -20.0
    # efel.setDoubleSetting('DerivativeThreshold', -30.0) #default: 10.0
    # efel.setDoubleSetting('DownDerivativeThreshold', -30.0) #default: -12.0
    # efel.setIntSetting('DerivativeWindow', 100) #default: 3
    data_eFEL = {
        "T": xlsx_data["t"],
        "V": xlsx_data["v"],
        "stim_start": [xlsx_data["t"].values[0]],
        "stim_end": [xlsx_data["t"].values[-1]],
    }
    feature_vals = efel.getFeatureValues([data_eFEL], [feature, "time", "peak_indices", "peak_voltage"])
    print(feature_vals)
    print(len(feature_vals[0]["peak_indices"]))
    return data_eFEL, feature_vals

base_directory = os.path.join("..", simulator, "data")
data_eFEL, feature_vals = extract_eFEL_feature(os.path.join(base_directory, "data_{}_{}_depol_{}.xlsx".format(simulator, model, potential)), feature)
peak_indices = feature_vals[0]["peak_indices"]
times = feature_vals[0]["time"]

plt.figure(figsize=(10, 6))
fig = plt.gcf()
plt.plot(data_eFEL["T"], data_eFEL["V"], '-r')
# plt.vlines(x=[data_eFEL["T"][x] for x in peak_indices], ymin=-70, ymax=30, colors='blue') # incorrect
plt.vlines(x=times[peak_indices], ymin=-70, ymax=30, colors='green')
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
# plt.xlim(20, 22)
plt.ylim(-70, 30)
fig.tight_layout()
plt.show()