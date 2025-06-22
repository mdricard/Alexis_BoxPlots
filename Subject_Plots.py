import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv = np.genfromtxt('D:/Alexis_Stats/Alexis_Final_Data_Juneteenth.csv', delimiter=',',skip_header=1)

# Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(csv, columns=['subject', 'shoe', 'speed', 'incline', 'step','comp_force','comp_impulse','shear_force', 'shear_impulse' ,'add_mom', 'add_impulse', 'trail_prop', 'lead_braking','hip_ron', 'knee_ron'])
print(df.head())
