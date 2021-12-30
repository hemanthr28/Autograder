#Script used to rename the folder names. You need to have a csv file with all the old folder names and new names. E.g. cell A1 - Old Folder name and cell B1 - New Fodler name
import os, unicodecsv as csv
# open and store the csv file
IDs = {}
with open('PID.csv','rb') as csvfile:
    timeReader = csv.reader(csvfile, delimiter = ',')
    # build dictionary with associated IDs
    for row in timeReader:
        IDs[row[0]] = row[1]
# move files
path = 'PATH'
gitname = os.listdir(path)
keys = list(IDs)
for names in keys:
    if (names not in gitname):
        try:
            os.mkdir(IDs[names])
        except FileExistsError:
            print('File present')

for oldname in os.listdir(path):
    # ignore files in path which aren't in the csv file
    if oldname in IDs:
        try:
            os.rename(os.path.join(path, oldname), os.path.join(path,(IDs[oldname])))
        except:
            print('File ' + oldname + ' could not be renamed to ' + IDs[oldname] + '!')
    