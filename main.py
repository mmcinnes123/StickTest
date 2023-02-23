import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

def Average(lst):
    return sum(lst)/len(lst)

### Pitch
with open("MagTest9.csv", 'r') as file:
    # Define which column headings are used
    columns = ["Quattro sensor 1: Pitch 1", "Quattro sensor 2: Pitch 2", "Quattro sensor 3: Pitch 3", "Quattro sensor 4: Pitch 4"]
    df = pd.read_csv(file, usecols=columns)
    # Run through each row of the data frame to find the average and SD of all values
    Pitch_mean_values = []
    Pitch_SD = []
    for i in range(len(df)):
        Pitch_mean_values.append(Average(list(df.loc[i,:])))
        Pitch_SD.append(np.std(list(df.loc[i,:])))

### Roll
with open("MagTest9.csv", 'r') as file:
    # Define which column headings are used
    columns = ["Quattro sensor 1: Roll 1", "Quattro sensor 2: Roll 2", "Quattro sensor 3: Roll 3", "Quattro sensor 4: Roll 4"]
    df = pd.read_csv(file, usecols=columns)
    # Run through each row of the data frame to find the average and SD of all values
    Roll_mean_values = []
    Roll_SD = []
    for i in range(len(df)):
        Roll_mean_values.append(Average(list(df.loc[i,:])))
        Roll_SD.append(np.std(list(df.loc[i,:])))

### Yaw
with open("MagTest9.csv", 'r') as file:
    # Define which column headings are used
    columns = ["Quattro sensor 1: Yaw 1", "Quattro sensor 2: Yaw 2", "Quattro sensor 3: Yaw 3", "Quattro sensor 4: Yaw 4"]
    df = pd.read_csv(file, usecols=columns)
    # Run through each row of the data frame to find the average and SD of all values
    Yaw_mean_values = []
    Yaw_SD = []
    for i in range(len(df)):
        Yaw_mean_values.append(Average(list(df.loc[i,:])))
        Yaw_SD.append(np.std(list(df.loc[i,:])))

# Calculate the average value for the SD in each plane
Pitch_average_SD = Average(Pitch_SD)
Roll_average_SD = Average(Roll_SD)
Yaw_average_SD = Average(Yaw_SD)

print("The average value of the SD deviation between four sensors for Pitch is: ", str(Pitch_average_SD))
print("The average value of the SD deviation between four sensors for Roll is: ", str(Roll_average_SD))
print("The average value of the SD deviation between four sensors for Yaw is: ", str(Yaw_average_SD))








# Unused code
# print(df.loc[:, ["Yaw SD"]])
# print(df.iloc[:,0])

# print(list(df.iloc[0,:]))
# x = list(df.iloc[0,:])
# print(Average(x))


# new = np.array(df.loc[:, ["Yaw SD"]])
# print(new)

# data = np.array(df)