from hbp_validation_framework import TestLibrary
tl = TestLibrary("shailesh")

tl.add_test(name="Test for initial frequency - Pyr_Strong - v_init = -65mV", 
            alias="ferg2014_finitial_strong_65",  author="Shailesh Appukuttan",
            brain_region="hippocampus CA1", species="Mus musculus", cell_type="hippocampus CA1 pyramidal cell",
            recording_modality="electrophysiology", test_type="single cell activity", score_type="Other", 
            description="Tests initial frequency for strongly adapting cells",
            data_location="https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/sp6_validation_data/eFELunit/FromOriginal/Ferguson2014_SA_Finitial_-65.0.json",
            data_type="Mean, SD", implementation_status="in development",
            instances=[{
              "version": "1.0",
              "repository": "https://github.com/appukuttan-shailesh/eFELunit.git",
              "path": "eFELunit.tests.Ferg2014_APFrequencyTest",
              "description": "Uses eFELunit v2.0"
            }])

