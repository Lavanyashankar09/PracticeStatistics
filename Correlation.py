import seaborn as sns
df = sns.load_dataset('iris')

#here sepal length and sepal width are negetively correlated
corr1 = df.corr()
#plot way
plot1 = sns.pairplot(df)