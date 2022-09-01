# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import pandas as pd
import matplotlib.pyplot as plt

output_directory = os.path.join(".", "Results", "_".join(sys.argv[0].split("_")[0:2]))
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


def read_data(filepath):
    '''
    Return spike data from excel sheet
    '''
    xlsx_data = pd.read_excel(filepath)
    data = {
        "T": xlsx_data["t"],
        "V": xlsx_data["v"],
    }
    return data


# Load Original data from xlsx file
data_Original_SA  = read_data(os.path.join(".", "Original", "data", "data_Original_SA_hyperpol_-50.0.xlsx"))
data_Original_WA1 = read_data(os.path.join(".", "Original", "data", "data_Original_WA1_hyperpol_-1000.0.xlsx"))
data_Original_WA2 = read_data(os.path.join(".", "Original", "data", "data_Original_WA2_hyperpol_-1000.0.xlsx"))

# Load Brian1 data from xlsx file
data_Brian1_SA  = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_strong_hyperpol_-50.0.xlsx"))
data_Brian1_WA1 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak1_hyperpol_-1000.0.xlsx"))
data_Brian1_WA2 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak2_hyperpol_-1000.0.xlsx"))

# Load Brian2 data from xlsx file
data_Brian2_SA  = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_strong_hyperpol_-50.0.xlsx"))
data_Brian2_WA1 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak1_hyperpol_-1000.0.xlsx"))
data_Brian2_WA2 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak2_hyperpol_-1000.0.xlsx"))

# Load Neuron data from xlsx file
data_Neuron_SA  = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_strong_hyperpol_-50.0.xlsx"))
data_Neuron_WA1 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak1_hyperpol_-1000.0.xlsx"))
data_Neuron_WA2 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak2_hyperpol_-1000.0.xlsx"))


# plot data and save figure
plt.figure(figsize=(7, 10))
fig = plt.gcf()

ax =plt.subplot(3, 1, 1)
ax.text(-0.1, 1.15, "A", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_SA["T"], data_Original_SA["V"], '-r')
plt.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '--b')
plt.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '-.g')
plt.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], ':m')
plt.title("Strongly adapting model with -50 pA input")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
plt.xlim(0.0, 2000.0)
plt.ylim(-100, 25)

ax = plt.subplot(3, 1, 2)
ax.text(-0.1, 1.15, "B", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_WA1["T"], data_Original_WA1["V"], '-r')
plt.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '--b')
plt.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '-.g')
plt.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], ':m')
plt.title("Weakly adapting model #1 with -1000 pA input")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
plt.xlim(0.0, 2000.0)
plt.ylim(-125, 25)

ax = plt.subplot(3, 1, 3)
ax.text(-0.1, 1.15, "C", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_WA2["T"], data_Original_WA2["V"], '-r')
plt.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '--b')
plt.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '-.g')
plt.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], ':m')
plt.title("Weakly adapting model #2 with -1000 pA input")
ax.legend(['Original', 'Brian1', 'Brian2', 'NEURON'], loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
plt.xlim(0.0, 2000.0)
plt.ylim(-125, 25)

fig.tight_layout()
fig_name = os.path.join(output_directory, "script_03_hyperpol_plot.pdf")
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()