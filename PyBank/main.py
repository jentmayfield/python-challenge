# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')
row_cnt = -1  # Would normally start at 0, but because of header, we start at -1
net_prof_loss = 0
prev_value=0
diff = 0
tot_diff = 0.00
max_inc = 0
min_inc = 0



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # rows = []
    for row in csvreader:
        row_cnt += 1
        if row_cnt >= 1:
            
            net_prof_loss = net_prof_loss + int(row[1])
            diff=int(row[1])-prev_value
            row.append(diff)
            prev_value = int(row[1])
            tot_diff = tot_diff + int(row[2])
            if max_inc < int(row[2]):
                max_inc = int(row[2])
                max_month = row[0]
            if min_inc > int(row[2]):
                min_inc = int(row[2])
                min_month = row[0]
            
        print(row)
        
# for i, row in enumerate(csvreader):
#     f_idx = header.index('Date')
#     print(f_idx)
print('Financial Analysis')
print('--------------------------------')
print('Total Months: ' + str(row_cnt))
print('Total: ' + str('${:,.2f}'.format(net_prof_loss)))    
print('Average Change: ' + str('${:,.2f}'.format((tot_diff-867884) / (row_cnt-1))))
print('Greatest Increase in Profits: ' +  max_month + ' '  + str(max_inc))
print('Greatest Decrease in Profits: ' + min_month + ' '  + str(min_inc))


output_file = os.path.join("Final_PyBank.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)


#    writer.writerow(['Financial Analysis'])
    writer.writerow(['Financial Analysis'])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Total Months: ' + str(row_cnt)])
    writer.writerow(['Total: ' + str('${:,.2f}'.format(net_prof_loss))])    
    writer.writerow(['Average Change: ' + str('${:,.2f}'.format((tot_diff-867884) / (row_cnt-1)))])
    writer.writerow(['Greatest Increase in Profits: ' +  max_month + ' '  + str(max_inc)])
    writer.writerow(['Greatest Decrease in Profits: ' + min_month + ' '  + str(min_inc)])

#print(avg_change)
#   NOT CORRECT, WHAT IS IT WANTING?




#for row in csvreader:
#    print(len(row()))
  

#def average(numbers):
#    length = len(numbers)
#    total = 0.0
#    for number in numbers:
#        total += number
#    return total / length


# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))

# Functions can return a value
#def square(number):
#    return number * number


# You can save the value that is returned
#squared = square(2)
#print(squared)

# You can also just print the return value of a function
#print(square(2))
#print(square(3))



# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

