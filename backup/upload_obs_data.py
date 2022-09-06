# !pip install hbp_archive
from hbp_archive import Container

c = Container("sp6_validation_data", "bp000106")

# upload observations: FromOriginal
data_files_from_Original = [
  "../obsData/FromOriginal/Ferguson2014_SA_Ffinal_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_SA_Ffinal_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_SA_Finitial_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_SA_Finitial_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_SA_Fmean_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_SA_Fmean_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Ffinal_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Ffinal_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Finitial_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Finitial_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Fmean_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA1_Fmean_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Ffinal_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Ffinal_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Finitial_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Finitial_-65.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Fmean_-55.0.json",
  "../obsData/FromOriginal/Ferguson2014_WA2_Fmean_-65.0.json"
]
c.upload(data_files_from_Original, "eFELunit/FromOriginal", overwrite=True)

# upload observations: Model_SA
data_files_from_model_SA = [
  "../obsData/Model_SA/Ferguson2014_SA_AP1_amp.json",
  "../obsData/Model_SA/Ferguson2014_SA_AP1_peak.json",
  "../obsData/Model_SA/Ferguson2014_SA_AP1_width.json",
  "../obsData/Model_SA/Ferguson2014_SA_AP2_amp.json",
  "../obsData/Model_SA/Ferguson2014_SA_AP2_peak.json",
  "../obsData/Model_SA/Ferguson2014_SA_AP2_width.json",
  "../obsData/Model_SA/Ferguson2014_SA_APlast_amp.json",
  "../obsData/Model_SA/Ferguson2014_SA_APlast_width.json",
  "../obsData/Model_SA/Ferguson2014_SA_iv_curve.json",
  "../obsData/Model_SA/Ferguson2014_SA_spikecount.json",
  "../obsData/Model_SA/Ferguson2014_SA_time_to_first_spike.json",
  "../obsData/Model_SA/Ferguson2014_SA_time_to_last_spike.json",
  "../obsData/Model_SA/Ferguson2014_SA_time_to_second_spike.json"
]
c.upload(data_files_from_model_SA, "eFELunit/Model_SA", overwrite=True)

# upload observations: Model_WA1
data_files_from_model_WA1 = [
  "../obsData/Model_WA1/Ferguson2014_WA1_AP1_amp.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_AP1_peak.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_AP1_width.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_AP2_amp.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_AP2_peak.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_AP2_width.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_APlast_amp.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_APlast_width.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_iv_curve.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_spikecount.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_time_to_first_spike.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_time_to_last_spike.json",
  "../obsData/Model_WA1/Ferguson2014_WA1_time_to_second_spike.json"
]
c.upload(data_files_from_model_WA1, "eFELunit/Model_WA1", overwrite=True)

# upload observations: Model_WA2
data_files_from_model_WA2 = [
  "../obsData/Model_WA2/Ferguson2014_WA2_AP1_amp.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_AP1_peak.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_AP1_width.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_AP2_amp.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_AP2_peak.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_AP2_width.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_APlast_amp.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_APlast_width.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_iv_curve.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_spikecount.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_time_to_first_spike.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_time_to_last_spike.json",
  "../obsData/Model_WA2/Ferguson2014_WA2_time_to_second_spike.json"
]
c.upload(data_files_from_model_WA2, "eFELunit/Model_WA2", overwrite=True)


