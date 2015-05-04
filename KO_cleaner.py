#!/usr/bin/env python
import sys

## Takes a KO file and removes all lines not assigned a K number
def line_cleaner(input):
    clean_list = "" # Initializes string of lines with a K number
    with open(input, "r") as file: # Opens the file for reading
        ## Check every line in file for tab or # characters and, if found, adds it to clean_list
        for line in file:
            if "\t" in line:
                clean_list += line
            elif "#" in line:
                clean_list += line
    ## Writes the clean_list to a new file
    with open(outname, "w") as outfile:
        outfile.write(clean_list)

## Changes filename from "X.ko" to "X_cleaned.ko"
outname = sys.argv[1]
outname = outname[:-3] + "_cleaned.ko"

if __name__ == '__main__':
    line_cleaner(sys.argv[1])
