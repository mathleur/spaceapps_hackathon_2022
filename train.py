import cdflib
cdf_pycdf = cdflib.CDF("wi_h2_mfi_20220101_v04.cdf")
BF1 = cdf_pycdf.varget("BF1", startrec = 0, endrec = 925803 - 1)
BGSE = cdf_pycdf.varget("BGSE", startrec = 0, endrec = 925803 - 1)
BGSM = cdf_pycdf.varget("BGSM", startrec = 0, endrec = 925803 - 1)
time = cdf_pycdf.varget("Time_PB5", startrec = 0, endrec = 925803 - 1)
# print(BF1)
# print(BGSE)
# print(BGSM[1])
print("time wind")
print(time)


cdf_pycdf = cdflib.CDF("dscovr_h0_mag_20220101_v01.cdf")
time = cdf_pycdf.varget("Time1_PB5", startrec = 0, endrec = 86400 - 1)
print("time magnetic")
# for i in range(86400):
#   print(time[i]-time[i + 1])
print(time)