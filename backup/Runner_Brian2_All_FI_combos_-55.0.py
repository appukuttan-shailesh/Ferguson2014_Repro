# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys, json
import subprocess

# Load target data for SA model
with open(os.path.join(".", "obsData", "Model_SA", "Ferguson2014_SA_Finitial.json")) as json_file:
    data_SA_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_SA", "Ferguson2014_SA_Ffinal.json")) as json_file:
    data_SA_final = json.load(json_file)

# Load target data for WA1 model
with open(os.path.join(".", "obsData", "Model_WA1", "Ferguson2014_WA1_Finitial.json")) as json_file:
    data_WA1_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_WA1", "Ferguson2014_WA1_Ffinal.json")) as json_file:
    data_WA1_final = json.load(json_file)

# Load target data for WA2 model
with open(os.path.join(".", "obsData", "Model_WA2", "Ferguson2014_WA2_Finitial.json")) as json_file:
    data_WA2_intial = json.load(json_file)
with open(os.path.join(".", "obsData", "Model_WA2", "Ferguson2014_WA2_Ffinal.json")) as json_file:
    data_WA2_final = json.load(json_file)

py2env = "/home/shailesh/.virtualenvs/ferg_py2/bin/python2"
py3env = "/home/shailesh/.virtualenvs/py3env/bin/python"

def create_command(data, feature, model_type, v_init=None):
    commands = """data = {data}
from eFELunit.tests import eFELfeatureTest
test = eFELfeatureTest(data, feature='{feature}', force_run=True, show_plot=False)
from Brian2.generic_Pyr_model_Brian2 import CA1_Pyr_Brian2_Template
model = CA1_Pyr_Brian2_Template(type='{model_type}', v_init={v_init})
test.judge(model, deep_error=True)
    """.format(data=data, feature=feature, model_type=model_type, v_init=v_init)
    return commands

print("********************************************************************************")
print("SA Model - Initial FI - Vm=-55.0 mV")
model_type = "strong"
data = data_SA_intial
feature = "initial_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("SA Model - Final FI - Vm=-55.0 mV")
model_type = "strong"
data = data_SA_final
feature = "final_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA1 Model - Initial FI - Vm=-55.0 mV")
model_type = "weak1"
data = data_WA1_intial
feature = "initial_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA1 Model - Final FI - Vm=-55.0 mV")
model_type = "weak1"
data = data_WA1_final
feature = "final_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA2 Model - Initial FI - Vm=-55.0 mV")
model_type = "weak2"
data = data_WA2_intial
feature = "initial_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA2 Model - Final FI - Vm=-55.0 mV")
model_type = "weak2"
data = data_WA2_final
feature = "final_fi"
v_init = -55.0
with subprocess.Popen([py3env, "-c", 
                            create_command(data=data,feature=feature,
                            model_type=model_type, v_init=v_init)], 
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)