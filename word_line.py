#importing libraries
import fileinput

#Start of function(This is case insensitvie function)
def word_line(filename, word):

        #Opening the file in Reading mode
        with open(filename, 'r') as file:

                #Reading file line by line
                for line in file:

                        #converting word and line in uppercase and searching word in line
                        if word.upper() in line.upper():
                                print(line)


#Enter file location, word you want to search
filename = input("Enter the filename/location: ")
word = input("Get all the line containing this word: ")

#Calling the function 
word_line(filename, word)

