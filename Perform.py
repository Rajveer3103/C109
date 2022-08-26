import pandas as pd
import statistics as st
import csv
df=pd.read_csv("StudentsPerformance.csv")
readingScore_list=df["reading score"].tolist()
#Mean for reading score
readingScore_mean=st.mean(readingScore_list)
#Median for reading score
readingScore_median=st.median(readingScore_list)
#Mode for reading score
readingScore_mode=st.mode(readingScore_list)
print("mean, median and mode of readingScore is {},{},{} respectively".format(readingScore_mean, readingScore_median, readingScore_mode))
#Standard deviation for height and weight
readingScore_std_deviation=st.stdev(readingScore_list)
#First, Second and Third standard deviation for height
readingScore_first_std_deviation_start, readingScore_first_std_deviation_end=readingScore_mean-readingScore_std_deviation, readingScore_mean+readingScore_std_deviation
readingScore_second_std_deviation_start, readingScore_second_std_deviation_end=readingScore_mean-(2*readingScore_std_deviation), readingScore_mean+(2*readingScore_std_deviation)
readingScore_third_std_deviation_start, readingScore_third_std_deviation_end=readingScore_mean-(3*readingScore_std_deviation), readingScore_mean+(3*readingScore_std_deviation)
#Percentage of data within first second and third standard deviation for height
readingScore_list_of_data_within_1_std_deviation=[result for result in readingScore_list if result>readingScore_first_std_deviation_start and result<readingScore_first_std_deviation_end]
readingScore_list_of_data_within_2_std_deviation=[result for result in readingScore_list if result>readingScore_second_std_deviation_start and result<readingScore_second_std_deviation_end]
readingScore_list_of_data_within_3_std_deviation=[result for result in readingScore_list if result>readingScore_third_std_deviation_start and result<readingScore_third_std_deviation_end]
#Printing data for height and weight(Standard Deviation)
print("{}% of data for readingScore lies within one standard deviation".format(len(readingScore_list_of_data_within_1_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within one standard deviation".format(len(readingScore_list_of_data_within_2_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within one standard deviation".format(len(readingScore_list_of_data_within_3_std_deviation)*100.0/len(readingScore_list)))





