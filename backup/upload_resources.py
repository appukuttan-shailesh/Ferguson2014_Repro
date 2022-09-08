# !pip install hbp_archive
from hbp_archive import Container

c = Container("EBRAINS_live_papers", "bp000106")

# upload scripts
scripts_analysis = [
  "../script_01_compare_FI_6panels.py",
  "../script_02_compare_depol_6panels.py",
  "../script_03_compare_hyperpol_6panels.py",
  "../script_04_original_vary_vstart.py",
  "../script_05_create_table_FI_test.py",
  "../script_06_create_table_eFELfeatureTest.py",
  "../script_07_compare_feature.py"
]
c.upload(scripts_analysis, "2022_appukuttan_davison/scripts_analysis", overwrite=True)

# upload Original model source codes
models_original = [
  "../Original/strongly_adapting_PYR_model_FI.py",
  "../Original/strongly_adapting_PYR_model.py",
  "../Original/strongly_adapting_PYR_model_stimarg.py",
  "../Original/weakly_adapting_PYR_model1_FI.py",
  "../Original/weakly_adapting_PYR_model1.py",
  "../Original/weakly_adapting_PYR_model1_stimarg.py",
  "../Original/weakly_adapting_PYR_model1_vary_vinit.py",
  "../Original/weakly_adapting_PYR_model2_FI.py",
  "../Original/weakly_adapting_PYR_model2.py",
  "../Original/weakly_adapting_PYR_model2_stimarg.py"
]
c.upload(models_original, "2022_appukuttan_davison/models/Original", overwrite=True)

# upload Brian1 model source codes
models_brian1 = [
  "../Brian1/generic_Pyr_model_Brian1.py",
  "../Brian1/run_Brian1_stimarg.py",
]
c.upload(models_brian1, "2022_appukuttan_davison/models/Brian1", overwrite=True)

# upload Brian2 model source codes
models_brian2 = [
  "../Brian2/generic_Pyr_model_Brian2.py",
  "../Brian2/run_Brian2_stimarg.py",
  "../Brian2/strongly_adapting_Pyr_model.py",
  "../Brian2/weakly_adapting_Pyr_model.py"
]
c.upload(models_brian2, "2022_appukuttan_davison/models/Brian2", overwrite=True)

# upload NEURON model source codes
models_neuron = [
  "../Neuron/generic_Pyr_model_Neuron.py",
  "../Neuron/Pyr.mod",
  "../Neuron/run_Neuron_stimarg.py",
  "../Neuron/generic_Pyr_model_Neuron_with_mod_file.zip",
  "../Neuron/strongly_adapting_Pyr_model.py",
]
c.upload(models_neuron, "2022_appukuttan_davison/models/Neuron", overwrite=True)

# upload pip freeze files
pip_freeze = [
  "py2venv_pip_freeze.txt",
  "py3venv_pip_freeze.txt"
]
c.upload(pip_freeze, "2022_appukuttan_davison/misc", overwrite=True)

# upload figures
figures = [
  "figures/SciUnit.png"
]
c.upload(figures, "2022_appukuttan_davison/figures", overwrite=True)
