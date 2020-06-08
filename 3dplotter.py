import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#Nicholas Kim, ORF 435 Final Project

strings = ["a67", "b67", "c67", "a70", "b70", "c70"]


for str in strings:
    df = pd.read_csv(r"C:\Users\Nick Kim\Documents\Nicholas Kim\School\School Semesters\Fall 2019 Semester\Risk Management\Final Project\plotXYZ\xyz_" + str + ".csv")

    X = df.iloc[0][1]
    Y = df.iloc[0][2]
    Z = df.iloc[0][3]

    def convert(y):
        y = y[1:len(y)-1]
        y = y.split(",")
        for i, val in enumerate(y):
            y[i] = float(val)
        return y

    X = convert(X)
    Y = convert(Y)
    Z = convert(Z)

    ax = plt.axes(projection='3d')
    ax.plot_trisurf(X, Y, Z,
                    cmap='viridis', edgecolor='none');

    strat = ""
    if (str[0] == "a"):
        strat = "Sharpe Optimal"
    if (str[0] == "b"):
        strat = "Conservative"
    if (str[0] == "c"):
        strat = "Bogle"
    plt.title("Age " + str[1:len(str)] + ", " + strat)
    plt.xlabel("Annual Savings Amount")
    plt.ylabel("Ret. Spending (%final salary)")
    ax.set_zlabel('Probability of Goal');
    plt.show()
