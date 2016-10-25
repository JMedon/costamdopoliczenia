from bs4 import BeautifulSoup
import pandas as pd

table = BeautifulSoup(open('C:/age0.html','r').read()).find('table')
df = pd.read_html(table) #I think it accepts BeatifulSoup object
                         #otherwise try str(table) as input

???  df = pd.read_html('path/to/file.html', flavor='bs4') 
  
