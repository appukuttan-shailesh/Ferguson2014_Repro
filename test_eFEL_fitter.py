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

base_directory = os.path.join(".", simulator, "data")
filepath = os.path.join(base_directory, "data_{}_{}_depol_{}.xlsx".format(simulator, model, potential))
xlsx_data = pd.read_excel(filepath)
data_eFEL = {
        "T": xlsx_data["t"],
        "V": xlsx_data["v"],
        "stim_start": [xlsx_data["t"].values[0]],
        "stim_end": [xlsx_data["t"].values[-1]],
    }
flag = True
for thres in range(-30, 50, 5):
  for downthres in range(-30, 50, 5):
    for downderivthres in range(-30, -5, 5):
      for derivWindow in range (1, 15, 1):
        efel.reset()
        efel.setDoubleSetting('Threshold', thres) # default: -20.0
        efel.setDoubleSetting('DerivativeThreshold', downthres) #default: 10.0
        efel.setDoubleSetting('DownDerivativeThreshold', downderivthres) #default: -12.0
        efel.setIntSetting('DerivativeWindow', derivWindow) #default: 3
        
        feature_vals = efel.getFeatureValues([data_eFEL], [feature, "time", "peak_indices"])
        if len(feature_vals[0]["AP1_peak"])>0 and feature_vals[0]["AP1_peak"][0]>10.0 and len(feature_vals[0]["peak_indices"])>10:
            print(thres, downthres, downderivthres)
            print(feature_vals)