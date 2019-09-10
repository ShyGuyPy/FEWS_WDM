#

# ------------Import Python Modules-----------#
from wdmtoolbox import wdmtoolbox
from pathlib import Path
import glob
import pandas
import numpy
# --------------------------------------------#


#this is the directory where the raw wdm files are placed
source_dir_met = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met"
source_dir_prad = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\prad"

#create object containing all files in for met and prad
allFiles1 = glob.glob(source_dir_met + "/*met*.wdm*")
allFiles2 = glob.glob(source_dir_prad+ "/*prad*.wdm*")

#our file destintion
output_folder = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"


#iterate through the met files
for file in allFiles1:
    #takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    #use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1000)

    list(data_df.columns)
    check = data_df.iloc[0,0]
    print(check)

    #data_df['year'] = pandas.Series(numpy.random.randn(len(data_df['Datetime'])), index=data_df.index)
    # data_df['day'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
    # data_df['month'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
    # data_df['hour'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
    #format the data
    #print(data_df)

    # count = 0
    # for index in data_df['year']:
    #     count +=1
    #
    # print("count ="+ count)

    #then we immediatly write the data to a csv assigning the designated file extension
    data_df.to_csv(output_folder +"/" + title + ".PET")
    #data_df.to_csv(output_folder +"/" + title + ".csv")

    #we repeat the process for all
    # data_df = wdmtoolbox.extract(file, 1001)
    # data_df.to_csv(output_folder +"/" + title + ".DPT")
    #
    # data_df = wdmtoolbox.extract(file, 1002)
    # data_df.to_csv(output_folder +"/" + title + ".WND")
    #
    # data_df = wdmtoolbox.extract(file, 1003)
    # data_df.to_csv(output_folder +"/" + title + ".RAD")
    #
    # data_df = wdmtoolbox.extract(file, 1004)
    # data_df.to_csv(output_folder +"/" + title + ".TMP")










