import os
import numpy as np
os.environ["CDF_LIB"] = "C:\\CDF\\lib"
from spacepy import pycdf

# Wind variables
cdf_pycdf_wind = pycdf.CDF("wi_h2_mfi_20220101_v04.cdf")
cdf_pycdf_mag = pycdf.CDF("wi_h2_mfi_20220101_v04.cdf")
wind_features = []
mag_features = []
for feature in cdf_pycdf_wind:
  print(feature, cdf_pycdf_wind[feature].attrs)
  wind_features.append(feature)

for feature in cdf_pycdf_mag:
  mag_features.append(feature)

print(wind_features)
print(mag_features)

# cdf_pycdf2 = pycdf.CDF("dscovr_h0_mag_20220101_v01.cdf")
# print(cdf_pycdf["BF1"].attrs)