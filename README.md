cleancsv
--------

A script to clean up user input in .csv files, such as from registration forms.

Usage:
     python3 clean-csv.py

Requirements:
   1. Ensure target .csv file is utf-8 encoded.
   2. Put this script in a directory with your target .csv file.
   3. Rename the target file to 'input.csv'.
   4. CUSTOMISE THE COLUMN NAMES AND PROCESSING TO MATCH YOUR OWN FILE STRUCTURE / REQUIREMENTS.
   5. Open a terminal in the same directory and execute: python3 clean-csv.py

On success a cleaned output.csv file will be generated.

Customisation:
    Edit the loop that processes rows and add whatever processing rules you want to apply.