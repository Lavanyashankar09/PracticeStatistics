import numpy as np
import matplotlib.pyplot as plt

## Define our dataset
dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

plt.hist(dataset)

## Z Score
outliers=[]

def detect_outliers(data):
  threshold=3 ## 3 std deviation
  mean=np.mean(data)
  std=np.std(data)

  for i in data:
    z_score=(i-mean)/std
    if np.abs(z_score)> threshold:
      outliers.append(i)

  return outliers

detect_outliers(dataset)

#IQR
#1. Sort the data
dataset=sorted(dataset)
#2. Calculate Q1 aqnd Q3
q1,q3=np.percentile(dataset,[25,75])
#3. IQR(Q3-Q1)
iqr=q3-q1
#4. Find the Lower fence(q1-1.5(iqr))
lower_fence=q1-(1.5*iqr)
#5. Find the upper fence(q3+1.5(iqr))
higher_fence=q3+(1.5* iqr)

import seaborn as sns
sns.boxplot(dataset)
