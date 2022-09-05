# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import pandas as pd
import matplotlib.pyplot as plt

potential = sys.argv[1]

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


# Load Brian1 data from xlsx file
data_Brian1_SA  = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_strong_depol_" + potential + ".xlsx"))
data_Brian1_WA1 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak1_depol_" + potential + ".xlsx"))
data_Brian1_WA2 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak2_depol_" + potential + ".xlsx"))

# Load Brian2 data from xlsx file
data_Brian2_SA  = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_strong_depol_" + potential + ".xlsx"))
data_Brian2_WA1 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak1_depol_" + potential + ".xlsx"))
data_Brian2_WA2 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak2_depol_" + potential + ".xlsx"))

# Load Neuron data from xlsx file
data_Neuron_SA  = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_strong_depol_" + potential + ".xlsx"))
data_Neuron_WA1 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak1_depol_" + potential + ".xlsx"))
data_Neuron_WA2 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak2_depol_" + potential + ".xlsx"))


# plot data and save figure
plt.figure(figsize=(10, 10))
fig = plt.gcf()

ax =plt.subplot(3, 3, 1)
ax.text(-0.1, 1.15, "A", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '-r')
plt.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '--b')
plt.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], '-.g')
plt.title("Pyr_Strong: first spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(10.0, 30.0)
plt.ylim(-70, 30)

ax =plt.subplot(3, 3, 2)
ax.text(-0.1, 1.15, "B", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '-r')
plt.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '--b')
plt.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], '-.g')
plt.title("Pyr_Strong: second spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(30.0, 50.0)
plt.ylim(-70, 30)

ax =plt.subplot(3, 3, 3)
ax.text(-0.1, 1.15, "C", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '-r')
plt.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '--b')
plt.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], '-.g')
plt.title("Pyr_Strong: third spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(920.0, 940.0)
plt.ylim(-70, 30)


ax = plt.subplot(3, 3, 4)
ax.text(-0.1, 1.15, "D", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '-r')
plt.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '--b')
plt.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], '-.g')
plt.title("Pyr_Weak1: first spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(110.0, 130.0)
plt.ylim(-70, 30)

ax = plt.subplot(3, 3, 5)
ax.text(-0.1, 1.15, "E", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '-r')
plt.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '--b')
plt.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], '-.g')
plt.title("Pyr_Weak1: second spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(280.0, 300.0)
plt.ylim(-70, 30)

ax = plt.subplot(3, 3, 6)
ax.text(-0.1, 1.15, "F", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '-r')
plt.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '--b')
plt.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], '-.g')
plt.title("Pyr_Weak1: third spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(780.0, 800.0)
plt.ylim(-70, 30)

ax = plt.subplot(3, 3, 7)
ax.text(-0.1, 1.15, "G", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '-r')
plt.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '--b')
plt.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], '-.g')
plt.title("Pyr_Weak2: first spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(110.0, 130.0)
plt.ylim(-70, 30)

ax = plt.subplot(3, 3, 8)
ax.text(-0.1, 1.15, "G", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '-r')
plt.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '--b')
plt.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], '-.g')
plt.title("Pyr_Weak2: second spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(280.0, 300.0)
plt.ylim(-70, 30)

ax = plt.subplot(3, 3, 9)
ax.text(-0.1, 1.15, "G", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '-r')
plt.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '--b')
plt.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], '-.g')
plt.title("Pyr_Weak2: third spike")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (mV)")
#plt.xlim(780.0, 800.0)
plt.ylim(-70, 30)

fig.tight_layout()
fig_name = os.path.join(output_directory, "script_08_compare_spike_shape_{}.pdf".format(potential))
fig.legend(['Brian1', 'Brian2', 'NEURON'], loc='upper center', bbox_to_anchor=(0.5, -0.005),
          fancybox=True, shadow=True, ncol=5)
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()