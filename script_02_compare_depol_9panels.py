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
data_Original_SA  = read_data(os.path.join(".", "Original", "data", "data_Original_SA_depol_188.0.xlsx"))
data_Original_WA1 = read_data(os.path.join(".", "Original", "data", "data_Original_WA1_depol_154.0.xlsx"))
data_Original_WA2 = read_data(os.path.join(".", "Original", "data", "data_Original_WA2_depol_154.0.xlsx"))

# Load Brian1 data from xlsx file
data_Brian1_SA  = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_strong_depol_188.0.xlsx"))
data_Brian1_WA1 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak1_depol_154.0.xlsx"))
data_Brian1_WA2 = read_data(os.path.join(".", "Brian1", "data", "data_Brian1_weak2_depol_154.0.xlsx"))

# Load Brian2 data from xlsx file
data_Brian2_SA  = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_strong_depol_188.0.xlsx"))
data_Brian2_WA1 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak1_depol_154.0.xlsx"))
data_Brian2_WA2 = read_data(os.path.join(".", "Brian2", "data", "data_Brian2_weak2_depol_154.0.xlsx"))

# Load Neuron data from xlsx file
data_Neuron_SA  = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_strong_depol_188.0.xlsx"))
data_Neuron_WA1 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak1_depol_154.0.xlsx"))
data_Neuron_WA2 = read_data(os.path.join(".", "Neuron", "data", "data_Neuron_weak2_depol_154.0.xlsx"))


# plot data and save figure
plt.figure(figsize=(9, 10))
fig = plt.gcf()

ax1 = plt.subplot2grid((3,5), (0, 0), colspan=3)
ax1.text(-0.15, 1.15, "A", transform=ax1.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax1.plot(data_Original_SA["T"], data_Original_SA["V"], '-r')
ax1.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '--b')
ax1.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '-.g')
ax1.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], ':m')
# ax1.title.set_text("Strongly adapting model with 188 pA input")
ax1.text(0.9, 1.125, "Strongly adapting model with 188 pA input", transform=ax1.transAxes, fontsize=14, va='top', ha='center')
ax1.set_xlabel("Time (ms)")
ax1.set_ylabel("Membrane potential (mV)")
ax1.set_xlim(0.0, 1200.0)
ax1.set_ylim(-80, 30)

ax2 = plt.subplot2grid((3,5), (0, 3))
ax2.plot(data_Original_SA["T"], data_Original_SA["V"], '-r')
ax2.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '--b')
ax2.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '-.g')
ax2.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], ':m')
ax2.set_xlim(100, 130)
ax2.set_ylim(-80, 30)
ax2.set(yticklabels=[])  # remove the tick labels
ax2.tick_params(left=False)  # remove the ticks

ax2a = plt.subplot2grid((3,5), (0, 4))
ax2a.plot(data_Original_SA["T"], data_Original_SA["V"], '-r')
ax2a.plot(data_Brian1_SA["T"], data_Brian1_SA["V"], '--b')
ax2a.plot(data_Brian2_SA["T"], data_Brian2_SA["V"], '-.g')
ax2a.plot(data_Neuron_SA["T"], data_Neuron_SA["V"], ':m')
ax2a.set_xlim(220, 250)
ax2a.set_ylim(-80, 30)
ax2a.set(yticklabels=[])  # remove the tick labels
ax2a.tick_params(left=False)  # remove the ticks

ax3 = plt.subplot2grid((3,5), (1, 0), colspan=3)
ax3.text(-0.15, 1.15, "B", transform=ax3.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax3.plot(data_Original_WA1["T"], data_Original_WA1["V"], '-r')
ax3.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '--b')
ax3.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '-.g')
ax3.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], ':m')
# ax3.title.set_text("Weakly adapting model #1 with 154 pA input")
ax3.text(0.9, 1.125, "Weakly adapting model #1 with 154 pA input", transform=ax3.transAxes, fontsize=14, va='top', ha='center')
ax3.set_xlabel("Time (ms)")
ax3.set_ylabel("Membrane potential (mV)")
ax3.set_xlim(0.0, 1200.0)
ax3.set_ylim(-100, 50)

ax4 = plt.subplot2grid((3,5), (1, 3))
ax4.plot(data_Original_WA1["T"], data_Original_WA1["V"], '-r')
ax4.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '--b')
ax4.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '-.g')
ax4.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], ':m')
ax4.set_xlim(130, 160)
ax4.set_ylim(-100, 50)
ax4.set(yticklabels=[])  # remove the tick labels
ax4.tick_params(left=False)  # remove the ticks

ax4a = plt.subplot2grid((3,5), (1, 4))
ax4a.plot(data_Original_WA1["T"], data_Original_WA1["V"], '-r')
ax4a.plot(data_Brian1_WA1["T"], data_Brian1_WA1["V"], '--b')
ax4a.plot(data_Brian2_WA1["T"], data_Brian2_WA1["V"], '-.g')
ax4a.plot(data_Neuron_WA1["T"], data_Neuron_WA1["V"], ':m')
ax4a.set_xlim(220, 250)
ax4a.set_ylim(-100, 50)
ax4a.set(yticklabels=[])  # remove the tick labels
ax4a.tick_params(left=False)  # remove the ticks

ax5 = plt.subplot2grid((3,5), (2, 0), colspan=3)
ax5.text(-0.15, 1.15, "C", transform=ax5.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
ax5.plot(data_Original_WA2["T"], data_Original_WA2["V"], '-r')
ax5.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '--b')
ax5.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '-.g')
ax5.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], ':m')
# ax5.title.set_text("Weakly adapting model #2 with 154 pA input")
ax5.text(0.9, 1.125, "Weakly adapting model #2 with 154 pA input", transform=ax5.transAxes, fontsize=14, va='top', ha='center')
ax5.set_xlabel("Time (ms)")
ax5.set_ylabel("Membrane potential (mV)")
ax5.set_xlim(0.0, 1200.0)
ax5.set_ylim(-100, 50)

ax6 = plt.subplot2grid((3,5), (2, 3))
ax6.plot(data_Original_WA2["T"], data_Original_WA2["V"], '-r')
ax6.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '--b')
ax6.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '-.g')
ax6.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], ':m')
ax6.set_xlim(130, 160)
ax6.set_ylim(-100, 50)
ax6.set(yticklabels=[])  # remove the tick labels
ax6.tick_params(left=False)  # remove the ticks

ax6a   = plt.subplot2grid((3,5), (2, 4))
ax6a.plot(data_Original_WA2["T"], data_Original_WA2["V"], '-r')
ax6a.plot(data_Brian1_WA2["T"], data_Brian1_WA2["V"], '--b')
ax6a.plot(data_Brian2_WA2["T"], data_Brian2_WA2["V"], '-.g')
ax6a.plot(data_Neuron_WA2["T"], data_Neuron_WA2["V"], ':m')
ax6a.set_xlim(220, 250)
ax6a.set_ylim(-100, 50)
ax6a.set(yticklabels=[])  # remove the tick labels
ax6a.tick_params(left=False)  # remove the ticks

# fig.tight_layout()
plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

fig.legend(['Original', 'Brian1', 'Brian2', 'NEURON'], loc='lower center', bbox_to_anchor=(0.5, 0), fancybox=True, shadow=True, ncol=4)

fig_name = os.path.join(output_directory, "script_02_depol_plot_9panels.pdf")
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()