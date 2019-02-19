# BassEQMergeAll.py

This is a script that will allow you to quickly merge your miniDSP room correction settings into all of the
BassEQ XMLs in a folder.

## BassEQMergeAll.py Instructions

For this example, we will merge all of the Movie XMLs with the base configuration.

1. Acquire Python for your platform
2. In miniDSP, ensure that all input PEQ gains are set to 0
3. Click File->Save->Save current configuration
4. In a terminal or console, cd into the 'Movie BEQs' folder
5. Run: `python ../Utilities/BassEQMergeAll.py <path to base config XML>`
6. After several seconds (can sometimes take a bit), it should finish merging all the XMLs.
7. Load a BassEQ XML into miniDSP and ensure that your room correction is there, as well as the input PEQs.
8. Repeat for the 'TV Shows BEQ' folder, if desired.
