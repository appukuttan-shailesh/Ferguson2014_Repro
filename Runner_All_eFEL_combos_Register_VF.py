# Description:

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys, json
import subprocess

simulator = sys.argv[1]
if sys.argv[2] == "all":
    features_list = [
                    'spikecount',
                    'time_to_first_spike',
                    'time_to_second_spike',
                    'time_to_last_spike',
                    'AP1_amp',
                    'AP2_amp',
                    'APlast_amp',
                    'AP1_peak',
                    'AP2_peak',
                    'AP1_width',
                    'AP2_width',
                    'APlast_width',
                    'iv_curve'
                ]
else:
    features_list = [sys.argv[2]]

v_init = -65.0 # mV

# py2env = "/home/shailesh/.virtualenvs/ferg_py2/bin/python2"
py2env = "/home/shailesh/.virtualenvs/py2venv/bin/python"
# py3env = "/home/shailesh/.virtualenvs/py3env/bin/python"
py3env = "/home/shailesh/.virtualenvs/py3venv/bin/python"
if simulator == "Brian1":
    pyenv = py2env
else:
    pyenv = py3env

def create_command(feature, sim_params, model_type, model_alias, v_init=None):
    commands = """
from hbp_validation_framework import utils
from {simulator}.generic_Pyr_model_{simulator} import CA1_Pyr_{simulator}_Template
model = CA1_Pyr_{simulator}_Template(type='{model_type}', v_init={v_init})
model.model_alias = '{model_alias}'
model.model_version = 'Neuron_Euler'
result, score = utils.run_test_standalone(username = "shailesh",
                            model = model,
                            test_alias = "ferg2014_{feature_lower}_{model_type}",
                            storage_collab_id = "live-paper-2022-appukuttan-davison",
                            register_result = True,
                            # below parameters passed to test
                            feature='{feature}',
                            sim_params={sim_params},
                            force_run=True,
                            show_plot=False)
    """.format(feature=feature, feature_lower=feature.lower(), sim_params=sim_params, simulator=simulator, model_type=model_type, model_alias=model_alias, v_init=v_init)
    return commands

sim_params_default = {"stim_delay": 0, "stim_duration": 1000, "tstop": 1000, "dt": 0.02}
sim_params_iv_curve = {"stim_delay": 1500, "stim_duration": 2500, "tstop": 5000, "dt": 0.02}

for feature in features_list:
    if feature == "iv_curve":
        sim_params = sim_params_iv_curve
    else:
        sim_params = sim_params_default

    print("********************************************************************************")
    print("SA Model - {} - Vm={} mV".format(feature, v_init))
    model_type = "strong"
    model_alias = "ferg2014_strong"
    subprocess.check_output([pyenv, "-c",
                            create_command(feature=feature, sim_params=sim_params,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)])

    print("********************************************************************************")
    print("WA1 Model - {} - Vm={} mV".format(feature, v_init))
    model_type = "weak1"
    model_alias = "ferg2014_weak1"
    subprocess.check_output([pyenv, "-c",
                            create_command(feature=feature, sim_params=sim_params,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)])

    print("********************************************************************************")
    print("WA2 Model - {} - Vm={} mV".format(feature, v_init))
    model_type = "weak2"
    model_alias = "ferg2014_weak2"
    subprocess.check_output([pyenv, "-c",
                            create_command(feature=feature, sim_params=sim_params,
                            model_type=model_type, model_alias=model_alias, v_init=v_init)])


# Code for handling a single run
# ------------------------------
#
# model_type = "strong"
# feature = "spikecount"
#
# sim_params_default = {"stim_delay": 0, "stim_duration": 1000, "tstop": 1000, "dt": 0.02}
# sim_params_iv_curve = {"stim_delay": 1500, "stim_duration": 2500, "tstop": 5000, "dt": 0.02}
#
# if feature == "iv_curve":
#     sim_params = sim_params_iv_curve
# else:
#     sim_params = sim_params_default
#
# from hbp_validation_framework import utils
# from Brian2.generic_Pyr_model_Brian2 import CA1_Pyr_Brian2_Template
# model = CA1_Pyr_Brian2_Template(type=model_type, v_init=-65.0)
# model.model_alias = "ferg2014_{}".format(model_type)
# model.model_version = "Brian2"
# result, score = utils.run_test_standalone(username = "shailesh",
#                             model = model,
#                             test_alias = "ferg2014_{}_{}".format(feature.lower(), model_type),
#                             storage_collab_id = "live-paper-2022-appukuttan-davison",
#                             register_result = True,
#                             # below parameters passed to test
#                             feature=feature,
#                             sim_params=sim_params,
#                             force_run=True,
#                             show_plot=False)