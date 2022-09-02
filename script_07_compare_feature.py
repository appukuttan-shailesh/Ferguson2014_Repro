# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import json
import pandas as pd
import matplotlib.pyplot as plt

feature = sys.argv[1]

output_directory = os.path.join(".", "Results", "_".join(sys.argv[0].split("_")[0:2]))
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

v_init = -65.0 # mV
# feature list for reference
features_list = [
				'spikecount', 
				'time_to_first_spike', 
				'time_to_second_spike', 
				'time_to_last_spike', 
				'AP1_amp', 
				'AP2_amp', 
				'APlast_amp', 
				'AP1_width', 
				'AP2_width', 
				'APlast_width', 
				'iv_curve'
			]
models = ["Strongly_Adapting_PYR_Model", "Weakly_Adapting_PYR_Model_1", "Weakly_Adapting_PYR_Model_2"]

testname = "Test_for_{}".format(feature)
test_dir = os.path.join(".", "Results", "eFELfeatureTest", testname)

Brian1_vals = {}
Brian2_vals = {}
NEURON_vals = {}

for model in models:
    # Load Brian1 data
    Brian1_test_summary = os.path.join(test_dir, "{}_{}_{}".format("Brian1", model, str(v_init)), "test_summary.json")
    with open(Brian1_test_summary) as f:
        data = json.load(f)
    Brian1_vals[model] = data["prediction"]
    
    # Load Brian2 data
    Brian2_test_summary = os.path.join(test_dir, "{}_{}_{}".format("Brian2", model, str(v_init)), "test_summary.json")
    with open(Brian2_test_summary) as f:
        data = json.load(f)
    Brian2_vals[model] = data["prediction"]
    
    # Load NEURON data
    NEURON_test_summary = os.path.join(test_dir, "{}_{}_{}".format("NEURON", model, str(v_init)), "test_summary.json")
    with open(NEURON_test_summary) as f:
        data = json.load(f)
    NEURON_vals[model] = data["prediction"]


# plot data and save figure
plt.figure(figsize=(10, 4))
fig = plt.gcf()

min_I = min([int(float(x["i_inj"].split(" ")[0])) for x in Brian1_vals[models[0]]])
max_I = max([int(float(x["i_inj"].split(" ")[0])) for x in Brian1_vals[models[0]]])

ax =plt.subplot(1, 3, 1)
ax.text(-0.1, 1.15, "A", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian1_vals[models[0]]], [float(x["value"].split(" ")[0]) for x in Brian1_vals[models[0]]], '-r', linewidth=3.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian2_vals[models[0]]], [float(x["value"].split(" ")[0]) for x in Brian2_vals[models[0]]], '--b', linewidth=2.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in NEURON_vals[models[0]]], [float(x["value"].split(" ")[0]) for x in NEURON_vals[models[0]]], '-.g', linewidth=1.0)
plt.title("Pyr_Strong")
ax.set_xticks(range(min_I, max_I+1,20))
ax.grid(True, linestyle = '--')
plt.xlim(min_I, max_I)
plt.xlabel("I_inj (pA)")
# plt.ylabel("Feature")
plt.ylabel("Peak voltage (mV)")

ax = plt.subplot(1, 3, 2)
ax.text(-0.1, 1.15, "B", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian1_vals[models[1]]], [float(x["value"].split(" ")[0]) for x in Brian1_vals[models[1]]], '-r', linewidth=3.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian2_vals[models[1]]], [float(x["value"].split(" ")[0]) for x in Brian2_vals[models[1]]], '--b', linewidth=2.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in NEURON_vals[models[1]]], [float(x["value"].split(" ")[0]) for x in NEURON_vals[models[1]]], '-.g', linewidth=1.0)
plt.title("Pyr_Weak1")
ax.set_xticks(range(min_I, max_I+1,20))
ax.grid(True, linestyle = '--')
plt.xlim(min_I, max_I)
plt.xlabel("I_inj (pA)")
# plt.ylabel("Feature")
plt.ylabel("Peak voltage (mV)")

ax = plt.subplot(1, 3, 3)
ax.text(-0.1, 1.15, "C", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian1_vals[models[2]]], [float(x["value"].split(" ")[0]) for x in Brian1_vals[models[2]]], '-r', linewidth=3.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in Brian2_vals[models[2]]], [float(x["value"].split(" ")[0]) for x in Brian2_vals[models[2]]], '--b', linewidth=2.0)
plt.plot([float(x["i_inj"].split(" ")[0]) for x in NEURON_vals[models[2]]], [float(x["value"].split(" ")[0]) for x in NEURON_vals[models[2]]], '-.g', linewidth=1.0)
plt.title("Pyr_Weak2")
ax.set_xticks(range(min_I, max_I+1,20))
ax.grid(True, linestyle = '--')
plt.xlim(min_I, max_I)
plt.xlabel("I_inj (pA)")
# plt.ylabel("Feature")
plt.ylabel("Peak voltage (mV)")

fig.tight_layout()
fig_name = os.path.join(output_directory, "script_07_compare_{}.png".format(feature))
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()