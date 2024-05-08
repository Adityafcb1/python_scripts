#import glob to search for files that match a specific file pattern or name.
#import os for file manipulation
#import shutil to perform operation on files

import glob
import os
import shutil

def rmfile(filename):
        #searching all files that matches pattern
        for file_path in glob.glob(filename):

                #if its file directly delete 
                if os.path.isfile(file_path):
                        os.remove(file_path)
                
                #if its folder delete subfolders and files inside it
                else:
                        shutil.rmtree(file_path)

#enter the file or file location you want to delete
filename = input("Enter the filename/location: \n")

#calling the function to remove the file or folder
a = rmfile(filename)
