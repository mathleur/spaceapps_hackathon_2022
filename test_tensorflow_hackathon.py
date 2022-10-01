
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
