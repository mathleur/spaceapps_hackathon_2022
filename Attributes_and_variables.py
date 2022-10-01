import os
import numpy as np
os.environ["CDF_LIB"] = "C:\\CDF\\lib"
from spacepy import pycdf

# Wind variables
cdf_pycdf_wind = pycdf.CDF("wi_h2_mfi_20220101_v04.cdf")
wind_features = []
print("wind Features: \n")
for feature in cdf_pycdf_wind:
  print("\n", feature, "\n")
  print(cdf_pycdf_wind[feature].attrs)
  # f.write(cdf_pycdf_wind[feature].attrs)
  wind_features.append(feature)


print(f'There are {len(wind_features)} features including: ')
print(cdf_pycdf_wind)

# Magnetic variables
cdf_pycdf_mag = pycdf.CDF("dscovr_h0_mag_20220101_v01.cdf")
mag_features = []
print("Magnetic Features: \n")
for feature in cdf_pycdf_mag:
  print("\n", feature, "\n")
  print(cdf_pycdf_mag[feature].attrs)
  # f.write(cdf_pycdf_wind[feature].attrs)
  mag_features.append(feature)


print(f'There are {len(mag_features)} features including: ')
# for feature in mag_features:
#   print(feature)
print(cdf_pycdf_mag)

# print(mag_features)

# cdf_pycdf2 = pycdf.CDF("dscovr_h0_mag_20220101_v01.cdf")
# print(cdf_pycdf["BF1"].attrs)