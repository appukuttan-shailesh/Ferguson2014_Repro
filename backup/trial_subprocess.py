# Description: 

# Implemented by: Shailesh Appukuttan (CNRS), August 2022

import os, sys
import subprocess

output_directory = os.path.join(".", "Results", "_".join(sys.argv[0].split("_")[0:2]))
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

stim_min = -50.0
stim_max = 300.0
stim_step = 10.0

output = subprocess.check_output(["/home/shailesh/.virtualenvs/ferg_py2/bin/python2", "./Brian1/strongly_adapting_PYR_model_FI.py", str(10)])
print(output)