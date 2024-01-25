# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 05:33:39 2024

@author: Eshaan Gurjar
"""

from tkinter import *

root = Tk()
root.title("Sales Report")
root.geometry("500x700")



months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000, 45000, 778000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

month_label = Label(root, text = months)
profits_label = Label(root, text = profits)

year_summary_min = Label(root)
year_summary_max = Label(root)

def find():
    min_profits = min(profits)
    max_profits = max(profits)
    
    min_profits_index = profits.index(min_profits)  
    max_profits_index = profits.index(max_profits)
    
    min_profits_month = months[min_profits_index]
    max_profits_month = months[max_profits_index]
    
    year_summary_min["text"] = "The minimum earnings of " + str(min_profits) + " was earned in the month of " + str(min_profits_month)
    year_summary_max["text"] = "The maximum earnings of " + str(max_profits) + " was earned in the month of " + str(max_profits_month)
    
btn = Button(root, text = "Show Summary", command = find)

month_label.pack()
profits_label.pack()
btn.pack()
year_summary_min.pack()
year_summary_max.pack()

root.mainloop()