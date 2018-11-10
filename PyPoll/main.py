# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('election_data.csv')

# LIsts to store data
voter_id =[]
county = []
candidate = []
row_cnt = -1
cnt_khan = 0
cnt_correy = 0
cnt_li = 0
cnt_otooley = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        row_cnt += 1
        if row[2] == 'Khan':
            cnt_khan += 1
        if row[2] == 'Correy':
            cnt_correy += 1
        if row[2] == 'Li':
            cnt_li += 1
        if row[2] == "O'Tooley":
            cnt_otooley += 1

per_kahn = (cnt_khan / row_cnt * 100)
per_correy = (cnt_correy / row_cnt * 100)
per_li = (cnt_li / row_cnt * 100)
per_otooley = (cnt_otooley / row_cnt * 100)



data = [['Khan',cnt_khan],['Correy',cnt_correy],['Li',cnt_li],["O'Tooley",cnt_otooley]]
var_winner = max(data, key=lambda item: item[1])


print('Election Results')
print('---------------------------')
print('Total Votes: ' + str(row_cnt))
print('---------------------------')
print('Khan: ' + (str('{:,.3f}'.format(per_kahn) + "% " +'(' + str(cnt_khan) + ')')))
print('Correy: ' + (str('{:,.3f}'.format(per_correy) + "% " + '('+ str(cnt_correy) + ')')))
print('Li: ' + (str('{:,.3f}'.format(per_li) + "% " +'(' + str(cnt_li) + ')')))
print("O'Tooley: " + (str('{:,.3f}'.format(per_otooley) + "% " + "(" + str(cnt_otooley) + ')')))
print('---------------------------')
print('Winner: ' + var_winner[0])
print('---------------------------')

output_file = os.path.join("Final_PyPoll.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

#    writer.writerow(['Election Results'])
    writer.writerow(['Election Results'])
    writer.writerow(['---------------------------'])
    writer.writerow(['Total Votes: ' + str(row_cnt)])
    writer.writerow(['---------------------------'])
    writer.writerow(['Khan: ' + (str('{:,.3f}'.format(per_kahn) + "% " +'(' + str(cnt_khan) + ')'))])
    writer.writerow(['Correy: ' + (str('{:,.3f}'.format(per_correy) + "% " + '('+ str(cnt_correy) + ')'))])
    writer.writerow(['Li: ' + (str('{:,.3f}'.format(per_li) + "% " +'(' + str(cnt_li) + ')'))])
    writer.writerow(["O'Tooley: " + (str('{:,.3f}'.format(per_otooley) + "% " + "(" + str(cnt_otooley) + ')'))])
    writer.writerow(['---------------------------'])
    writer.writerow(['Winner: ' + var_winner[0]])
    writer.writerow(['---------------------------'])