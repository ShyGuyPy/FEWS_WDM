# -*- coding: utf-8 -*-
"""
01/29/2018

Description: extract and plot old and new met and prad wdms to qa NLDAS0
download and wdm overwrite process.

Input(s): .wdm
Output(s): png files

@author: aseck@icprb.org
Things To improve: create figures folders if
 they do not exist and use arrays
 for the met and prad variables
"""
# ------------Import Python Modules-----------#
import os
from wdmtoolbox import wdmtoolbox
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.image as mpimg
import glob
import datetime

# --------------------------------------------#
# ---------------------------------------------------------------------------#
# ---Define input/output file directories------------------------------------#
# new met directory
metdirectory1 = "Z:\MODEL\p52fc04_sa\input\scenario\climate\met\met8418"
# old met directory
metdirectory2 = "Z:\MODEL\p52fc04_sa\input\scenario\climate\met\met8416e_copy"
# where to save met figures
path1 = "Z:\MODEL\p52fc04_sa\output\icprb\wdmcheck\met8418"
# new prad directory
praddirectory1 = "Z:\MODEL\p52fc04_sa\input\scenario\climate\prad\prad8418"
# old prad directory
praddirectory2 = "Z:\MODEL\p52fc04_sa\input\scenario\climate\prad\prad8416e"
# where to save prad figures
path3 = "Z:\MODEL\p52fc04_sa\output\icprb\wdmcheck\prad8418"
allFiles1 = glob.glob(metdirectory1 + "/*met*.wdm*")
allFiles2 = glob.glob(praddirectory1 + "/*prad*.wdm*")

# ---------------------------------------------------------------------------#
# ---Define input/output file directories------------------------------------#

myFmt = mdates.DateFormatter('%m/%d')

# ---------------------------------------------------------------------------#
# ---get the date correcponding to three months ago--------------------------#

import datetime

i = datetime.datetime.now()
currentdate = i
# print i.month-1
if (i.month - 3 <= 0):
    correctmonth = i.month + 9
else:
    correctmonth = i.month - 3
if (i.month - 3 <= 0):
    correctyear = i.year - 1
else:
    correctyear = i.year
todaysdate = datetime.datetime(i.year, i.month, i.day)
# print todaysdate
threemonthago = datetime.datetime(correctyear, correctmonth, i.day)
# print threemonthago

# ---------------------------------------------------------------------------#
# ---going through the met files and prnt files with issues------------------#

# print 'Check the following files for negative values in wdms'


for file_ in allFiles1:
    title = file_[-10:-4]
    oldfile_ = glob.glob(metdirectory2 + "/met_" + title + ".wdm")
    figurename1 = path1 + "/atmp/atmp_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/atmp/old_atmp_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 1004)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 1004)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000)
        plt.suptitle(title + " Air temperature", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-20, 120])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Air temperature (F)')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-20, 120])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Air temperature (F)')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-20, 120])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Air temperature (F)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

        # wind speed
    title = file_[-10:-4]
    oldfile_ = glob.glob(metdirectory2 + "/met_" + title + ".wdm")
    figurename1 = path1 + "/wndh/wndh_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/wndh/old_wndh_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 1002)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 1002)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000)
        plt.suptitle(title + " Wind ", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-20, 120])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Wind  ()')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-20, 120])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Wind  ()')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-20, 120])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Wind  ()')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

        # evapotranspiration
    figurename1 = path1 + "/evap/evap_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/evap/old_evap_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 1000)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 1000)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000)
        plt.suptitle(title + " Evapotranspiration", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-0.05, 0.05])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Evapotranspiration (in)')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-0.05, 0.05])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Evapotranspiration (in)')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-0.05, 0.05])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Evapotranspiration (in)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

        # dew point temperature
    figurename1 = path1 + "/dewp/dewp_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/dewp/old_dewp_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 1001)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 1001)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000)
        plt.suptitle(title + " Dew point temperature", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-20, 120])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Temperature (F)')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-20, 120])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Temperature (F)')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-20, 120])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Temperature (F)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

        # solar radiation
    figurename1 = path1 + "/radh/radh_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/radh/old_radh_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 1001)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 1001)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000)
        plt.suptitle(title + " Solar radiation", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-20, 120])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Radiation (W/m2)')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-20, 120])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Radiation (W/m2)')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-20, 120])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Radiation (W/m2)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

    # ---going through the met files and prnt files with issues------------------#
# print 'Check the following files for negative values in wdms'


for file_ in allFiles2:
    title = file_[-10:-4]
    oldfile_ = glob.glob(praddirectory2 + "/prad_" + title + ".wdm")
    figurename1 = path3 + "/hprc/hprc_" + title + ".png"
    # print oldfile_[0]
    figurename2 = path1 + "/hprc/old_hprc_" + title + ".png"
    dataatmp1 = wdmtoolbox.extract(file_, 2000)
    dataatmp2 = wdmtoolbox.extract(oldfile_[0], 2000)
    df1 = dataatmp1
    df2 = dataatmp2
    df3 = df2.subtract(df1, fill_value=0)
    a = 1
    # textfile =  path1+ "/atmp/atmp_" +  title + ".txt"

    if a == 1:
        # print figurename1
        # f1=open(textfile)
        # f1=textfile
        # nv.to_csv(f1)
        # f1.close()
        fig, [ax1, ax2, ax3] = plt.subplots(nrows=3, ncols=1)
        fig.set_size_inches(10.5, 10.5)
        # fig.set_dpi(1000) /home/user1/MODEL/ICPRBextras/ExtrasV1.0/check_wdms
        plt.suptitle(title + " Precipitation", size="large")
        ax1.plot(dataatmp1, 'b')
        ax1.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax1.xaxis.set_major_formatter(myFmt)
        ax1.set_ylim([-0.05, 0.5])
        ax1.set_title('new wdm', color="blue", size="medium")
        ax1.set_ylabel('Precipitation (in)')

        ax2.plot(dataatmp2, 'g')
        ax2.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax2.xaxis.set_major_formatter(myFmt)
        ax2.set_ylim([-0.05, 0.5])
        ax2.set_title('old wdm', color="green", size="medium")
        ax2.set_ylabel('Precipitation (in)')

        ax3.plot(df3, 'r')
        ax3.set_xlim(['2017-01-01 00:00:00', currentdate])
        ax3.xaxis.set_major_formatter(myFmt)
        ax3.set_ylim([-0.05, 0.5])
        ax3.set_title('old wdm-new wdm', color="red", size="medium")
        ax3.set_ylabel('Precipitation (in)')

        fig.tight_layout()
        fig.subplots_adjust(top=0.88)

        plt.savefig(figurename1)
        plt.close(fig)

print
"Finished making met and prad figures in " + path1 + " and " + path3 + ". Please take a look"