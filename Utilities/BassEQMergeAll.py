# BassEQMergeAll.py
# By Matt King
#
# Script that merges your miniDSP room correction config with BassEQs
# Ensure all input PEQ gains are set to 0 in your room correction
# Usage: python BassEQMergeAll.py <path to base config XML>

import xml.etree.ElementTree as ET
import glob
import sys

inputFilterNames = [
    'PEQ_1_',
    'PEQ_2_',
]

if len(sys.argv) < 2:
    print 'Usage: %s <base config xml path>' % sys.argv[0]

# Load the xmls
print "Reading in XMLs..."
trees = []
files = []
for f in glob.glob('*.xml'):
    trees.append(ET.parse(f))
    files.append(f)

# Load base config
baseConfigTree = ET.parse(sys.argv[1])
baseConfig = baseConfigTree.getroot()

print "Modifying BassEQ XMLs with your base config..."
for tree in trees:
    peqs = {}
    eqConfig = tree.getroot()
    # Iterate through the input PEQs for BassEQ and store them
    for child in eqConfig.iter('filter'):
        if any(x in child.attrib['name'] for x in inputFilterNames):
            peqs[child.attrib['name']] = {}
            for subchild in child:
                peqs[child.attrib['name']][subchild.tag] = subchild.text

    # Now overwrite the input PEQs in the base config
    for child in baseConfig.iter('filter'):
        if any(x in child.attrib['name'] for x in inputFilterNames):
            for subchild in child:
                subchild.text = peqs[child.attrib['name']][subchild.tag]

    # And write out the file!
    baseConfigTree.write(files[trees.index(tree)])

print "Done!!"
