#! /usr/bin/python
#
#  USGS Preliminary Computer Program: shp2n3.py
#  Written by: Eric B. Wolf
#  Written in: Python 2.6 + GDAL/OGR 1.6
#  Program ran on: Windows XP SP3
#
#  DISCLAIMER: Although this program has been used by the USGS, no warranty, 
#  expressed or implied, is made by the USGS or the United States Government 
#  as to the accuracy and functioning of the program and related program 
#  material nor shall the fact of distribution constitute any such warranty, 
#  and no responsibility is assumed by the USGS in connection therewith.
#
#  Uses OGR to open an ESRI Shapefile.
#  Attributes are encoded as literals relying on the types from the table.
#  Shape geometry is stored as hasGeometry: <GML>
#
#  Actual output to N3 format is encapsulated in n3class.py
#

from osgeo import ogr
from osgeo import gdal

import sys
import string

from n3class import N3

def help_message():
    print "shp2n3.py -- Convert ESRI Shapefile to n3 notation"
    print "             Always generates schema\n"
    print "   Usage: shp2n3.py infile.shp outfile.n3\n"
    sys.exit(0)

# Main function


try:
    infile = sys.argv[1];
    outfile = sys.argv[2];
except:
    help_message()

try:
    driver = ogr.GetDriverByName('ESRI Shapefile')
except:
    print "Error getting driver!"
    print 'Error:', gdal.GetLastErrorMsg()
    help_message();

try:
    inShp = ogr.Open(infile)
    inLyr = inShp.GetLayer(0)
    outFp = open(outfile, "w")
except:
    print "Error opening files!"
    print 'Error:', gdal.GetLastErrorMsg()
    help_message();

shpN3 = N3()
    
shpN3.write_headers(inLyr, outFp)
shpN3.write_triples(inLyr, outFp) 

inShp.Destroy()
outFp.close()
