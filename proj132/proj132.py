import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bright_stars.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()


plt.xlabel("radius")
plt.ylabel("mass")
plt.plot(radius,mass)
plt.show()



