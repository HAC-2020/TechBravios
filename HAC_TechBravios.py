# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:47:52 2020

@author: Geet Patel
"""

import tkinter

root=tkinter.Tk()

    # set the background colour of GUI window
root.configure(background='light green')
 
    # set the title of GUI window
root.title("registration form")
 
    # set the configuration of GUI window
root.geometry("500x300")
 
    #excel()♣

    # create a Form label
heading = tkinter.Label(root, text="Hospital name", bg="light green")
 
    # create a Name label
name = tkinter.Label(root, text="seat name", bg="light green")
 
    # create a Course label
course = tkinter.Label(root, text="add.", bg="light green")
 
    # create a Semester label
sem = tkinter.Label(root, text="ph. number", bg="light green")
 
    # create a Form No. lable
form_no = tkinter.Label(root, text="email", bg="light green")
 
en1=tkinter.Entry(root)
en2=tkinter.Entry(root)
en3=tkinter.Entry(root)
en4=tkinter.Entry(root)
en5=tkinter.Entry(root)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
heading.grid(row=0, column=0)
name.grid(row=1, column=0)
course.grid(row=2, column=0)
sem.grid(row=3, column=0)
form_no.grid(row=4, column=0)
#
en1.grid(row=0, column=2)
en2.grid(row=1, column=2)
en3.grid(row=2, column=2)
en4.grid(row=3, column=2)
en5.grid(row=4, column=2)

 
    # create a text entry box
    # for typing the information
name_field = tkinter.Entry(root)
course_field = tkinter.Entry(root)
sem_field = tkinter.Entry(root)
form_no_field = tkinter.Entry(root)


root.mainloop()