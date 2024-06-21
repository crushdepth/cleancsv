# Clean-csv
#
# @author Simon Wilkinson
# @version 1.0
# @license GNU General Public License (GPL) V2
# @date 2024-06-21
# @description Clean up user input in .csv files, typically from registration forms.
#
# Usage:
#     python3 clean-csv.py
#
# Requirements:
#   1. Ensure target .csv file is utf-8 encoded.
#   2. Put this script in a directory with your target .csv file.
#   3. Rename the target file to 'input.csv'.
#   4. Open a terminal in the same directory and execute: python3 clean-csv.py
#
# If successful a cleaned output.csv file will be generated.

import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header
        header = next(reader)
        writer.writerow(header)

        # Process rows, customise processing as required.
        for row in reader:
            # "Email Address": convert to lower case
            row[0] = row[0].lower()

            # "First Name": convert to lower case, then capitalize each word
            row[1] = row[1].lower().title()

            # "Last Name": convert to lower case, then capitalize each word
            row[2] = row[2].lower().title()

            # "Address": Trim white space
            row[3] = row[3].strip()

            # Write the cleaned row to the output file
            writer.writerow(row)

if __name__ == '__main__':
    input_file = 'input.csv'  # Replace with your input file name
    output_file = 'output.csv'  # Replace with your desired output file name
    clean_csv(input_file, output_file)
