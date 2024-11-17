# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:53:41 2023

@author: gl450
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# Replace 'your_data_file.csv' with your CSV file name
csv_file = "E:/Corona Virus - Information/Cancer rates/Neoplasms_2018-2023.csv" 

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Filter by Underlying Cause of death Code with more than 1000 deaths
filtered_df = df[df['Deaths'] > 1000]

# Pivot the DataFrame to have years as columns, 'Ten-Year Age Groups Code' as index, and 'Deaths' as values
pivot_df = filtered_df.pivot_table(index='Ten-Year Age Groups Code', columns='Year Code', values='Deaths', aggfunc='sum')

# Plot the line chart
ax = pivot_df.plot(kind='line', marker='o')

# Set the x-axis labels to 'Ten-Year Age Groups Code'
ax.set_xticks(range(len(pivot_df.index)))
ax.set_xticklabels(pivot_df.index)

# Set the x-axis and y-axis labels
ax.set_xlabel('Ten-Year Age Groups Code')
ax.set_ylabel('Deaths')

# Set the plot title
ax.set_title('Deaths by Ten-Year Age Groups and Year')

# Add legend
ax.legend(title='Year')

# Display the plot
plt.show()