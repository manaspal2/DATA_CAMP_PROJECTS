import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

########### READ DATA ###########
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
print (crimes)

############################################################
# Which hour has the highest frequency of crimes? 
# Store as an integer variable called peak_crime_hour.
############################################################
print (crimes["TIME OCC"].value_counts())
print (crimes["TIME OCC"].value_counts().index[0][0:2])

############################################################
# Which area has the largest frequency of night crimes 
# (crimes committed between 10pm and 3:59am)?
############################################################
n_cr_data_part1 = crimes[(crimes['TIME OCC'].astype(int)>2200) &
                          (crimes['TIME OCC'].astype(int)<=2359)]
n_cr_data_part2 = crimes[(crimes['TIME OCC'].astype(int)>0000) &
                          (crimes['TIME OCC'].astype(int)<=359)]
night_crime_data = pd.concat([n_cr_data_part1, n_cr_data_part2], ignore_index=True)
print (night_crime_data)
crime_area = crimes.groupby("AREA NAME").size().to_dict()
peak_night_crime_location = max(crime_area, key=crime_area.get)
print(f'Max crime are at night: {peak_night_crime_location}')

print("## Create an empty series ##")
victim_ages = pd.Series()
print (victim_ages)
print (">>====>>", len(crimes))

def vict_gr(df, lAge=0, hAge=0):
    global victim_ages
    if hAge != 0:
        print(f"Low limit of age: {lAge}")
        print(f"High limit of age: {hAge}")
        result = df[(df["Vict Age"] >= lAge) & (df["Vict Age"] <= hAge)]
        seriesIndex = str(lAge) + "-" + str(hAge)
    else:
        print(f"Low limit of age: {lAge}")
        result = df[df["Vict Age"] >= lAge]
        seriesIndex = str(lAge) + "+"
  
    if victim_ages.size==0:
        victim_ages = pd.Series([len(result)], index=[seriesIndex])
    else:
        new_series = pd.Series([len(result)], index=[seriesIndex])
        victim_ages = pd.concat([victim_ages, new_series])
    #print (victim_ages)
    return result

result = vict_gr(crimes, lAge=0, hAge=17)
print("############################################################")
result = vict_gr(crimes, lAge=18, hAge=25)
print("############################################################")
result = vict_gr(crimes, lAge=26, hAge=34)
print("############################################################")
result = vict_gr(crimes, lAge=35, hAge=44)
print("############################################################")
result = vict_gr(crimes, lAge=45, hAge=54)
print("############################################################")
result = vict_gr(crimes, lAge=55, hAge=64)
print("############################################################")
result = vict_gr(crimes, lAge=65)
print("############################################################")
print (victim_ages)