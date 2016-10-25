import urllib
import os
import csv


myfolder="C:\\danestooq"

#import tickers from csv file
with open('Stooq_tickers.csv', 'r') as f:
  reader = csv.reader(f)
  tickers = list(reader)

print(tickers)

#loop to download all data from list
#http://stooq.pl/q/d/l/?s=cl.f&i=d

file_name=ticker
fullfilename = os.path.join(myFolder, filename)
url="http://stooq.pl/q/d/l/?s=" + ticker + "&i=d"
urllib.urlretrieve(url, fullfilename)


