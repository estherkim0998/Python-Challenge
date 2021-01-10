#!/usr/bin/env python
# coding: utf-8

# In[8]:


# PyBank 
# Dependencies 
import csv 
import os 
# Files to load and output
file_to_load = os.path.join(".","Resources","budget_data.csv")
file_to_output = os.path.join(".","Analysis","budget_analysis.txt")
# track various financial parameters
total_months = 0 
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease= ["",9999999999999]
total_net = 0 
with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)
        header = next(reader)
        #print(header)
        
        #Extract first row to avoid appending to net_change list 
        first_row = next(reader)
        #print(first_row)
        total_months = total_months + 1
        #print(first_row[1])
        total_net = total_net + int(first_row[1])
        prev_net = int(first_row[1])
        #print(prev_net)
       #print(first_row[1])
    
    #loop through your data
        for row in reader:
            #Track the total 
            total_months = total_months + 1
            total_net = total_net + int(row[1])
            #print(total_net)
            
            #Trakc the net change
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list = net_change_list + [net_change]
            month_of_change = month_of_change + [row[0]]
            #print(net_change_list)
            #print(month_of_change)
            
            if net_change> greatest_increase[1]:
                    greatest_increase[0] = row[0]
                    greatest_increase[1] = net_change
            if net_change< greatest_decrease[1]:
                    greatest_decrease[0] = row[0]
                    greatest_decrease[1] = net_change
            
        net_monthly_avg = sum(net_change_list)/len(net_change_list)
        
        output = (f"\nFinancial Analysis\n"
                  f"====================\n"
                  f"Total Months: {total_months}\n"
                  f"Total: ${total_net}\n"
                  f"Average Change: ${net_monthly_avg:.2f}\n"
                  f"Greatest Increase in Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
                  f"Greatest Decrease in Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n")
        print(output)
with open(file_to_output,"w") as txt_file:
        txt_file.write(output)
            


# In[ ]:




