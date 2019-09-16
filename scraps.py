
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


#output_folder = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/output/")
#source_dir = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/inputs/")


# test = output_folder + "met_A11001.wdm"
# print(test)
# title = test[-10:-4]
# print(title)
# print(type(title))



# file_name = "C:\\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met_A11001.wdm"
# test = FileType(file_name, 1004)
# ex_test = test.extract()
#print(ex_test)




output_folder = Path("C:/Users/icprbadmin/Documents/Python_Scripts/FEWS_WDM/output/")

file = "C:\\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\input\met_A11001.wdm"
destination = r"C:\Users\icprbadmin\Documents\Python_Scripts\FEWS_WDM\output"
dataatmp = wdmtoolbox.extract(file, 1004)
dataevap = wdmtoolbox.extract(file, 1000)

#print(dataatmp)
# print(type(dataevap))

#test_csv = wdmtoolbox.csvtowdm(file, 1004, dataatmp )
#test_csv =dataatmp.to_csv(output_folder/"test_csv.TMP")
#print(test_csv)



list(data_df.columns)
check = data_df.iloc[0, 0]
print(check)

# data_df['year'] = pandas.Series(numpy.random.randn(len(data_df['Datetime'])), index=data_df.index)
# data_df['day'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
# data_df['month'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
# data_df['hour'] = pandas.Series(numpy.random.randn(len(data_df['datetime'])), index=data_df.index)
# format the data
# print(data_df)

# count = 0
# for index in data_df['year']:
#     count +=1
#
# print("count ="+ count)