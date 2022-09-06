from hbp_validation_framework import TestLibrary
tl = TestLibrary("shailesh")

test_list = [
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

base_data_loc = "https://object.cscs.ch/v1/AUTH_c0a333ecf7c045809321ce9d9ecdfdea/sp6_validation_data/eFELunit/" 

for model in model_list:
    for test in test_list:
      test_json = tl.add_test(name="eFEL test: {} - {}".format(test, model["name"]), 
            alias="ferg2014_{}_{}".format(test.lower(), model["name"].split("_")[1].lower()),  author="Shailesh Appukuttan",
            brain_region="hippocampus CA1", species="Mus musculus", cell_type="hippocampus CA1 pyramidal cell",
            recording_modality="electrophysiology", test_type="single cell activity", score_type="Other", 
            description="Tests eFEL '{}' feature for {} models".format(test, model["name"]),
            data_location=base_data_loc + "Model_{}/Ferguson2014_{}_{}.json".format(model["short"], model["short"],test),
            data_type="Mean, SD", implementation_status="in development",
            instances=[{
              "version": "1.0",
              "repository": "https://github.com/appukuttan-shailesh/eFELunit.git",
              "path": "eFELunit.tests.eFELfeatureTest",
              "description": "Uses eFELunit v2.0.x"
            }])
      print(test_json["id"])

# Registered test IDs:
# 6ea02c1c-8a2a-4e93-906c-1ca28d389f8c
# 3e6eca8b-c9d3-4459-b3b8-1bc812d3b178
# 7a2c3f9f-39df-41d4-9f8b-a69ed6db9f9b
# 8c8506c3-974a-4717-81e4-91be933da499
# e7263e1e-340e-4ce6-9de3-7ad0e8a7b2e9
# fb7b4092-fa48-444a-9e60-d59396a39ec1
# 5342a8d4-7981-438a-b7d2-a40358c09296
# d9b319f7-2529-477b-9356-9a237fac15b6
# dfa0381b-0525-4a58-b7a4-ca1f9f412a28
# 27d4a18b-f2aa-439a-a3eb-eaa72410eb08
# 0869abec-69f5-4dec-aa63-8522af4b291e
# 59ca0c21-cb15-4d6d-9c0b-a7555c4f6f9b
# f10e4f93-be8f-420e-b6c9-7d455822144d
# d7418480-fbc9-479d-86b3-95a834141247
# 5b354246-3173-4147-96ff-2a3a37bb1227
# 62de3999-c3e1-4243-8e73-a7f87d71e08f
# 1ba60539-b53b-4408-a3ee-cbd8ed7f1d8f
# 3a3ea5e8-214b-4c57-a3d2-b7af4d1cb4d5
# 9707c34c-761a-4430-8dfc-16201e7cf2e5
# 55c960bc-50fb-4e83-9243-84e85e884982
# 3c209ea4-66cb-41c3-ac8f-61381424c081
# c1d4bb17-5f29-4cfe-80c0-2404a26db7f2
# 8cce168c-d497-4d56-a65e-0b345df51d5f
# 990b5383-1281-432b-bdc8-892d8ceb05ba
# ffc824b7-36e1-4099-83de-2279893dbbde
# 5ceecc4a-d9e0-48ab-8c49-f1a5ac54220f
# a097cd2b-605a-42e1-beef-84fbf48e7788
# fa8b9ebe-a163-4115-94e5-02ccb6d3cfca
# 8654f1bd-c902-41f1-a3f8-3e328ef0f3ca
# 04f25b07-af39-4f6b-b738-91cb27d51b49
# 83ae2e78-c0fa-41de-a8be-35ea4b58acc2
# 86730c86-a57b-48b0-a950-a773983c922a
# f68485bc-022f-4fa9-9373-796fd2a441c7
# 07ba303f-1611-447c-a6b5-7c1eb4ca3307
# cc389905-6ca9-4d19-a18b-4145c306a222
# 2c950213-d474-47bc-ba53-839d9a0eab13
# 804ab25f-8462-4cb4-b5d4-23a479aefd4a
# f42cf22f-fbde-4dfd-b118-e00b3845546c
# b9f079f2-beea-4fad-b0f7-a26e515be669