import tkinter

screen = tkinter.Tk()
screen.title('BIO-DATA')
screen.configure(bg = 'pink')
screen.geometry('500x300')

lab = tkinter.Label(screen, text = 'WELCOME TO PYTHON ADVANCED', fg = 'blue').pack()
name = tkinter.Label(text = 'Name', bg = 'purple').place(x =30,y=50)
email = tkinter.Label(text = 'Email').place(x = 30, y = 90)

bt = tkinter.Button(text='Click Here').place(x = 80, y = 110)

name_txt = tkinter.Entry().place(x=80, y=50)
email_txt = tkinter.Entry().place(x = 80, y = 90)

screen.mainloop()