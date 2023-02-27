### TO DO BEFORE RUNNING THIS CODE
# Tidy up input .csv file so there's only one heading row and any rows on bottom are deleted
# Change settings:

# Settings:
input_file = "MagTest9.csv"
# Type of data (slow, fast, DZ, mov, stat)
ty_data = "slow_mov"

boxplot_title = "Standard deviation - " + str(ty_data)
boxplot_figname = "SD_BoxPlot_" + str(ty_data) + ".png"
SDvTime_scattertitle = "Pitch SD - " + str(ty_data)
SDvTime_figname_Pitch = "SDvTime(Pitch)_" + str(ty_data) + ".png"
SDvTime_figname_Roll = "SDvTime(Roll)_" + str(ty_data) + ".png"
SDvTime_figname_Yaw = "SDvTime(Yaw)_" + str(ty_data) + ".png"

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
import seaborn as sns

logging.basicConfig(filename='std.log')

def Average(lst):
    return sum(lst)/len(lst)


# find out how many
with open(input_file, 'r') as file:
    columns = ["Quattro sensor 1: Pitch 1","Quattro sensor 1: Roll 1", "Quattro sensor 1: Yaw 1",
               "Quattro sensor 2: Pitch 2", "Quattro sensor 2: Roll 2", "Quattro sensor 2: Yaw 2",
               "Quattro sensor 3: Pitch 3", "Quattro sensor 3: Roll 3", "Quattro sensor 3: Yaw 3",
               "Quattro sensor 4: Pitch 4", "Quattro sensor 4: Roll 4", "Quattro sensor 4: Yaw 4"]
    df = pd.read_csv(file, usecols=columns)


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
    # Make a list of pitch for each sensor
    Pitch_Sen1 = df['Quattro sensor 1: Pitch 1'].values.tolist()
    # Run through each row of the data frame to find the average and SD of all values
    Pitch_mean_values = []
    Pitch_SD = []
    counter = 0
    for i in range(len(df)):
        # Make a list of the four values at each time sample
        lst = list(df.loc[i,:])
        # Only calculate the Mean and SD if the values aren't bridging the 180/-180 threshold
        # Check if they're large (around 180/-180, not around 0)
        are_near_180 = all(abs(val) > 100 for val in lst)
        # Check if they're all negative, or all positive
        are_neg = all(val < 0 for val in lst)
        are_pos = all(val > 0 for val in lst)
        # Check if we want to exclude them or not
        if (are_near_180 == True) and (are_neg == False) and (are_pos == False):
            counter += 1
            Pitch_mean_values.append(np.nan)
            Pitch_SD.append(np.std(np.nan))
        else:
            Pitch_mean_values.append(Average(lst))
            Pitch_SD.append(np.std(lst))
    print("The number of samples excluded from the Pitch values was: " + str(counter))

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
    counter = 0
    for i in range(len(df)):
        # Make a list of the four values at each time sample
        lst = list(df.loc[i,:])
        # Only calculate the Mean and SD if the values aren't bridging the 180/-180 threshold
        # Check if they're large (around 180/-180, not around 0)
        are_near_180 = all(abs(val) > 100 for val in lst)
        # Check if they're all negative, or all positive
        are_neg = all(val < 0 for val in lst)
        are_pos = all(val > 0 for val in lst)
        # Check if we want to exclude them or not
        if (are_near_180 == True) and (are_neg == False) and (are_pos == False):
            counter += 1
            Roll_mean_values.append(np.nan)
            Roll_SD.append(np.std(np.nan))
        else:
            Roll_mean_values.append(Average(lst))
            Roll_SD.append(np.std(lst))
    print("The number of samples excluded from the Roll values was: " + str(counter))

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
    counter = 0
    for i in range(len(df)):
        # Make a list of the four values at each time sample
        lst = list(df.loc[i,:])
        # Only calculate the Mean and SD if the values aren't bridging the 180/-180 threshold
        # Check if they're large (around 180/-180, not around 0)
        are_near_180 = all(abs(val) > 100 for val in lst)
        # Check if they're all negative, or all positive
        are_neg = all(val < 0 for val in lst)
        are_pos = all(val > 0 for val in lst)
        # Check if we want to exclude them or not
        if (are_near_180 == True) and (are_neg == False) and (are_pos == False):
            counter += 1
            Yaw_mean_values.append(np.nan)
            Yaw_SD.append(np.std(np.nan))
        else:
            Yaw_mean_values.append(Average(lst))
            Yaw_SD.append(np.std(lst))
    print("The number of samples excluded from the Yaw values was: " + str(counter))

