# -*- coding: utf-8 -*-
"""PDS_Assignment1-Question2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FHBM7HHyAqwUfI9rtfJXHOIBaU5OsJOT
"""

import pandas as pd

from matplotlib import pyplot as plt

StudentsPerformance = pd.read_csv("/content/StudentsPerformance.csv")

StudentsPerformance

# Scatter plot with parental level of education against math score
plt.scatter(StudentsPerformance['parental level of education'], StudentsPerformance['math score'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('parental level of education')
plt.ylabel('math score')

plt.show()

# Bar chart with day against tip
plt.bar(StudentsPerformance['parental level of education'], StudentsPerformance['math score'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('parental level of education')
plt.ylabel('math score')

# Adding the legends
plt.show()

# histogram of reading score
plt.hist(StudentsPerformance['reading score'])

plt.title("Histogram")

# Adding the legends
plt.show()

import seaborn as sns

# draw lineplot
sns.lineplot(x="gender", y="reading score", data=StudentsPerformance)

# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')

plt.show()

sns.barplot(x='gender',y='reading score', data=StudentsPerformance,
            hue='lunch')

plt.show()
