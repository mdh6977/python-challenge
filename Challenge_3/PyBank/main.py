#!/usr/bin/env python
# coding: utf-8

# In[53]:


import os
import csv
from pathlib import Path


# In[54]:


filepath = Path("Desktop/Challenge_3/PyBank/Resources/budget_data.csv")


# In[55]:


total_months = []
total_profit = []
monthly_profit_change = []


# In[56]:


with open(filepath,newline="", encoding="utf-8") as budget:

    
    csvreader = csv.reader(budget,delimiter=",") 

   
    header = next(csvreader)  

    
    for row in csvreader: 

        
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    
    for i in range(len(total_profit)-1):
        
        
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])


# In[57]:


max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


# In[58]:


max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


# In[59]:


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# In[60]:


output_file = Path("Desktop/Challenge_3/PyBank/Resources/Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# In[ ]:




