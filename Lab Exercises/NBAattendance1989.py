# Name of file  : NBAattendance1989.py
# Date Created: July 7, 2020
# Created by: Sathish Rajendiran
# Purpose of Program: To read from file

#
#

# open the file for reading (in the same directory as the program)
NBAfile = open ('NBA-Attendance-1989.txt', 'r')

# create a dummy list
NBAlist = [ ]

for line in NBAfile:
    # strip the newline at the end of the line (and other white space from ends)
    textline = line.strip()
    # split the line on whitespace
    items = textline.split()
    # add the list of items to the NBAlist
    NBAlist.append(items)

# print the lines from the list

for line in NBAlist:
    print('Line:', line)

NBAfile.close()
