import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

flights = sns.load_dataset("flights")
flights.head()
may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
plt.show()
