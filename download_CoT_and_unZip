import urllib
import zipfile


url="http://www.cftc.gov/files/dea/history/fut_disagg_xls_2016.zip"
file_name="fut_disagg_xls_2016.zip"
optional_target_folder="C:\\"

testfile = urllib.URLopener()
testfile.retrieve(url, file_name)

zfile = zipfile.ZipFile(file_name)#'fut_disagg_xls_2016.zip'
zfile.extractall(optional_target_folder)

zfile.close()

