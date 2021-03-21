from scr.data_management import LoadIrisDataset
import matplotlib.pyplot as plt
import seaborn as sns

df = LoadIrisDataset()
print(df)

sns.pairplot(df, hue='Species');
plt.show()