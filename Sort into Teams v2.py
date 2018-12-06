#! python3
# get list of employees from excel list and sort them into teams randomly
#requires an excel list of players named 'Employees.xlsx' run from same directory as script

import openpyxl, random

#open the workbook and select the sheet
wb = openpyxl.load_workbook('Employees.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')


#create a dictionary of each employee with an empty team
teamsList = {}
teamCount = 0
for row in range(2,sheet.max_row + 1):
    name = sheet['A'+ str(row)].value
    #set the defaul team as 0
    teamsList.setdefault(name, 0)
    #count the amount of people
    teamCount = teamCount + 1

#show how many players are in the dictionary
print('The total number of players is ' + str(teamCount))

#request team information
teamNo = int(input('How many teams?: '))
print('The number of players per team would even out to ' + str(teamCount/teamNo))
teamPlayers = int(input('How many players per team?: '))

#create a dictionary of teams
teams = {}
for number in range(1, teamNo +1):
    teams.setdefault(str(number),0)



#function to randomly assign players to teams
def randomlySort():
    for i in teamsList:
        #if there are no available keys then assign player to team 0
        teamsCount = 0
        for players in teams:
            teamsCount = teamsCount + teams[players]
        if teamsCount == teamNo * teamPlayers:
            teamsList[i] = 0
        else:
            #random variable
            r = random.randint(1,len(teams))
            #if there's fewer than teamPlayers on a team, assign person to that team
            if teams[str(r)] <= teamPlayers -1:
                teamsList[i] = r
                teams[str(r)] = teams[str(r)]+1
            #if there are more than teamPlayers on the team, regenerate a random key
            #until you get a team with less than 8 players
            elif teams[str(r)] > teamPlayers:
                for z in teams:
                    r = random.randint(1,len(teams))
                    if teams[str(r)]<=teamPlayers:
                        teamsList[i] = r
                        teams[str(r)] = teams[str(r)]+1
                            

def cleanupSort ():
    #find players not assigned to a team and distribute them randomly
    for i in teamsList:
        if teamsList[i] == 0:
            while True:
                r = random.randint(1,len(teams))
                #find under-strength team and boost them
                if teams[str(r)] <= teamPlayers -1:
                    teamsList[i] = r
                    teams[str(r)] = teams[str(r)]+1
                    break

randomlySort()
cleanupSort()

#print the names of the teams sorted by their keys
resultFile = open('Teams.txt','w')

sort = 1
sortCount = 0
sortTotal = 0
for x in teamsList:
    if sort <= len(teams):
        resultFile.write('Team ' + str(sort)+'\n')
        for y in teamsList:
              if teamsList[y] == sort:
                  resultFile.write('     ' + str(y)+ '\n')
                  sortCount = sortCount + 1
                  sortTotal = sortTotal + 1
        sort = sort + 1
        if sortCount > 0:
            noPlayers = str(sortCount)
        else:
            noPlayers = 'No Players'
        resultFile.write('\n Team Count = ' + noPlayers+ '\n \n')
        sortCount = 0
resultFile.write('Total Players: ' + str(sortTotal))    
resultFile.close()
              
    


