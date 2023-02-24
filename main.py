### TO DO BEFORE RUNNING THIS CODE
# Tidy up input .csv file so there's only one heading row
# Change settings:

# Settings:
input_file = "MagTest9.csv"
boxplot_title = "Standard deviation - Slow"
boxplot_figname = "SD_BoxPlot_Slow.png"
SDvTime_scattertitle = "Pitch SD - Slow"
SDvTime_figname = "SDvTime(Pitch)_Slow.png"

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

def Average(lst):
    return sum(lst)/len(lst)

### Time
with open(input_file, 'r') as file:
    columns = [8]
    df = pd.read_csv(file, usecols=columns)
    Time = df[df.columns[0]].values.tolist()

### Pitch
with open(input_file, 'r') as file:
    # Define which column headings are used
    columns1 = ["Quattro sensor 1: Pitch 1", "Quattro sensor 2: Pitch 2", "Quattro sensor 3: Pitch 3", "Quattro sensor 4: Pitch 4"]
    df = pd.read_csv(file, usecols=columns1)
    # Make a list of pitch for sensor 1
    Pitch_Sen1 = df['Quattro sensor 1: Pitch 1'].values.tolist()
    # Run through each row of the data frame to find the average and SD of all values
    Pitch_mean_values = []
    Pitch_SD = []
    for i in range(len(df)):
        Pitch_mean_values.append(Average(list(df.loc[i,:])))
        Pitch_SD.append(np.std(list(df.loc[i,:])))

### Roll
with open(input_file, 'r') as file:
    # Define which column headings are used
    columns2 = ["Quattro sensor 1: Roll 1", "Quattro sensor 2: Roll 2", "Quattro sensor 3: Roll 3", "Quattro sensor 4: Roll 4"]
    df = pd.read_csv(file, usecols=columns2)
    # Make a list of Roll for sensor 1
    Roll_Sen1 = df['Quattro sensor 1: Roll 1'].values.tolist()
    # Run through each row of the data frame to find the average and SD of all values
    Roll_mean_values = []
    Roll_SD = []
    for i in range(len(df)):
        Roll_mean_values.append(Average(list(df.loc[i,:])))
        Roll_SD.append(np.std(list(df.loc[i,:])))

### Yaw
with open(input_file, 'r') as file:
    # Define which column headings are used
    columns3 = ["Quattro sensor 1: Yaw 1", "Quattro sensor 2: Yaw 2", "Quattro sensor 3: Yaw 3", "Quattro sensor 4: Yaw 4"]
    df = pd.read_csv(file, usecols=columns3)
    # Make a list of Yaw for sensor 1
    Yaw_Sen1 = df['Quattro sensor 1: Yaw 1'].values.tolist()
    # Run through each row of the data frame to find the average and SD of all values
    Yaw_mean_values = []
    Yaw_SD = []
    for i in range(len(df)):
        Yaw_mean_values.append(Average(list(df.loc[i,:])))
        Yaw_SD.append(np.std(list(df.loc[i,:])))

# # Calculate the average value for the SD in each plane
Pitch_average_SD = Average(Pitch_SD)
Roll_average_SD = Average(Roll_SD)
Yaw_average_SD = Average(Yaw_SD)
SD = [Pitch_SD, Roll_SD, Yaw_SD]


print("The mean value of the SD deviation between four sensors for Pitch is: ", str(Pitch_average_SD))
print("The mean value of the SD deviation between four sensors for Roll is: ", str(Roll_average_SD))
print("The mean value of the SD deviation between four sensors for Yaw is: ", str(Yaw_average_SD))

### Create a boxplot of the SDs
plt.figure(1)
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111)
# Creating axes instance
bp = ax.boxplot(SD, patch_artist=True,
                notch='True', showmeans='True')

## Define settings of boxplot

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(linewidth=1.5)
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(linewidth=2)
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color='red',
               linewidth=3)
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker='D',
              color='#e7298a',
              alpha=0.5)

# x-axis labels
ax.set_xticklabels(['Pitch SD\nMedian = ' + str(round(bp['medians'][0].get_ydata()[0],2)), 'Roll SD\nMedian = ' + str(round(bp['medians'][1].get_ydata()[0],2)),
                    'Yaw SD\nMedian = ' + str(round(bp['medians'][2].get_ydata()[0],2))])

# Adding title
plt.title(boxplot_title)
plt.ylabel('Degrees')
# Show plot
# plt.show()
# Save plot
plt.savefig(boxplot_figname)
plt.clf()

### Plotting SD and angle against time, to see moments of poor agreement
plt.figure(2)
x = Time
y1 = Pitch_Sen1
y2 = Pitch_SD
plt.scatter(x, y1, s = 5)
plt.scatter(x,y2, s = 3)
plt.rcParams.update({'figure.figsize':(15,12), 'figure.dpi':100})
plt.title(SDvTime_scattertitle)
plt.xlabel('Time')
plt.ylabel('Degrees')
plt.legend(["Pitch angle", "Pitch SD between sensors"])
# plt.show()
plt.savefig(SDvTime_figname)
plt.clf()



# Unused code
# print(df.loc[:, ["Yaw SD"]])
# print(df.iloc[:,0])

# print(list(df.iloc[0,:]))
# x = list(df.iloc[0,:])
# print(Average(x))


# new = np.array(df.loc[:, ["Yaw SD"]])
# print(new)

# data = np.array(df)

