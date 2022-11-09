import numpy as np
import seaborn as sns
import statistics as st

## Define our dataset
df = sns.load_dataset("tips")

#mean
mean = np.mean(df["total_bill"])
#median
median = np.median(df["total_bill"])
#mode
mode = st.mode(df["total_bill"])

#boxplot
bp = sns.boxplot(df["total_bill"])

#percentiles
p = np.percentile(df["total_bill"],[25,75])

#Histogram
hp = sns.histplot(df["total_bill"])

#Histogram - to get loop, not normally distributed
hpT = sns.histplot(df["total_bill"], kde=True)

## Define our dataset
df1 = sns.load_dataset("iris")

#Histogram - normally distributed
hpT1 = sns.histplot(df1["sepal_width"], kde=True)

#to see count of species
cp1 = sns.countplot(df1["species"])

#percentiles
p1 = np.percentile(df1["sepal_length"],[25,75])

#first is my 25 percentile
#second is my 75 percentile
