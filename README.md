<<<<<<< HEAD
# OSEMBE Code Decoder and CSV Modifier

## Overview

This Python script is designed to decode technology and fuel codes and append the decoded descriptions to a CSV file as a new column. It can be used to enhance the readability and understanding of OSEMBE data.

## Author

- **Author:** Timon Renzelmann

## Functions

The script includes the following functions:

1. `decode_tech(tech_code)`: Decodes a single 9-digit technology code.
2. `decode_fuel(fuel_code)`: Decodes a single 4-digit fuel code.
3. `add_code_descriptions_to_csv(input_csv_filename, output_csv_filename=None)`: Creates a new CSV file with a new column containing code descriptions. when the output file is none or equals the input file, it will replace it.

## Example Usages

Here's an example of how to use the script:

input_csv_filename = 'TECHNOLOGY.csv'
output_csv_filename = 'TECHNOLOGY_explained.csv'
add_code_descriptions_to_csv(input_csv_filename, output_csv_filename)

## Command Line Usage

You can use the script from the command line with the following usages:

```bash
# To decode a fuel code:
python code_decipherer.py decode_fuel FUEL_CODE

# To decode a technology code:
python code_decipherer.py decode_tech TECH_CODE

# To add code descriptions to a CSV file:
python code_decipherer.py add_code_descriptions_to_csv INPUT_CSV_FILENAME [OUTPUT_CSV_FILENAME]


