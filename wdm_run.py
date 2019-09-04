#

# ------------Import Python Modules-----------#
from wdmtoolbox import wdmtoolbox
import pandas
from pathlib import Path

# --------------------------------------------#

data_folder = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/output/")


file = "C:\\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met_A11001.wdm"
destination = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"
dataatmp = wdmtoolbox.extract(file, 1004)
dataevap = wdmtoolbox.extract(file, 1000)

# print(dataevap)
# print(type(dataevap))

#test_csv = wdmtoolbox.csvtowdm(file, 1004, dataatmp )
test_csv =dataatmp.to_csv(data_folder/"test_csv.csv")
print(test_csv)