"""
Script: Code Decoder and CSV Modifier

Description:
This Python script decodes technology and fuel codes.
The main function creates a new or updates a CSV file with appended decoded descriptions in a new column.

Functions:
1. decode_code(code): decodes a single fuel or tech code of 4 or 9 digits.
3. add_code_descriptions_to_csv(input_csv_filename, output_csv_filename=None): creates a new csv file including a new column with code descriptions.

Example Usages:
```python
code = 'DEBFCCH1'
print(decode_code(code))
# Output: Germany (DE)| Biofuel (BF)| Combined cycle (CC)| Primary energy commodity (P)| age 1| size 1	
```	
or
```python	
input_csv_filename = 'input_data\\FUEL.csv'
output_csv_filename = 'output_codes_fuel.csv'
add_code_descriptions_to_csv(input_csv_filename, output_csv_filename)
# Output: Code descriptions saved to 'output_codes_fuel.csv'.
```
Author: Timon Renzelmann
"""

import sys
import pandas as pd
import os

# Define code mappings
country_codes = {
    'AT': 'Austria',
    'BE': 'Belgium',
    'BG': 'Bulgaria',
    'CH': 'Switzerland',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DE': 'Germany',
    'DK': 'Denmark',
    'EE': 'Estonia',
    'ES': 'Spain',
    'FI': 'Finland',
    'FR': 'France',
    'GR': 'Greece',
    'HR': 'Croatia',
    'HU': 'Hungary',
    'IE': 'Ireland',
    'IT': 'Italy',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'MT': 'Malta',
    'NL': 'the Netherlands',
    'NO': 'Norway',
    'PL': 'Poland',
    'PT': 'Portugal',
    'RO': 'Romania',
    'SE': 'Sweden',
    'SI': 'Slovenia',
    'SK': 'Slovakia',
    'UK': 'United Kingdom'
}


commodity_codes = {
    'BF': 'Biofuel',
    'BM': 'Biomass',
    'CO': 'Coal',
    'EL': 'Electricity',
    'E1': 'Electricity 1',
    'E2': 'Electricity 2',
    'GO': 'Geothermal',
    'HF': 'Heavy fuel oil',
    'HY': 'Hydro',
    'NG': 'Natural gas',
    'NU': 'Nuclear',
    'OC': 'Ocean',
    'OI': 'Oil',
    'OS': 'Oil Shale',
    'SO': 'Sun',
    'UR': 'Uranium',
    'WS': 'Waste',
    'WI': 'Wind',
}

technology_codes = {
    'CC': 'Combined cycle',
    'CH': 'Combined heat and power',
    'CS': 'Carbon Capture and Storage',
    'CV': 'Conventional',
    'DI': 'Distributed PV',
    'DM': 'Dam',
    'DS': 'Pumped Storage',
    'FC': 'Fuel cell',
    'GC': 'Gas cycle',
    'G2': 'Generation 2',
    'G3': 'Generation 3',
    'HP': 'Internal combustion engine with heat recovery',
    'OF': 'Offshore',
    'ON': 'Onshore',
    'ST': 'Steam cycle',
    'UT': 'Utility PV',
    'WV': 'Wave power',
}

energy_level_codes = {
    'P': 'Primary energy commodity',
    'F': 'Final electricity',
    'I': 'Import technology',
    'X': 'Extraction or generation technology',
}

def decode_tech(tech_code):
    """Decodes a single technology code of 9 digits.
    
    Args:
        tech_code (str): The technology code to decode.
        
    Returns:
        str: The decoded description of the technology code.
    """
    if len(tech_code) != 9:
        return "Error: Code length must be 9"

    country = tech_code[0:2]
    commodity = tech_code[2:4]
    technology = tech_code[4:6]
    energy_level = tech_code[6]
    age = tech_code[7]
    size = tech_code[8]

    country_description = country_codes.get(country, f'Unknown country')
    commodity_description = commodity_codes.get(commodity, f'Unknown commodity')
    if technology in technology_codes:
        technology_description = technology_codes[technology]
    elif technology in country_codes:
            technology_description = f'connected to {country_codes[technology]}'
    else:
        technology_description = 'Unknown technology'
    energy_level_description = energy_level_codes.get(energy_level, f'Unknown energy level')
    age_description = f'age {age}'
    size_description = f'size {size}'

    full_description = (
        f"{country_description} ({country})| "
        f"{commodity_description} ({commodity})| "
        f"{technology_description} ({technology})| "
        f"{energy_level_description} ({energy_level})| "
        f"{age_description}| "
        f"{size_description}"
    )

    return full_description

