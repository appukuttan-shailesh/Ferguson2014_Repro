from hbp_validation_framework import ModelCatalog
mc = ModelCatalog("shailesh")

# Pyr_Strong

model = mc.register_model(collab_id="live-paper-2022-appukuttan-davison", name="Strongly adapting CA1 Pyr Model",
                          alias="ferg2014_strong", author="Shailesh Appukuttan", organization="CNRS, France",
                          private=False, cell_type="hippocampus CA1 pyramidal cell", model_scope="single cell",
                          abstraction_level="spiking neurons: point neuron",
                          brain_region="hippocampus CA1", species="Mus musculus",
                          owner="Andrew Davison", license="Creative Commons Attribution Non Commercial 4.0 International",
                          description="This is part of a reproduction/replication study of Ferguson et al. (2014)")

instance = mc.add_model_instance(alias="ferg2014_strong",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Original/strongly_adapting_PYR_model.py",
                                  version="Original",
                                  description="Based on ModelDB accession #182515",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_strong",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian1/generic_Pyr_model_Brian1.py",
                                  version="Brian1",
                                  description="Brian1 re-implementation with SciUnit",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_strong",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian2/generic_Pyr_model_Brian2.py",
                                  version="Brian2",
                                  description="Brian2 reproduction with SciUnit",
                                  code_format="Brian2, Py")                                                                    

instance = mc.add_model_instance(alias="ferg2014_strong",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Neuron/generic_Pyr_model_Neuron_with_mod_file.zip",
                                  version="Neuron",
                                  description="NEURON reproduction with SciUnit",
                                  code_format="Neuron, Py, NMODL")     


# Pyr_Weak1

model = mc.register_model(collab_id="live-paper-2022-appukuttan-davison", name="Weakly adapting CA1 Pyr Model #1",
                          alias="ferg2014_weak1", author="Shailesh Appukuttan", organization="CNRS, France",
                          private=False, cell_type="hippocampus CA1 pyramidal cell", model_scope="single cell",
                          abstraction_level="spiking neurons: point neuron",
                          brain_region="hippocampus CA1", species="Mus musculus",
                          owner="Andrew Davison", license="Creative Commons Attribution Non Commercial 4.0 International",
                          description="This is part of a reproduction/replication study of Ferguson et al. (2014)")

instance = mc.add_model_instance(alias="ferg2014_weak1",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Original/weakly_adapting_PYR_model1.py",
                                  version="Original",
                                  description="Based on ModelDB accession #182515",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_weak1",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian1/generic_Pyr_model_Brian1.py",
                                  version="Brian1",
                                  description="Brian1 re-implementation with SciUnit",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_weak1",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian2/generic_Pyr_model_Brian2.py",
                                  version="Brian2",
                                  description="Brian2 reproduction with SciUnit",
                                  code_format="Brian2, Py")                                                                    

instance = mc.add_model_instance(alias="ferg2014_weak1",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Neuron/generic_Pyr_model_Neuron_with_mod_file.zip",
                                  version="Neuron",
                                  description="NEURON reproduction with SciUnit",
                                  code_format="Neuron, Py, NMODL")    


# Pyr_Weak2

model = mc.register_model(collab_id="live-paper-2022-appukuttan-davison", name="Weakly adapting CA1 Pyr Model #2",
                          alias="ferg2014_weak2", author="Shailesh Appukuttan", organization="CNRS, France",
                          private=False, cell_type="hippocampus CA1 pyramidal cell", model_scope="single cell",
                          abstraction_level="spiking neurons: point neuron",
                          brain_region="hippocampus CA1", species="Mus musculus",
                          owner="Andrew Davison", license="Creative Commons Attribution Non Commercial 4.0 International",
                          description="This is part of a reproduction/replication study of Ferguson et al. (2014)")

instance = mc.add_model_instance(alias="ferg2014_weak2",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Original/weakly_adapting_PYR_model2.py",
                                  version="Original",
                                  description="Based on ModelDB accession #182515",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_weak2",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian1/generic_Pyr_model_Brian1.py",
                                  version="Brian1",
                                  description="Brian1 re-implementation with SciUnit",
                                  code_format="Brian1, Py")

instance = mc.add_model_instance(alias="ferg2014_weak2",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Brian2/generic_Pyr_model_Brian2.py",
                                  version="Brian2",
                                  description="Brian2 reproduction with SciUnit",
                                  code_format="Brian2, Py")                                                                    

instance = mc.add_model_instance(alias="ferg2014_weak2",
                                  source="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/EBRAINS_live_papers/2022_appukuttan_davison/models/Neuron/generic_Pyr_model_Neuron_with_mod_file.zip",
                                  version="Neuron",
                                  description="NEURON reproduction with SciUnit",
                                  code_format="Neuron, Py, NMODL")      