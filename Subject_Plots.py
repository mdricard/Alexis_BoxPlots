import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", palette="Dark2")

csv = np.genfromtxt('D:/Alexis_Stats/Alexis_Final_Data_Juneteenth.csv', delimiter=',',skip_header=1)

# Convert NumPy array to Pandas DataFrame
all_data = pd.DataFrame(csv, columns=['subject', 'shoe', 'speed', 'incline', 'step','comp_force','comp_impulse','shear_force', 'shear_impulse' ,'add_mom', 'add_impulse', 'trail_prop', 'lead_braking','hip_ron', 'knee_ron'])

hoka = all_data[all_data["shoe"] == 0]
hoka_level = hoka[hoka["incline"] == 0]
hoka_uphill = hoka[hoka["incline"] == 1]
hoka_downhill = hoka[hoka["incline"] == 2]
barefoot = all_data[all_data["shoe"] == 1]
barefoot_level = barefoot[barefoot["incline"] == 0]
barefoot_uphill = barefoot[barefoot["incline"] == 1]
barefoot_downhill = barefoot[barefoot["incline"] == 2]

sns.boxplot(x="subject", y="comp_force", color='black', fill=False, data=hoka_level)
sns.stripplot(x="subject", y="comp_force", data=hoka_level, color="blue", alpha=0.6, jitter=True)
plt.grid(True)
plt.show()

#--------------------------   Hoka  Level  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=hoka_level)
sns.despine(offset=10, trim=True)
ax.set_title("Hoka Neutral by Speed")        # Add title and labels
#ax = sns.stripplot(x="subject", y="comp_force", data=hoka_level, color="blue", alpha=0.6, jitter=True)
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()
#--------------------------   Hoka  Uphill  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=hoka_uphill)
sns.despine(offset=10, trim=True)
ax.set_title("Hoka Uphill by Speed")        # Add title and labels
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()
#--------------------------   Hoka  Downhill  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=hoka_downhill)
sns.despine(offset=10, trim=True)
ax.set_title("Hoka Downhill by Speed")        # Add title and labels
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()


#--------------------------   Barefoot  Level  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=barefoot_level)
sns.despine(offset=10, trim=True)
ax.set_title("Barefoot Neutral by Speed")        # Add title and labels
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()
#--------------------------   Barefoot  Uphill  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=barefoot_uphill)
sns.despine(offset=10, trim=True)
ax.set_title("Barefoot Uphill by Speed")        # Add title and labels
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()
#--------------------------   Barefoot  Downhill  -----------------------------
ax = sns.boxplot(x="speed", y="add_mom",
            hue='subject', legend=False,
            data=barefoot_downhill)
sns.despine(offset=10, trim=True)
ax.set_title("Barefoot Downhill by Speed")        # Add title and labels
ax.set_xticklabels(['0.5', '0.8', '1.2'])  # Custom
ax.set_xlabel("Walking Speed (m/s)")
ax.set_ylabel("Adduction Moment (%BWxHt)")
plt.show()
# Subset rows where shoe is Hoka, incline is level and speed is 0.5 m/s
#subset = df[(df['shoe'] == 0) & (df['incline'] == 0) & (df['speed'] == 0)]
#subset = df[df['shoe'] == 0]
#print(subset.head())



"""""
sns.boxplot(x="subject", y="comp_force", color='black', fill=False, data=subset)
sns.swarmplot(x="subject", y="comp_force", data=subset, size=5, color="blue", alpha=0.6)
plt.grid(True)
plt.show()
"""