import tkinter
'''
CREATE A SIMPLE REGISTRATION FORM USING TKINKER USING PLACE() GEOMETRY
NAME
EMAIL
PHONE NUMBER
COMMENT(MULTI-LINE INPUT)

ADD A CLICKABLE BUTTON

ADD A BACKGROUND COLOR AND ANOTHER FEATURE OF CHOICE.
'''

screen = tkinter.Tk()
screen.title('REGISTRARTION FORM')
screen.configure(bg = 'green')
screen.geometry('600x400')

lab = tkinter.Label(screen, text = 'WELCOME TO REGISTRATION FORM', bg = 'white', fg = 'blue').pack()
name = tkinter.Label(text='Name', bg='white').place(x = 30, y = 40)
name_txt = tkinter.Entry().place(x=80, y=40)

email = tkinter.Label(text='Email', bg='white').place(x = 30, y = 70)
email_txt = tkinter.Entry().place(x=80, y=70)

phone_number = tkinter.Label(text='Phone Number').place(x=30, y=95)
phone = tkinter.Entry().place(x=120, y=95)

comment = tkinter.Label(text='Comment').place(x=30, y=120)
comment_txt = tkinter.Entry().place(width=90, height=110, x=110, y=120)

bt= tkinter.Button(text='SUBMIT',bg='blue').place(x= 30, y=150)

screen.mainloop()