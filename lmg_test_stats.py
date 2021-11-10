import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

lmgs = pd.read_csv("SD2 Weapon Stats(Toulon) - Sheet9.csv")
reload = lmgs['time between "shots" in the magazine/salvo']
print(reload.describe())
sns.boxplot(x=reload)
sns.stripplot(x=reload, color='black')
plt.show()