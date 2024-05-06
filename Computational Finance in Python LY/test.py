from cmath import sqrt
import numpy as np
import pandas as pd
import plotnine
from plotnine.ggplot import *
import datetime
import calendar 
import locale


mat = np.arange(1,26).reshape(5,5)
# print(mat)

sigma = mat.sum()

N = mat[-1,-1]

mean = sigma/N

# sigma = 

data1 = {'city': ['Berlin', 'Hamburg', 'Munich'], 'state': ['Berlin', 'Hamburg', 'Bavaria'], 'population': [3520031,1787408,1450381]}
df1 = pd.DataFrame(data1)
print(df1)

df2 = pd.read_excel(r'/Users/alexandros/Desktop/BASF.xls')

a = np.array(df2)

b = np.log(a)
print(b)

returns = b[1:len(b)] - b[0:len(b)-1] # log-returns



print(returns) 

print(returns.mean())
print(returns.std()*sqrt(255))

a = datetime.date(1998, 11, 6)
print(a) 
b = datetime.date.today() 
print(b)
c=b-a
print(c)

x = calendar.Calendar(firstweekday=0)
calender_example = x.itermonthdates(2022, 4)
for i in calender_example: 
     print(i)