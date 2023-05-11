#Tanner Cole
#05/01/2023
#M07 Final Project
""" Creating a new patient sign up form for an optometry office,
this form will aks for name,email,phone number, and various other information
from the patient."""

#import tkinter
from tkinter import *
from tkinter import messagebox

#creating framework
root = Tk()
root.geometry("500x500")
root.title('Vision Care Patient Registration')

#Widget label creation for Header
label_1 = Label(root,text="Vision Care Registration", width=20,font=("bold" ,20))
#Column and row placement for header
label_1.place(x=90, y=60)

#Name Label
label_2 =Label(root,text="Enter Name", width=20,font=("bold" ,10))
label_2.place(x=80,y=130)
entry_2=Entry(root)
entry_2.place(x=240,y=130)

#Email Label
label_3 =Label(root, text="Enter email", width=20,font=("bold" ,10))
label_3.place(x=68,y=180)
entry_3=Entry(root)
entry_3.place(x=240,y=180)

#Phone Number Input
label_4 =Label(root, text="Enter Phone Number", width=20,font=("bold" ,10))
label_4.place(x=70,y=230)
entry_4=Entry(root)
entry_4.place(x=235,y=230)

#Gender Selection Tool
label_5=Label(root,text = "Prefered Gender",width=20,font=("bold",11))
label_5.place(x=70,y=280)
list_of_gender=['Male' ,'Female' ,'Non-Binary', 'Prefer not to say']
cv = StringVar()
drplist = OptionMenu(root,cv,*list_of_gender)
drplist.config(width=15)
cv.set('Prefered Gender')
drplist.place(x=240,y=280)

#Prefered Appointment Selection Tool
label_6=Label(root,text = "Appointment Time",width=20,font=("bold",11))
label_6.place(x=75,y=330)
list_of_time=['Morning' ,'Mid-Afternoon', 'Late-Afternoon', 'Evening']
cv = StringVar()
drplist = OptionMenu(root,cv,*list_of_time)
drplist.config(width=20)
cv.set('Appointment Time')
drplist.place(x=230,y=330)

#Insurance Radio Tool
label_7=Label(root,text="Using Insurance",width=20,font=('bold',10))
label_7.place(x=80, y= 380)
vars1=IntVar()
Checkbutton(root,text="Yes", variable = vars1).place(x=280,y=380)
vars2=IntVar()
Checkbutton(root,text="No", variable = vars2).place(x=340,y=380)

#Subimssion button
class NewWindow(Toplevel):
    def __init__(self, root = None):

        super().__init__(root = root)
        self.title("Submission Confirmation")
        self.geometry("500x500")
        label_8=Label(self, text = "Thank you for registering.")
        label_8.pack()
        btn = Button(self, text = "Exit", width=20,bg="red",fg='white', command = self.destroy).place(x=180, y=430)

btn =  Button(root,text='Submit', width=20,bg="green",fg='white', command = NewWindow).place(x=180,y=430)

#exit button
exit_button = Button(root,text='Exit', width=20,bg="red",fg='white', command = root.destroy).place(x=180, y=460)
#Call the mainloop and execute the entire program
root.mainloop()
