# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import efel

v_init = float(sys.argv[1])

output_directory = os.path.join(".", "Results", "_".join(sys.argv[0].split("_")[0:2]))
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


def extract_FI_data(filepath):
    '''
    Extract and return spike data from excel sheet
    '''
    xlsx_data = pd.read_excel(filepath)

    fi_data = {}
    fi_data_str_initial = []
    fi_data_str_final = []
    fi_data_str_mean = []
    for col in xlsx_data.loc[:, xlsx_data.columns.drop('t')]:
        efel.reset()
        data_eFEL = {
            "T": xlsx_data["t"],
            "V": xlsx_data[col],
            "stim_start": [xlsx_data["t"].values[0]],
            "stim_end": [xlsx_data["t"].values[-1]],
        }
        feature_vals = efel.getFeatureValues([data_eFEL], ['inv_first_ISI', 'inv_last_ISI', 'Spikecount_stimint'])
        print(feature_vals)
        spikecount = feature_vals[0]['Spikecount_stimint'][0]
        if spikecount == 1:
            initial_f = 1
            final_f = 1
        else:    
            initial_f = feature_vals[0]['inv_first_ISI'][0]
            final_f = feature_vals[0]['inv_last_ISI'][0]
        print("{}: {} -> {}, {}, {}".format(os.path.basename(filepath), col, spikecount, initial_f, final_f))
        # NOTE: Spikecount is the number of spikes, not the number of spikes per second
        # Accurate as frequency when stim period is exactly 1 second
        # we use efel -> Spikecount_stimint, NOT Spikecount
        fi_data[col] = {"initial_f": initial_f, "final_f": final_f, "mean_f": spikecount}
        fi_data_str_initial.append({
                            "i_inj": str(col) + " pA", 
                            "value": str(round(initial_f, 2)) + " Hz", 
                            })
        fi_data_str_final.append({
                            "i_inj": str(col) + " pA", 
                            "value": str(round(final_f, 2)) + " Hz", 
                            })
        fi_data_str_mean.append({
                            "i_inj": str(col) + " pA", 
                            "value": str(round(spikecount, 2)) + " Hz"
                            })
    return fi_data, fi_data_str_initial, fi_data_str_final, fi_data_str_mean


def read_FI_data_from_file(filepath_initial, filepath_final):
    '''
    Read FI data from JSON file created by APFrequencyTest
    '''
    with open(filepath_initial, 'r') as f:
        data_initial = json.load(f)
    with open(filepath_final, 'r') as f:
        data_final = json.load(f)

    fi_data = {}
    for val_initial, val_final in zip(data_initial["prediction"], data_final["prediction"]):
        fi_data[float(val_initial["i_inj"].split(" ")[0])] = {
                                            "initial_f": float(val_initial["value"].split(" ")[0]), 
                                            "final_f": float(val_final["value"].split(" ")[0]),
                                            "mean_f": None
                                        }
    return fi_data


# Load Original FI data from xlsx file
data_Original_SA,  fi_data_SA_str_initial, fi_data_SA_str_final, fi_data_SA_str_mean = extract_FI_data(os.path.join(".", "Original", "data", "data_Original_SA_FI_" + str(v_init) + ".xlsx"))
data_Original_WA1, fi_data_WA1_str_initial, fi_data_WA1_str_final, fi_data_WA1_str_mean = extract_FI_data(os.path.join(".", "Original", "data", "data_Original_WA1_FI_" + str(v_init) + ".xlsx"))
data_Original_WA2, fi_data_WA2_str_initial, fi_data_WA2_str_final, fi_data_WA2_str_mean = extract_FI_data(os.path.join(".", "Original", "data", "data_Original_WA2_FI_" + str(v_init) + ".xlsx"))

# Write Original FI data to json file
# to be used as observation (target) data for other models
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_SA_Finitial_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_SA_str_initial, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA1_Finitial_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA1_str_initial, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA2_Finitial_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA2_str_initial, out_file, sort_keys = True, indent = 4, ensure_ascii=False)

with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_SA_Ffinal_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_SA_str_final, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA1_Ffinal_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA1_str_final, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA2_Ffinal_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA2_str_final, out_file, sort_keys = True, indent = 4, ensure_ascii=False)

with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_SA_Fmean_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_SA_str_mean, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA1_Fmean_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA1_str_mean, out_file, sort_keys = True, indent = 4, ensure_ascii=False)
with open(os.path.join(".", "obsData", "FromOriginal", "Ferguson2014_WA2_Fmean_" + str(v_init) + ".json"), 'w') as out_file:
     json.dump(fi_data_WA2_str_mean, out_file, sort_keys = True, indent = 4, ensure_ascii=False)

base_directory = os.path.join(".", "Results", "FI_test")

# Load Brian1 FI data from xlsx file
data_Brian1_SA  = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian1_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian1_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"))
data_Brian1_WA1 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian1_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian1_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"))
data_Brian1_WA2 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian1_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian1_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"))

# Load Brian2 FI data from xlsx file
data_Brian2_SA  = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian2_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian2_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"))
data_Brian2_WA1 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian2_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian2_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"))
data_Brian2_WA2 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "Brian2_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "Brian2_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"))

