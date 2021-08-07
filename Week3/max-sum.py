
NBAfile= open('NBA-attendance-1989.txt','r')
NBAList = []
for line in NBAfile:
     textline=line.strip()
     items = textline.split()
     NBAList.append(items)
attendances = []
for line in NBAList:
     attendances.append(int(line[1]))
att_sum = sum(attendances)
print ('Total Attendance was: ',att_sum)
average_att = sum(attendances) / len(attendances)
print ('Average Attendance was: ',average_att)
team, att, price = NBAList[0]
prices = []
for (team, att, price) in NBAList:
     prices.append(float(price))
avg_price = sum(prices) / len(prices)
print ('Average Ticket Price was: ',avg_price)
max_att = max(attendances)
max_price = max(prices)
teams = []
for (team, att, price) in NBAList:
     teams.append(team)
max_team=teams[attendances.index(max_att)]
max_team2 = teams[prices.index(max_price)]
print ('Team with greatest attendance was: ',max_team, 'Attendance of: ', max_att)
print ('Team with greatest price was: ',max_team2, 'Price of: ', max_price)
