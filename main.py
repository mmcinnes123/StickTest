### TO DO BEFORE RUNNING THIS CODE
# Tidy up input .csv file so there's only one heading row and any rows on bottom are deleted
# Change settings:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
import seaborn as sns

# Settings:
input_file = "MagTest9.csv"
# Type of data (slow, fast, DZ, mov, stat)
ty_data = "slow_mov"

# Set names based on settings
boxplot_title = "Standard deviation - " + str(ty_data)
boxplot_figname = "SD_BoxPlot_" + str(ty_data) + ".png"
SDvTime_scattertitle = "Pitch SD - " + str(ty_data)
SDvTime_figname_Pitch = "SDvTime(Pitch)_" + str(ty_data) + ".png"
SDvTime_figname_Roll = "SDvTime(Roll)_" + str(ty_data) + ".png"
SDvTime_figname_Yaw = "SDvTime(Yaw)_" + str(ty_data) + ".png"


logging.basicConfig(filename='std.log', level=logging.INFO)
logging.info("Input file: " + input_file)
logging.info("Test type: " + ty_data)

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
    counter_Pitch = 0
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
            counter_Pitch += 1
            Pitch_mean_values.append(np.nan)
            Pitch_SD.append(np.std(np.nan))
        else:
            Pitch_mean_values.append(Average(lst))
            Pitch_SD.append(np.std(lst))
    logging.info("The number of samples excluded from the Pitch values was: " + str(counter_Pitch))

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
    counter_Roll = 0
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
            counter_Roll += 1
            Roll_mean_values.append(np.nan)
            Roll_SD.append(np.std(np.nan))
        else:
            Roll_mean_values.append(Average(lst))
            Roll_SD.append(np.std(lst))
    logging.info("The number of samples excluded from the Roll values was: " + str(counter_Roll))

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
    counter_Yaw = 0
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
            counter_Yaw += 1
            Yaw_mean_values.append(np.nan)
            Yaw_SD.append(np.std(np.nan))
        else:
            Yaw_mean_values.append(Average(lst))
            Yaw_SD.append(np.std(lst))
    logging.info("The number of samples excluded from the Yaw values was: " + str(counter_Yaw))


### Create a list and data frame of the SDs
SD = [Pitch_SD, Roll_SD, Yaw_SD]
SD = pd.DataFrame(list(zip(Pitch_SD, Roll_SD, Yaw_SD)), columns =['Pitch_SD', 'Roll_SD', 'Yaw_SD'])


### Create a boxplot of the SDs
plt.figure(1)
fig = plt.figure(figsize=(10, 8))
bp = sns.boxplot(SD, notch='True', showmeans='True')
Pitch_median = round(SD['Pitch_SD'].median(),2)
Roll_median = round(SD['Roll_SD'].median(),2)
Yaw_median = round(SD['Yaw_SD'].median(),2)
bp.set_xticklabels(["Pitch SD\nMedian = " + str(Pitch_median) + "\nNumber discounted = " + str(counter_Pitch),
                    "Roll SD\nMedian = " + str(Roll_median) + "\nNumber discounted = " + str(counter_Roll),
                    "Yaw SD\nMedian = " + str(Yaw_median) + "\nNumber discounted = " + str(counter_Yaw)])
# Adding title
plt.title(boxplot_title + "(" + input_file + ")")
plt.ylabel('Degrees')
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
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
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
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
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
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
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