# Load Neuron FI data from xlsx file
data_Neuron_SA  = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "NEURON_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "NEURON_Strongly_Adapting_PYR_Model_" + str(v_init), "test_summary.json"))
data_Neuron_WA1 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "NEURON_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "NEURON_Weakly_Adapting_PYR_Model_1_" + str(v_init), "test_summary.json"))
data_Neuron_WA2 = read_FI_data_from_file(os.path.join(base_directory, "Test_for_initial_fi", "NEURON_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"),
                                                          os.path.join(base_directory, "Test_for_final_fi", "NEURON_Weakly_Adapting_PYR_Model_2_" + str(v_init), "test_summary.json"))

labels = [
            'Original-Initial', 'Original-Final', 
            'Brian1-Initial', 'Brian1-Final', 
            'Brian2-Initial', 'Brian2-Final',
            'NEURON-Initial', 'NEURON-Final'
        ]

# plot data and save figure
plt.figure(figsize=(5, 10))
fig = plt.gcf()

ax = plt.subplot(3, 1, 1)
ax.grid(True, linestyle = '--')
plt.plot(list(data_Original_SA.keys()), list([x["initial_f"] for x in data_Original_SA.values()]), '-r')
plt.plot(list(data_Original_SA.keys()), list([x["final_f"] for x in data_Original_SA.values()]), '--r')
plt.plot(list(data_Brian1_SA.keys()), list([x["initial_f"] for x in data_Brian1_SA.values()]), '-b')
plt.plot(list(data_Brian1_SA.keys()), list([x["final_f"] for x in data_Brian1_SA.values()]), '--b')
plt.plot(list(data_Brian2_SA.keys()), list([x["initial_f"] for x in data_Brian2_SA.values()]), '-g')
plt.plot(list(data_Brian2_SA.keys()), list([x["final_f"] for x in data_Brian2_SA.values()]), '--g')
plt.plot(list(data_Neuron_SA.keys()), list([x["initial_f"] for x in data_Neuron_SA.values()]), '-m')
plt.plot(list(data_Neuron_SA.keys()), list([x["final_f"] for x in data_Neuron_SA.values()]), '--m')
plt.title("Strongly adapting model")
# plt.legend(['Original-Initial', 'Original-Final'], loc='best')
plt.xlabel("$I_{applied} (pA)$")
plt.ylabel("AP frequency (Hz)")
plt.xlim(-50.0, 300.0)
plt.ylim(0, 120)

ax = plt.subplot(3, 1, 2)
ax.grid(True, linestyle = '--')
plt.plot(list(data_Original_WA1.keys()), list([x["initial_f"] for x in data_Original_WA1.values()]), '-r')
plt.plot(list(data_Original_WA1.keys()), list([x["final_f"] for x in data_Original_WA1.values()]), '--r')
plt.plot(list(data_Brian1_WA1.keys()), list([x["initial_f"] for x in data_Brian1_WA1.values()]), '-b')
plt.plot(list(data_Brian1_WA1.keys()), list([x["final_f"] for x in data_Brian1_WA1.values()]), '--b')
plt.plot(list(data_Brian2_WA1.keys()), list([x["initial_f"] for x in data_Brian2_WA1.values()]), '-g')
plt.plot(list(data_Brian2_WA1.keys()), list([x["final_f"] for x in data_Brian2_WA1.values()]), '--g')
plt.plot(list(data_Neuron_WA1.keys()), list([x["initial_f"] for x in data_Neuron_WA1.values()]), '-m')
plt.plot(list(data_Neuron_WA1.keys()), list([x["final_f"] for x in data_Neuron_WA1.values()]), '--m')
plt.title("Weakly adapting model #1")
# plt.legend(['Original-Initial', 'Original-Final'], loc='best')
plt.xlabel("$I_{applied} (pA)$")
plt.ylabel("AP frequency (Hz)")
plt.xlim(-50.0, 350.0)
plt.ylim(0, 50)

ax = plt.subplot(3, 1, 3)
ax.grid(True, linestyle = '--')
plt.plot(list(data_Original_WA2.keys()), list([x["initial_f"] for x in data_Original_WA2.values()]), '-r')
plt.plot(list(data_Original_WA2.keys()), list([x["final_f"] for x in data_Original_WA2.values()]), '--r')
plt.plot(list(data_Brian1_WA2.keys()), list([x["initial_f"] for x in data_Brian1_WA2.values()]), '-b')
plt.plot(list(data_Brian1_WA2.keys()), list([x["final_f"] for x in data_Brian1_WA2.values()]), '--b')
plt.plot(list(data_Brian2_WA2.keys()), list([x["initial_f"] for x in data_Brian2_WA2.values()]), '-g')
plt.plot(list(data_Brian2_WA2.keys()), list([x["final_f"] for x in data_Brian2_WA2.values()]), '--g')
plt.plot(list(data_Neuron_WA2.keys()), list([x["initial_f"] for x in data_Neuron_WA2.values()]), '-m')
plt.plot(list(data_Neuron_WA2.keys()), list([x["final_f"] for x in data_Neuron_WA2.values()]), '--m')
plt.title("Weakly adapting model #2")
ax.legend(labels, loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=4)
plt.xlabel("$I_{applied} (pA)$")
plt.ylabel("AP frequency (Hz)")
plt.xlim(-50.0, 350.0)
plt.ylim(0, 50)

fig.tight_layout()
fig_name = os.path.join(output_directory, "script_01_FI_plot_" + str(v_init) + ".pdf")
plt.savefig(fig_name, dpi=600, bbox_inches='tight')
plt.show()