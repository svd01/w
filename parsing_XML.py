#!/usr/bin/env python
# coding=utf-8

import os
import xml.etree.cElementTree as ET

def getBatchNameFromXml(XML_patch):
    """
        <ImportSession>
            <?xml version="1.0" encoding="UTF-8"?>
            <Batches>
                <Batch Name="2016-05012 12-09-12-675 (12:10:43.661)" Description="" Priority="4" BatchClassName="AlphaInsurance">
        """
    try:
        tree = ET.parse(XML_patch)
        importSession = tree.getroot()
        batches = importSession.find('Batches')
        batch = batches[0].attrib
        name = batch.get('Name')
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
