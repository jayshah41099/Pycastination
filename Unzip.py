from zipfile import ZipFile
import sys

zip = sys.argv[1]
with ZipFile (zip, 'r') as zip_object:
    zip_object.extractall()

print (zip_object.namelist())