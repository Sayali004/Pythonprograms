# 1. Plot the daily temperature (°C) for one week
import matplotlib.pyplot as plt
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temp=[30,32,31,29,28,27,26]
plt.plot(days, temp)
plt.title("Daily Temperature")
plt.show()


