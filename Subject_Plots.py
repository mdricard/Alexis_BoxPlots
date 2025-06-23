import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv = np.genfromtxt('D:/Alexis_Stats/Alexis_Final_Data_Juneteenth.csv', delimiter=',',skip_header=1)

# Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(csv, columns=['subject', 'shoe', 'speed', 'incline', 'step','comp_force','comp_impulse','shear_force', 'shear_impulse' ,'add_mom', 'add_impulse', 'trail_prop', 'lead_braking','hip_ron', 'knee_ron'])
#print(df.head())
# Select rows where col1 is greater than 2 AND col2 is 'C'
#selected_rows = df[(df['col1'] > 2) & (df['col2'] == 'C')]
#print(selected_rows)

# Subset rows where shoe is Hoka, incline is level and speed is 0.5 m/s
subset = df[(df['shoe'] == 0) & (df['incline'] == 0) & (df['speed'] == 0)]
#subset = df[df['shoe'] == 0]
#print(subset.head())

sns.boxplot(x="subject", y="comp_force", color='black', fill=False, data=subset)
sns.stripplot(x="subject", y="comp_force", data=subset, color="blue", alpha=0.6, jitter=True)
plt.grid(True)
plt.show()

"""""
sns.boxplot(x="subject", y="comp_force", color='black', fill=False, data=subset)
sns.swarmplot(x="subject", y="comp_force", data=subset, size=5, color="blue", alpha=0.6)
plt.grid(True)
plt.show()
"""