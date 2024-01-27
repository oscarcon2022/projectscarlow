#Oscar Contreras
#Carlow University
#Cleaning Data

#locations.csv file is the only one to clean in the set
import pandas as pd 


# cleaning the locations file 
l = pd.read_csv('./data/orig/locations.csv')

# Check the number of null values like we did in class
print("Number of null values before filling:", l.isnull().sum().sum())

# Fill null values in the 'region_id' column with the number 10
l['region_id'].fillna(10, inplace=True)

# Check the number of null values after filling
print("Number of null values after filling:", l.isnull().sum().sum())

# Change the name of the 'identifier' column to 'locations_id'. make it easier to read for the user
l = l.rename(columns={'identifier': 'locations_id'})

# Save the modified DataFrame back to the CSV file in the original directory
l.to_csv('./data/orig/locations.csv', index=False)


# Save the modified DataFrame to a new file in the clean directory
l.to_csv('./data/clean/locations.csv')










