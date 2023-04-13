# #To zip all the contents of a directory in a zip archive, 
# # we need to iterate over all the files in directory and it’s sub directories, 
# # then add each entry to the zip file using ZipFile.write()
# from zipfile import ZipFile
# import os
# from os.path import basename
# # create a ZipFile object
# with ZipFile('sampleDir.zip', 'w') as zipObj:
#    # Iterate over all the files in directory
#    for folderName, subfolders, filenames in os.walk('C:\Users\stavt\Documents\file-organizer\DOCUMENTS'):
#        for filename in filenames:
#            #create complete filepath of file in directory
#            filePath = os.path.join(folderName, filename)
#            # Add file to zip
#            zipObj.write(filePath, basename(filePath))

from pathlib import Path


def zip_this_folder():
    print('zipme')