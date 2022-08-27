# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys, json
import subprocess

simulator = sys.argv[1]
feature = sys.argv[2]

v_init = -65.0 # mV

# Load target data for SA model
with open(os.path.join(".", "obsData", "Model_SA", "Ferguson2014_SA_" + feature + ".json")) as json_file:
    data_SA_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_SA", "Ferguson2014_SA_" + feature + ".json")) as json_file:
    data_SA_final = json.load(json_file)

# Load target data for WA1 model
with open(os.path.join(".", "obsData", "Model_WA1", "Ferguson2014_WA1_" + feature + ".json")) as json_file:
    data_WA1_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_WA1", "Ferguson2014_WA1_" + feature + ".json")) as json_file:
    data_WA1_final = json.load(json_file)

# Load target data for WA2 model
with open(os.path.join(".", "obsData", "Model_WA2", "Ferguson2014_WA2_" + feature + ".json")) as json_file:
    data_WA2_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_WA2", "Ferguson2014_WA2_" + feature + ".json")) as json_file:
    data_WA2_final = json.load(json_file)

py2env = "/home/shailesh/.virtualenvs/ferg_py2/bin/python2"
py3env = "/home/shailesh/.virtualenvs/py3env/bin/python"
if simulator == "Brian1":
    pyenv = py2env
else:
    pyenv = py3env

def create_command(data, feature, model_type, v_init=None):
    commands = """data = {data}
from eFELunit.tests import eFELfeatureTest
test = eFELfeatureTest(observation=data, feature='{feature}', force_run=True, show_plot=False)
from {simulator}.generic_Pyr_model_{simulator} import CA1_Pyr_{simulator}_Template
model = CA1_Pyr_{simulator}_Template(type='{model_type}', v_init={v_init})
test.judge(model, deep_error=True)
    """.format(data=data, feature=feature, simulator=simulator, model_type=model_type, v_init=v_init)
    return commands

print("********************************************************************************")
print("SA Model - {} - Vm={} mV".format(feature, v_init))
model_type = "strong"
data = data_SA_intial
with subprocess.Popen([pyenv, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA1 Model - {} - Vm={} mV".format(feature, v_init))
model_type = "weak1"
data = data_WA1_intial
with subprocess.Popen([pyenv, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA2 Model - {} - Vm={} mV".format(feature, v_init))
model_type = "weak2"
data = data_WA2_intial
with subprocess.Popen([pyenv, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)