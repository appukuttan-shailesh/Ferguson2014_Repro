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
data_Original_nostim_550 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-55.0_amp_0.0_t_0.0.xlsx"))
data_Original_nostim_650 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-65.0_amp_0.0_t_0.0.xlsx"))
data_Original_nostim_750 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-75.0_amp_0.0_t_0.0.xlsx"))
data_Original_nostim_618 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-61.8_amp_0.0_t_0.0.xlsx"))

data_Original_t0_550 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-55.0_amp_5.0_t_0.0.xlsx"))
data_Original_t0_650 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-65.0_amp_5.0_t_0.0.xlsx"))
data_Original_t0_750 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-75.0_amp_5.0_t_0.0.xlsx"))
data_Original_t0_618 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-61.8_amp_5.0_t_0.0.xlsx"))

data_Original_550 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-55.0_amp_5.0_t_0.1.xlsx"))
data_Original_650 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-65.0_amp_5.0_t_0.1.xlsx"))
data_Original_750 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-75.0_amp_5.0_t_0.1.xlsx"))
data_Original_618 = read_data(os.path.join(".", "Original", "data", "vary_v_init", "data_Original_WA1_vinit_-61.8_amp_5.0_t_0.1.xlsx"))

# plot data and save figure
plt.figure(figsize=(8, 10))
fig = plt.gcf()

ax = plt.subplot(3, 1, 1)
ax.text(-0.1, 1.15, "A", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_nostim_550["T"], data_Original_nostim_550["V"], '-r')
plt.plot(data_Original_nostim_650["T"], data_Original_nostim_650["V"], '--b')
plt.plot(data_Original_nostim_750["T"], data_Original_nostim_750["V"], '-.g')
plt.plot(data_Original_nostim_618["T"], data_Original_nostim_618["V"], ':m')
plt.title("Weakly adapting model #1 with no stimulus")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.xlim(0.0, 200.0)
# plt.ylim(-100, 25)

ax = plt.subplot(3, 1, 2)
ax.text(-0.1, 1.15, "B", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_t0_550["T"], data_Original_t0_550["V"], '-r')
plt.plot(data_Original_t0_650["T"], data_Original_t0_650["V"], '--b')
plt.plot(data_Original_t0_750["T"], data_Original_t0_750["V"], '-.g')
plt.plot(data_Original_t0_618["T"], data_Original_t0_618["V"], ':m')
plt.title("Weakly adapting model #1 with 5 pA input at t = 0 ms")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.xlim(0.0, 200.0)
# plt.ylim(-100, 25)

ax = plt.subplot(3, 1, 3)
ax.text(-0.1, 1.15, "C", transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top', ha='right')
plt.plot(data_Original_550["T"], data_Original_550["V"], '-r')
plt.plot(data_Original_650["T"], data_Original_650["V"], '--b')
plt.plot(data_Original_750["T"], data_Original_750["V"], '-.g')
plt.plot(data_Original_618["T"], data_Original_618["V"], ':m')
plt.title("Weakly adapting model #1 with 5 pA input at t = 100 ms")
ax.legend(['$v_{init}$ = -55.0 mV', '$v_{init}$ = -65.0 mV', '$v_{init}$ = -75.0 mV', '$v_{init}$ = -61.8 mV'], loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.xlim(0.0, 200.0)
# plt.ylim(-125, 25)

fig.tight_layout()
fig_name = os.path.join(output_directory, "script_04_vary_vstart_3panels.pdf")
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()