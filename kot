import pandas as pd
import matplotlib.pyplot as plt
df_inifian = pd.read_csv(r'C:\Users\95210\OneDrive\Рабочий стол\test.txt', sep=';')
print(df_inifian.columns)
fig,ax = plt.subplots(figsize=(10,6))
ax.plot(df_inifian['time'],df_inifian['data'],'o-r',label='line')
plt.legend(["This is my legend"],fontsize="x-large")
plt.show()
