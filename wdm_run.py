#

# ------------Import Python Modules-----------#
from wdmtoolbox import wdmtoolbox
import pandas
from pathlib import Path
import glob

# --------------------------------------------#

# ------------Class for handling files-----------#
class FileType(object):
    def __init__(self, filepath, dsn):
        self.filepath = filepath
        self.dsn = dsn

    naming_dict = {
    1000:".PET", 1001:".DPT", 1002:".WND", 1003:".RAD", 1004:".TMP",
        1005:"", 2000:".PRC"

    }

    def extract(self):
        extracted = wdmtoolbox.extract(self.filepath, self.dsn)
        return extracted

    def push(self):
        pass

# --------------------------------------------#

#this is the directory where the raw wdm files are placed
source_dir_met = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met"
source_dir_prad = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\prad"
#source_dir = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/inputs/")

allFiles1 = glob.glob(source_dir_met + "/*met*.wdm*")
allFiles2 = glob.glob(source_dir_prad+ "/*prad*.wdm*")

#data_folder = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/output/")
data_folder = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"


# test = data_folder + "met_A11001.wdm"
# print(test)
# title = test[-10:-4]
# print(title)
# print(type(title))

for file in allFiles1:
    title = file[-10:-4]
    test1 = wdmtoolbox.extract(file, 1000)
    test1.to_csv(data_folder +"/" + title + ".PET")

    test1 = wdmtoolbox.extract(file, 1001)
    test1.to_csv(data_folder +"/" + title + ".DPT")

    test1 = wdmtoolbox.extract(file, 1002)
    test1.to_csv(data_folder +"/" + title + ".WND")

    test1 = wdmtoolbox.extract(file, 1003)
    test1.to_csv(data_folder +"/" + title + ".RAD")

    test1 = wdmtoolbox.extract(file, 1004)
    test1.to_csv(data_folder +"/" + title + ".TMP")

# file_name = "C:\\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met_A11001.wdm"
# test = FileType(file_name, 1004)
# ex_test = test.extract()
#print(ex_test)









data_folder = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/output/")

file = "C:\\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met_A11001.wdm"
destination = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"
dataatmp = wdmtoolbox.extract(file, 1004)
dataevap = wdmtoolbox.extract(file, 1000)

#print(dataatmp)
# print(type(dataevap))

#test_csv = wdmtoolbox.csvtowdm(file, 1004, dataatmp )
#test_csv =dataatmp.to_csv(data_folder/"test_csv.TMP")
#print(test_csv)