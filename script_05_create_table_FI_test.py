import os
import sys
import json
import pandas as pd

field = sys.argv[1]
req_score = sys.argv[2] # RMSE or NRMSE (useful only for field = score) 

output_directory = os.path.join(".", "Results", "_".join(sys.argv[0].split("_")[0:2]))
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

html_string = """
<table border="1">
  <thead>
	<tr>
	  <td rowspan="2">Parameter</td>
	  <td colspan="4">Strongly Adapting Model</td>FI_test
	  <td colspan="4">Weakly Adapting Model 1</td>
	  <td colspan="4">Weakly Adapting Model 2</td>
	</tr>
	<tr>
	  <td>Original</td>
	  <td>Brian1</td>
	  <td>Brian2</td>
	  <td>NEURON</td>
	  <td>Original</td>
	  <td>Brian1</td>
	  <td>Brian2</td>
	  <td>NEURON</td>
	  <td>Original</td>
	  <td>Brian1</td>
	  <td>Brian2</td>
	  <td>NEURON</td>
	</tr>
  </thead>
  <tbody>
  </tbody>
</table>
"""

dfs = pd.read_html(html_string)
df = dfs[0]

v_init = -65.0 # mV
features_list = [
				'initial_fi', 
				'final_fi', 
			]
models = ["Strongly_Adapting_PYR_Model", "Weakly_Adapting_PYR_Model_1", "Weakly_Adapting_PYR_Model_2"]

base_directory = os.path.join(".", "Results", "FI_test")

for idx, feature in enumerate(features_list):
	testname = "Test_for_{}".format(feature)
	test_dir = os.path.join(base_directory, testname)
	row_vals = [feature]

	for model in models:
		# for Original model (target data)
		row_vals.append(0.0)

		Brian1_test_summary = os.path.join(test_dir, "{}_{}_{}".format("Brian1", model, str(v_init)), "test_summary.json")
		with open(Brian1_test_summary) as f:
			data = json.load(f)
		if req_score == "NRMSE":
			obs_mean = sum([float(x["value"].split(" ")[0]) for x in data["observation"]])/len(data["observation"])
			row_vals.append(float(data[field])/obs_mean)
		else:
			row_vals.append(data[field])

		Brian2_test_summary = os.path.join(test_dir, "{}_{}_{}".format("Brian2", model, str(v_init)), "test_summary.json")
		with open(Brian2_test_summary) as f:
			data = json.load(f)
		if req_score == "NRMSE":
			obs_mean = sum([float(x["value"].split(" ")[0]) for x in data["observation"]])/len(data["observation"])
			row_vals.append(float(data[field])/obs_mean)
		else:
			row_vals.append(data[field])
	  
		Neuron_test_summary = os.path.join(test_dir, "{}_{}_{}".format("NEURON", model, str(v_init)), "test_summary.json")
		with open(Neuron_test_summary) as f:
			data = json.load(f)
		if req_score == "NRMSE":
			obs_mean = sum([float(x["value"].split(" ")[0]) for x in data["observation"]])/len(data["observation"])
			row_vals.append(float(data[field])/obs_mean)
		else:
			row_vals.append(data[field])

	df.loc[idx+1, :] = row_vals

filename = "table_FI_test_{}_vinit_{}_{}.txt".format(field, str(v_init), req_score)
with open(os.path.join(output_directory, filename),'w') as outfile:
    df.to_string(outfile)
	
filename = "latex_table_FI_test_{}_vinit_{}_{}.tex".format(field, str(v_init), req_score)
with open(os.path.join(output_directory, filename),'w') as outfile:
	outfile.write(df.style.to_latex())