def decode_fuel(fuel_code):
    """Decodes a single fuel code of 4 digits.
    
    Args:
        fuel_code (str): The fuel code to decode.
        
    Returns:
        str: The decoded description of the fuel code.
    """
    if len(fuel_code) != 4:
        return "Error: Code length must be 4"

    country = fuel_code[0:2]
    commodity = fuel_code[2:4]

    country_description = country_codes.get(country, f'Unknown country')
    commodity_description = commodity_codes.get(commodity, f'Unknown commodity')
    
    full_description = (
        f"{country_description} ({country})| "
        f"{commodity_description} ({commodity})"
    )

    return full_description

def decode_code(code):
    """Decodes a single code of 4 or 9 digits.
    
    Args:
        code (str): The code to decode.
        
    Returns:
        str: The decoded description of the code.
    """
    if len(code) == 9:
        return decode_tech(code)
    elif len(code) == 4:
        return decode_fuel(code)
    else:
        return "Error: Code length must be 4 or 9"
    
def add_code_descriptions_to_csv(input_csv_filename, output_csv_filename=None):
    """Modifies a CSV file by adding a ' #codedescription' column.
    
    This function reads a CSV file containing codes in one column, decodes each
    code using the decode_tech function for 9 digit codes and decode_fuel for 4-digit codes,
    and adds a new column to the CSV file with the decoded descriptions in the format ' #codedescription'.
    It overrides the input CSV file with the modified data if the output file name is not provided
    or if it's the same as the input file name.
    
    Args:
        input_csv_filename (str): The name of the input CSV file.
        output_csv_filename (str, optional): The name of the output CSV file.
    
    Returns:
        None
    """
    try:
        # Read the input CSV file
        df = pd.read_csv(input_csv_filename, header=None)

        # Store the existing header
        header = df.iloc[0].tolist()
        header.append("description")
        df1 = pd.DataFrame([header])

        # Remove the header from the DataFrame
        df = df.iloc[1:]

        # Apply the decode_tech or decode_fuel function based on code length and add a new column
        df[1] = df.apply(lambda row: f'#{decode_tech(row[0])}' if len(row[0]) == 9 and not pd.isna(row[0])
                         else (f' #{decode_fuel(row[0])}' if len(row[0]) == 4 and not pd.isna(row[0])
                               else ''), axis=1)
        #create new dataframe
        df = pd.concat([df1, df], ignore_index=True)

        if output_csv_filename is None or output_csv_filename == input_csv_filename:
            while True:
                overwrite_input = input(f"Overwrite '{input_csv_filename}'? (yes/no): ").strip().lower()
                if overwrite_input == 'yes':
                    # Save the modified DataFrame back to the input CSV file, overriding it
                    df.to_csv(input_csv_filename, index=False, header=False)
                    print(f"Code descriptions added to '{input_csv_filename}'.")
                    break
                elif overwrite_input == 'no':
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

        else:
            # Save the modified DataFrame to the output CSV file
            df.to_csv(output_csv_filename, index=False, header=False)
            print(f"Code descriptions saved to '{output_csv_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Add a new functions to handle decoding codes from the command line
def decode_code_from_cli():
    if len(sys.argv) != 3:
        print("Usage: python script.py decode_code code")
    else:
        code = sys.argv[2]
        result = decode_code(code)
        print(result)
  
if __name__ == '__main__':
    # input_file = 'input_data\\WP1_NetZero\\data\\TECHNOLOGY.csv'
    # output_file = 'tech_codes.csv'
    # input_file2 = 'input_data\WP1_NetZero\data\FUEL.csv'
    # output_file2 = 'fuel_codes.csv'
    # add_code_descriptions_to_csv(input_file, output_file)
    # add_code_descriptions_to_csv(input_file2, output_file2)
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py input_file [output_file]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        add_code_descriptions_to_csv(input_file, output_file)