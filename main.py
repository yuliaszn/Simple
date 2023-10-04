import pandas as pd
import matplotlib.pyplot as plt


df_inifian = pd.read_csv(r'datetime/team.csv')

print(df_inifian, ['data'])

fig,ax = plt.subplots( figsize = (10 , 6))
ax.plot(df_inifian['Data'], df_inifian['Time'], '-')
plt.legend(["This is my legend"], fontsize="x-large")
plt.show()