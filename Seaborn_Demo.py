import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker", data=df)
plt.grid(True)
plt.show()
