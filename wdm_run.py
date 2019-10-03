#

# ------------Import Python Modules-----------#
from wdmtoolbox import wdmtoolbox
import glob
import pandas as pd
from sys import platform
# --------------------------------------------#

# ------------Set Directories base on Operating System-------------#
#if OS X/linux
if platform == "darwin" or platform == "linux" or platform == "linux2":

    # this is the directory where the raw wdm files are placed
    source_dir_met = r"/Users/lukevawter/Desktop/Python_ICPRB/FEWS_WDM/input/met"
    source_dir_prad = r"/Users/lukevawter/Desktop/Python_ICPRB/FEWS_WDM/input/prad"

    # create object containing all files in for met and prad
    allFiles1 = glob.glob(source_dir_met + "/*met*.wdm*")
    allFiles2 = glob.glob(source_dir_prad + "/*prad*.wdm*")

    # our file destination
    output_folder = r"/Users/lukevawter/Desktop/Python_ICPRB/FEWS_WDM/output"
    #print("mac os")

# if OS Windows
elif platform == "win32":

    #this is the directory where the raw wdm files are placed
    source_dir_met = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met"
    source_dir_prad = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\prad"

    #create object containing all files in for met and prad
    allFiles1 = glob.glob(source_dir_met + "/*met*.wdm*")
    allFiles2 = glob.glob(source_dir_prad+ "/*prad*.wdm*")

    #our file destination
    output_folder = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"
    #print("win32 os")
#---------------------------------------------------#

#------------iterate through the met files---#
for file in allFiles1:


#------------1000.PET-------------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1000)
    #add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df =pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                             )], sort=False)
    #then we add the values from the DatetimeIndex to the appropriate column
    data_df['year']= data_df.index.year
    data_df['month']= data_df.index.month
    data_df['day']= data_df.index.day
    data_df['hour']= data_df.index.hour
    #output the data to the output directory with the required file extension
    data_df.to_csv(output_folder +"/" + title + ".PET")
#-----------------------------------#

#------------1001.DPT-----------------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1001)
    #add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df =pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                             )], sort=False)
    #then we add the values from the DatetimeIndex to the appropriate column
    data_df['year']= data_df.index.year
    data_df['month']= data_df.index.month
    data_df['day']= data_df.index.day
    data_df['hour']= data_df.index.hour
    # output the data to the output directory with the required file extension
    data_df.to_csv(output_folder +"/" + title + ".DPT")
#-----------------------------------#

#----------------1002.WND--------------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1002)
    #add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df =pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                             )], sort=False)
    #then we add the values from the DatetimeIndex to the appropriate column
    data_df['year']= data_df.index.year
    data_df['month']= data_df.index.month
    data_df['day']= data_df.index.day
    data_df['hour']= data_df.index.hour
    # output the data to the output directory with the required file extension
    data_df.to_csv(output_folder +"/" + title + ".WND")
#----------------------------------#

#--------------------1003.RAD------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1003)
    # add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df = pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                               )], sort=False)
    # then we add the values from the DatetimeIndex to the appropriate column
    data_df['year'] = data_df.index.year
    data_df['month'] = data_df.index.month
    data_df['day'] = data_df.index.day
    data_df['hour'] = data_df.index.hour
    # output the data to the output directory with the required file extension
    data_df.to_csv(output_folder +"/" + title + ".RAD")
#-----------------------------------#

#--------------------1004.TMP------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1004)
    # add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df = pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                               )], sort=False)
    # then we add the values from the DatetimeIndex to the appropriate column
    data_df['year'] = data_df.index.year
    data_df['month'] = data_df.index.month
    data_df['day'] = data_df.index.day
    data_df['hour'] = data_df.index.hour
    #output the data to the output directory with the required file extension
    data_df.to_csv(output_folder +"/" + title + ".TMP")
#------------------------------------#
#------------------------------------#

#----------iterate through the prad files-------#
for file in allFiles2:

#-------------------2000.PRC------#
    # takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    # use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 2000)
    # add rows to dataframe to accommodate year, month, day and hour we will pull from our datetimeindex object
    data_df = pd.concat([data_df, pd.DataFrame(columns=("year", "month", "day", "hour")
                                               )], sort=False)
    # then we add the values from the DatetimeIndex to the appropriate column
    data_df['year'] = data_df.index.year
    data_df['month'] = data_df.index.month
    data_df['day'] = data_df.index.day
    data_df['hour'] = data_df.index.hour
    # output the data to the output directory with the required file extension
    data_df.to_csv(output_folder + "/" + title + ".PRC")
    # ------------------------------------#










