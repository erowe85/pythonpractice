#! python3
#counts the amount of  cases each attorney has with a paralegal

import openpyxl, glob

#list of all the actual attorneys to filter out non-attorneys
lawyers = ['Cory Britt','Henry Acciani','Kory Veletean','Bobby Acciani','Matthew Nakajima','Dennis Mahoney','Anna Hines','Elizabeth Acciani','Barry Levy']

#open the workbook and select the sheet
    #glob finds a file with that name and anything following the word 'list
wbName = glob.glob('Weekly PI Project List*.xlsx')
#open the first file that appeared in the wbName list
wb = openpyxl.load_workbook(wbName[0])
sheet = wb.get_sheet_by_name('Sheet1')

attorneyCounts = {}

#go through sheet and count cases by paralegal for each attorney then add to a dictionary

for row in range(2, sheet.max_row+1):
    atty = sheet['C' + str(row)].value
    para = sheet['F' + str(row)].value
    

    #make sure the key in the attorney exists
    attorneyCounts.setdefault(atty,{})
    #make sure the key for the paralegal exists
    attorneyCounts[atty].setdefault(para , 0)

    #for each paralegal add 1 incrementally
    attorneyCounts[atty][para] += 1


    
resultFile = open('Case Counts.txt','w')

#show the results for each attorney
attycase = 0
for attys in attorneyCounts:
    #exclude Primaries not in the attorney list 'lawyers'
    if attys in lawyers:
        attycase = 0
        resultFile.write(attys + '\n')
        for paras in attorneyCounts[attys]:
            justifypara = str(paras)
            #format the paralegal case count to look pretty
            resultFile.write('     '+f'{justifypara: <20}' + '          ' + str(attorneyCounts[attys][paras])+ '\n')
            attycase = attorneyCounts[attys][paras] + attycase
        justifyatty = str(attycase)
        #format the total line to look pretty
        resultFile.write('\n Total cases for Attorney: ' + f'{justifyatty: >10}'+ '\n \n')

resultFile.close()
