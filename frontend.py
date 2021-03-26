from tkinter import *
import backend

def getSelectedRow(event):
    try:
        global selectedTuple
        index=list1.curselection()[0]
        selectedTuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selectedTuple[1])
        e2.delete(0,END)
        e2.insert(END, selectedTuple[2])
        e3.delete(0,END)
        e3.insert(END, selectedTuple[3])
        e4.delete(0,END)
        e4.insert(END, selectedTuple[4])
    except IndexError:
        pass
    

def viewCommand():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def searchCommand():
    list1.delete(0, END)
    for row in backend.search(title_text.get(),author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row) 

def insertCommand():
    backend.insert(title_text.get(),author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(),author_text.get(), year_text.get(), isbn_text.get()))

def deleteCommand():
    backend.delete(selectedTuple[0])

def updateCommand():
    backend.update(selectedTuple[0],title_text.get(),author_text.get(), year_text.get(), isbn_text.get())
    

window = Tk()

window.wm_title("Book application")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)
l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)
l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)
l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row = 0, column = 1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row = 0, column = 3)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row = 1, column = 1)
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 8, width = 35)
list1.grid(row =2, column = 0, rowspan =8, columnspan = 2)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', getSelectedRow)

b1 = Button(window, text = "View All", width = 12, command = viewCommand)
b1.grid(row = 2, column = 3)
b2 = Button(window, text = "Search Entry", width = 12, command = searchCommand)
b2.grid(row = 3, column = 3)
b3 = Button(window, text = "Add Entry", width = 12, command = insertCommand)
b3.grid(row = 4, column = 3)
b4 = Button(window, text = "Update", width = 12, command = updateCommand)
b4.grid(row = 5, column = 3)
b5 = Button(window, text = "Delete", width = 12, command = deleteCommand)
b5.grid(row = 6, column = 3)
b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()

