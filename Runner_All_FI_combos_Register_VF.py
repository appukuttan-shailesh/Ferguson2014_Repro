# Description:

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys, json
import subprocess

simulator = sys.argv[1]
v_init = float(sys.argv[2])

# py2env = "/home/shailesh/.virtualenvs/ferg_py2/bin/python2"
py2env = "/home/shailesh/.virtualenvs/py2venv/bin/python"
# py3env = "/home/shailesh/.virtualenvs/py3env/bin/python"
py3env = "/home/shailesh/.virtualenvs/py3venv/bin/python"
if simulator == "Brian1":
    pyenv = py2env
else:
    pyenv = py3env

list_feat_abbrev = {"initial_fi": "finitial", "final_fi": "ffinal"}

def create_command(feature, model_type, model_alias, v_init=None):
    commands = """
from hbp_validation_framework import utils
from {simulator}.generic_Pyr_model_{simulator} import CA1_Pyr_{simulator}_Template
model = CA1_Pyr_{simulator}_Template(type='{model_type}', v_init={v_init})
model.model_alias = '{model_alias}'
model.model_version = 'Neuron_Euler'
result, score = utils.run_test_standalone(username = "shailesh",
                            model = model,
                            test_alias = "ferg2014_{feat_abbrev}_{model_type}_{v_init_str}",
                            storage_collab_id = "live-paper-2022-appukuttan-davison",
                            register_result = True,
                            # below parameters passed to test
                            feature='{feature}',
                            force_run=True,
                            show_plot=False)
    """.format(feature=feature, feat_abbrev=list_feat_abbrev[feature], simulator=simulator, model_type=model_type, model_alias=model_alias, v_init=v_init, v_init_str=str(v_init)[1:3])
    return commands

print("********************************************************************************")
print("SA Model - Initial FI - Vm={} mV".format(v_init))
model_type = "strong"
model_alias = "ferg2014_strong"
feature = "initial_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("SA Model - Final FI - Vm={} mV".format(v_init))
model_type = "strong"
model_alias = "ferg2014_strong"
feature = "final_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA1 Model - Initial FI - Vm={} mV".format(v_init))
model_type = "weak1"
model_alias = "ferg2014_weak1"
feature = "initial_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA1 Model - Final FI - Vm={} mV".format(v_init))
model_type = "weak1"
model_alias = "ferg2014_weak1"
feature = "final_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA2 Model - Initial FI - Vm={} mV".format(v_init))
model_type = "weak2"
model_alias = "ferg2014_weak2"
feature = "initial_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)

print("********************************************************************************")
print("WA2 Model - Final FI - Vm={} mV".format(v_init))
model_type = "weak2"
model_alias = "ferg2014_weak2"
feature = "final_fi"
with subprocess.Popen([pyenv, "-c",
                            create_command(feature=feature,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)],
                            stdout=subprocess.PIPE, text=True) as process:
    for line in process.stdout:
        print(line)


# Code for handling a single run
# ------------------------------
#
# model_type = "strong"
# feature = "initial_fi"
# v_init = -65.0
# list_feat_abbrev = {"initial_fi": "finitial", "final_fi": "ffinal"}
#
# from hbp_validation_framework import utils
# from Neuron.generic_Pyr_model_Neuron import CA1_Pyr_Neuron_Template
# model = CA1_Pyr_Neuron_Template(type=model_type, v_init=-65.0)
# model.model_alias = "ferg2014_{}".format(model_type)
# model.model_version = "Neuron"
# result, score = utils.run_test_standalone(username = "shailesh",
#                             model = model,
#                             test_alias = "ferg2014_{}_{}_{}".format(list_feat_abbrev[feature], model_type, str(v_init)[1:3]),
#                             storage_collab_id = "live-paper-2022-appukuttan-davison",
#                             register_result = True,
#                             # below parameters passed to test
#                             feature=feature,
#                             force_run=True,
#                             show_plot=False)