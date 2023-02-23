# StickTest
Processing data from basic test with four IMUs moving together on a (relatively) straight piece of wood. 

main.py is used to find difference between each sensors estimation of its orientation, at every time sample. (Based on assumption that all sensors should have same orientation since they're rigidly attached and algined).
The standard deviation of this 'differnce' is calculated for each time sample, to give an indication of how much the sensors agree on their position throughout the movement. 