# # Calculate the average value for the SD in each plane
# Pitch_average_SD = Average(Pitch_SD)
# Roll_average_SD = Average(Roll_SD)
# Yaw_average_SD = Average(Yaw_SD)

# mask = ~np.isnan(Pitch_SD)
# Pitch_SD = [d[m] for d, m in zip(Pitch_SD, mask)]
# mask = ~np.isnan(Roll_SD)
# Roll_SD = [d[m] for d, m in zip(Roll_SD, mask)]
# mask = ~np.isnan(Yaw_SD)
# Yaw_SD = [d[m] for d, m in zip(Yaw_SD, mask)]
SD = [Pitch_SD, Roll_SD, Yaw_SD]

# print("The mean value of the SD deviation between four sensors for Pitch is: ", str(Pitch_average_SD))
# print("The mean value of the SD deviation between four sensors for Roll is: ", str(Roll_average_SD))
# print("The mean value of the SD deviation between four sensors for Yaw is: ", str(Yaw_average_SD))


### Create a boxplot of the SDs
plt.figure(1)
fig = plt.figure(figsize=(15, 12))
bp = sns.boxplot(SD, notch='True', showmeans='True')


# Adding title
plt.title(boxplot_title)
plt.ylabel('Degrees')
# Show plot
# plt.show()
# Save plot
plt.savefig(boxplot_figname)
plt.clf()




### Plotting SD and angle against time, to see moments of poor agreement
# ONLY WORKS IF THERE ARE NO NANs IN DATA
# Pitch
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
plt.savefig(SDvTime_figname_Pitch)
plt.clf()

# Roll
plt.figure(2)
x = Time
y1 = Roll_Sen1
y2 = Roll_SD
plt.scatter(x, y1, s = 5)
plt.scatter(x,y2, s = 3)
plt.rcParams.update({'figure.figsize':(15,12), 'figure.dpi':100})
plt.title(SDvTime_scattertitle)
plt.xlabel('Time')
plt.ylabel('Degrees')
plt.legend(["Roll angle", "Roll SD between sensors"])
# plt.show()
plt.savefig(SDvTime_figname_Roll)
plt.clf()

# Yaw
plt.figure(2)
x = Time
y1 = Yaw_Sen1
y2 = Yaw_SD
plt.scatter(x, y1, s = 5)
plt.scatter(x,y2, s = 3)
plt.rcParams.update({'figure.figsize':(15,12), 'figure.dpi':100})
plt.title(SDvTime_scattertitle)
plt.xlabel('Time')
plt.ylabel('Degrees')
plt.legend(["Yaw angle", "Yaw SD between sensors"])
# plt.show()
plt.savefig(SDvTime_figname_Yaw)
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



# ax = fig.add_subplot(111)
# # Creating axes instance
# bp = ax.boxplot(SD, patch_artist=True,
#                 notch='True', showmeans='True')

# Define settings of boxplot
#
# # changing color and linewidth of
# # whiskers
# for whisker in bp['whiskers']:
#     whisker.set(linewidth=1.5)
# # changing color and linewidth of
# # caps
# for cap in bp['caps']:
#     cap.set(linewidth=2)
# # changing color and linewidth of
# # medians
# for median in bp['medians']:
#     median.set(color='red',
#                linewidth=3)
# # changing style of fliers
# for flier in bp['fliers']:
#     flier.set(marker='D',
#               color='#e7298a',
#               alpha=0.2)
#
# # x-axis labels
# bp.set_xticklabels(['Pitch SD\nMedian = ' + str(round(bp['medians'][0].get_ydata()[0],2)), 'Roll SD\nMedian = ' + str(round(bp['medians'][1].get_ydata()[0],2)),
#                     'Yaw SD\nMedian = ' + str(round(bp['medians'][2].get_ydata()[0],2))])
