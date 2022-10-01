
import os
import numpy as np
os.environ["CDF_LIB"] = "C:\\CDF\\lib"
from spacepy import pycdf
import cdflib

cdf_pycdf = pycdf.CDF("2022.cdf")
print(cdf_pycdf)
print(cdf_pycdf["B1F1"][1])
tseries=cdf_pycdf["B1F1"]
print(cdf_pycdf1[1])
cdf_pycdf1=cdflib.CDF("2022.cdf")
x = cdf_pycdf1.varget("B1F1", startrec = 0, endrec = 84000)
print(type(x))
#print(tseries.dtype)


# import os
# import numpy as numpy
# os.environ["CDF_LIB"] = "C:\\CDF\\lib"

# from spacepy import pycdf
# cdf_pycdf = pycdf.CDF("wi_h2_mfi_20220101_v04.cdf")
# # cdf_pycdf2 = pycdf.CDF("dscovr_h0_mag_20220101_v01.cdf")
# print(cdf_pycdf["BF1"].attrs)