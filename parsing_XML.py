#!/usr/bin/env python
# coding=utf-8

import os
import xml.etree.cElementTree as ET

def getBatchNameFromXml(XML_patch):

    try:
        tree = ET.parse(XML_patch)      # create an object witch "pars" file
        importSession = tree.getroot()      # getting the main branch
        batches = importSession.find('Batches')     # search in the attribute branch "Batches"
        batch = batches[0].attrib   # take the first name before the delimiter
        name = batch.get('Name')     # take the name
        return name

    except IOError as e:
        print(e)

path_to_programm = "home/Git/Python/TiffFromXML/Project/"
data_directory = "DATA"

path_to_XML = path_to_programm + data_directory + "/XML/"
files_list = os.listdir(path_to_XML)

all_batch_Names = []
for file in files_list:
    all_batch_Names.append(getBatchNameFromXml(path_to_XML + file))

print("/n".join(all_batch_Names))
