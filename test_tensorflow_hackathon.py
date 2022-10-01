
import os
import numpy as np
os.environ["CDF_LIB"] = "C:\\CDF\\lib"
from spacepy import pycdf
import cdflib

cdf_pycdf1=cdflib.CDF("2022.cdf")[0]
cdf_pycdf = pycdf.CDF("2022.cdf")
print(cdf_pycdf)
print(cdf_pycdf["B1F1"][1])
tseries=cdf_pycdf["B1F1"]
print(cdf_pycdf1[1])
#print(tseries.dtype)