"""
Created on Fri Jan 19 21:09:11 2024

@author: oscarcontreras
"""


#Oscar Contreras
#Carlow University

import pandas as pd

# Read the clean CSV files into the program
p = pd.read_csv('./data/clean/pokemon.csv')
m = pd.read_csv('./data/clean/poke_moves.csv')
d = pd.read_csv('./data/clean/moves.csv')
l = pd.read_csv('./data/clean/locations.csv')

# Merge the datasets(did in class)
pm = p.merge(m, how="left", left_on='id', right_on="pokemon_id", suffixes=('_poke', '_pokemoves'))
pmd = pm.merge(d, how='left', left_on='move_id', right_on='id', suffixes=('_pm', '_d'))

# Delete the original datasets to save memory
del p
del m

# Keep the program running here with a while true loop
while True:
    # Welcome message
    print("Welcome to the Pokemon Data Explorer!")
    print("Choose an option:")
    print("1. Search By Name")
    print("2. Search By Region")
    print("3. Exit")

    # Get user input for option
    user_choice = input("Enter your choice (1, 2, or 3): ")

    if user_choice == "1":
        # Search By Name
        while True:
            pokemon_name = input("Enter the Pokemon name: ")
            # Filter data for the entered Pokemon name, perform necessary operations, and display results
            pokemon_data = pmd[pmd['identifier_pm'] == pokemon_name][['identifier_pm', 'identifier_d', 'power']].drop_duplicates().dropna().sort_values(by=['power'], ascending=False).head(4).groupby('identifier_pm').agg({"identifier_d": lambda x: ', '.join(x)}).rename(columns={"identifier_pm": "Name", "identifier_d": "Attacks"})

            if not pokemon_data.empty:
                print(pokemon_data)
                break
            else:
                print("Invalid Pokemon name. Please try again.")

    elif user_choice == "2":
        # Search By Region
        print(l)
        while True:
            region_name = input("Enter the Region name: ")
            # I Could not figure out how to make the user type the region name then get the pokemon and its 4 most powerful name out in the program.
            region_data = pmd[pmd['region_id'] == float(region_name)][['identifier_pm', 'identifier_d', 'power']].drop_duplicates().dropna().sort_values(by=['power'], ascending=False).head(4).groupby('identifier_pm').agg({"identifier_d": lambda x: ', '.join(x)}).rename(columns={"identifier_pm": "Name", "identifier_d": "Attacks"})
            if not region_data.empty:
                print(region_data)
                break
            else:
                print("Invalid Region ID. Please try again.")

    # Break option so the user can exit at any time
    elif user_choice == "3":
        print("Exiting the Pokemon Data Explorer. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    # Ask if the user wants to search another name or region or exit. Great option to keep the program running
    another_search = input("Would you like to search another name or region (yes/no) or press 3 to exit: ")
    if another_search.lower() != 'yes' and user_choice != '3':
        break

