# OSEMBE Code Decoder and CSV Modifier

## Overview

This Python script is designed to decode technology and fuel codes and append the decoded descriptions to a CSV file as a new column. It can be used to enhance the readability and understanding of OSEMBE data.

## Author

- **Author:** Timon Renzelmann

## Functions

The script includes the following functions:

1. `decode_code(code)`: Returns the decoded description of a single 4-digit fuel code or a 9-digit technology code.
2. `add_code_descriptions_to_csv(input_csv_filename, output_csv_filename=None)`: Creates a new CSV file with a new column containing code descriptions. When the output file is none or equals the input file, it will replace the input file.

## Example Usages

Here's an example of how to use the script:

```python 
input_csv_filename = 'TECHNOLOGY.csv'
output_csv_filename = 'TECHNOLOGY_explained.csv'
add_code_descriptions_to_csv(input_csv_filename, output_csv_filename)
```
## Command Line Usage

You can use the script from the command line with the following usages:

```bash
# To decode a fuel or tech code:
python code_decipherer.py decode_code CODE

# To add code descriptions to a CSV file:
python code_decipherer.py add_code_descriptions_to_csv INPUT_CSV_FILENAME [OUTPUT_CSV_FILENAME]
```

