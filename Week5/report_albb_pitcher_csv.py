'''
  This program reads the American League baseball players, 2003, tsv file
    using the csv reader 
    and stores it in a list of dictionaries, one for each player
  Each line has the team, the player name, the salary and the position played.

  The program writes a report on the average salary per player to a txt file.
  The program writes the players who made more than $10 million to a csv file
    using the csv writer with a header line suitable for excel.
'''

import csv

infile = 'ALbb.salaries.2003.tsv'

# create new empty list
playersList = []

with open(infile, 'rU') as csvfile:
    # the csv file reader returns a list of the csv items on each line
    ALReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')

    # from each line, a list of row items, put each element in a dictionary
    #   with a key representing the data
    for line in ALReader:
      # skip lines without data
      if line[0] == '' or line[0].startswith('American') or line[0].startswith('Team')\
            or line[0].startswith('Source'):
          continue
      else:
          try:
            # create a dictionary for each player
            player = {}
            # add each piece of data under a key representing that data
            player['team'] = line[0]
            player['name'] = line[1]
            player['sal'] = int(line[2].replace(',',''))
            player['position'] = line[3]
    
            # add this player to the list
            playersList.append(player)
    
          except IndexError:
            print ('Error: ', line)
csvfile.close()

print ("Read", len(playersList), "player data")


# Write a report text file with a title and the average of the salaries
# First create an output file name
outfile1 = infile.replace('tsv', '') + 'report.txt'
# open the file for writing
fout1 = open(outfile1, 'w')

# Write a file with all the players who were pitchers.
# We write a comma separated file, using the csv writer to quote the player names with commas
# first create an output file name
outfile2 = infile.replace('tsv','') + 'Pitchers.csv'

# open the file
with open(outfile2, 'w', newline='') as csvfileout:
    # create a csv writer for a comma sep file, with quoting as needed
    ALwriter = csv.writer(csvfileout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    # write the header row as a list of column labels
    ALwriter.writerow(['Player', 'Team', 'Position', 'Salary'])
    for player in playersList:
        # select the players with salary over 1 million
        if (player['position'] == 'Pitcher'):
            # write the player as a list of data items
            ALwriter.writerow([player['name'], player['team'], player['position'], player['sal']])

csvfileout.close()



