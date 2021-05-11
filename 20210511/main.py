# 정규분포(Boxplot)
'''
 - 사분위수(Quartile)
  - Q1,Q2(=median), Q3
    
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = np.random.normal(173.2,5.32,10000)
data.sort()

median=np.quantile(data,0.5)
q3=np.quantile(data,0.75)
q1=np.quantile(data,0.25)

iqr=q3-q1
b=q3-1.5*iqr
a=q1+1.5*iqr

print(a)
print(b)
#plt.boxplot(data)
#plt.show()


import pandas as pd
lst = [[1,2,3,4,5,6,7],
        [10,15,20,25,50,55,60],
        [0,0,0,0,0,0,0],
        [-1,-20,-30,-45,-50,-55,-70]]

df = pd.DataFrame(lst).T
corr = df.corr(method = 'pearson')
print(corr)

