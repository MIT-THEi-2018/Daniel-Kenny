import pprint
import tkinter as tk
from tkinter import *
# name = input('Welcome ! What is your name? \nName: ')
# Age = input('Age: ')
# Birthday = input('Birth :')
# region = {
#     'Central and Western':['user_name1','user_name2'],
#     'Eastern':['user_name3','user_name4'],
#     'Southern':['user_name1','user_name2']
# }
# pprint.pprint(region)

# user_region = input('Which area you live? \nRegion: ')

# region[user_region] = region[user_region]+[name]

# pprint.pprint(region)



window = Tk()
 
window.title("Prototype")
 
window.geometry('300x500')
 
listb = Listbox(window)

region_list = ['Central and Western', 'Eastern','Southern']

for item in region_list:
    listb.insert(0,item)
listb.pack()  
listb.grid(column=0, row=0)
 
def clicked():
   
    region = {
    'Central and Western':['user_name1','user_name2'],
    'Eastern':['user_name3','user_name4','new_user_name'],
    'Southern':['user_name1','user_name2']
}
    
    listb.insert(0,user_region)

 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()

