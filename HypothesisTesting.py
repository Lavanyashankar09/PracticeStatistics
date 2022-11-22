#Suppose the IQ in a certain population is normally distributed with a mean of μ = 100 and standard deviation of σ = 15.
#A researcher wants to know if a new drug affects IQ levels, so he recruits 20 patients to try it and records their IQ levels.
#The following code shows how to perform a one sample z-test in Python to determine if the new drug causes a significant difference in IQ levels:
#alpha is 0.05
    
#enter IQ levels for 20 patients
data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 
        105, 109, 109, 109, 110, 112, 112, 113, 114, 115]
    
from statsmodels.stats.weightstats import ztest as ztest
#z score, p value
z_test = ztest(data,value=100)
#p value < alpha 
#reject hypothesis


#t test
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,
      14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]

import numpy as np
ages_mean = np.mean(ages)

#for t test we should take sample of data
sample_size=10
age_sample=np.random.choice(ages,sample_size)
ages_sample_mean = np.mean(age_sample)

from scipy.stats import ttest_1samp
t_test = ttest_1samp(age_sample,30)
#same thing 
#if p value < alpha 
#reject hypothesis