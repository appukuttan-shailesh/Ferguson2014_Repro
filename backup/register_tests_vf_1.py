from hbp_validation_framework import TestLibrary
tl = TestLibrary("shailesh")

test_list = [
  {
    "name_suffix": "Initial frequency",
    "short": "Finitial",
  },
  {
    "name_suffix": "Final frequency",
    "short": "Ffinal",
  }
]

model_list = [
  {
    "name" : "Pyr_Strong",
    "short" : "SA",
  },
  {
    "name" : "Pyr_Weak1",
    "short" : "WA1",
  },  
  {
    "name" : "Pyr_Weak2",
    "short" : "WA2",
  }
]

vlist = ["65", "55"]

base_data_loc = "https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/sp6_validation_data/eFELunit/FromOriginal/" 

for v in vlist:
  for model in model_list:
    for test in test_list:
      test_json = tl.add_test(name="Test: {} - {} - v_init = -{}mV".format(test["name_suffix"], model["name"], v), 
            alias="ferg2014_{}_{}_{}".format(test["short"].lower(), model["name"].split("_")[1].lower(), v),  author="Shailesh Appukuttan",
            brain_region="hippocampus CA1", species="Mus musculus", cell_type="hippocampus CA1 pyramidal cell",
            recording_modality="electrophysiology", test_type="single cell activity", score_type="Other", 
            description="Tests {} for {} models".format(test["name_suffix"].lower(), model["name"]),
            data_location=base_data_loc + "Ferguson2014_{}_{}_-{}.0.json".format(model["short"],test["short"],v),
            data_type="Mean, SD", implementation_status="in development",
            instances=[{
              "version": "1.0",
              "repository": "https://github.com/appukuttan-shailesh/eFELunit.git",
              "path": "eFELunit.tests.Ferg2014_APFrequencyTest",
              "description": "Uses eFELunit v2.0.x"
            }])
      print(test_json["id"])

# Registered test IDs:
# 90ae68fa-a9e6-49dd-947a-908ab9a6dee2
# a218b945-8414-4a1e-bcbb-af400f0d7f91
# 66c660bc-ab00-4232-8b9d-31045d9136ec
# 03988b0a-55ac-430e-9899-2a82b7b2c2ce
# b3655789-3df1-43c9-8b22-736c4d24b8f4
# e5a04fc1-b54f-4c43-95fd-efcac0fdb52f
# 6b433a4e-dad4-4dd2-9456-b564606d4f29
# 4a0f7f7b-bc90-48e3-979a-b4ff77f7ec29
# 153d225f-9588-40e3-a8d2-e6df7c253d9a
# 1f878e5a-a536-485b-ae35-5370ffb09ac0
# 3cf1550e-a4a6-434d-bc4c-3ac7fa41437e
# 7281ef8a-fd74-441c-bcae-94b02f076a34