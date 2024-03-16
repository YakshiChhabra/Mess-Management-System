from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

def autroization():
    username=string1.get()
    password=string2.get()
    if username=="Akhil" and password=="Akhil@123":
    
        messagebox.showinfo("Authorization Section","Access Authorize")
        os.system(r"cd C:\Users\saini\Downloads\Mess-Management-main")
        
    elif username=="Himanshu" and password=="Himanshu@123":
        messagebox.showinfo("Authorization Section","Access Authorize") 
        os.system(r"C:\Users\saini\Downloads\Mess-Management-main")
       
    elif username=="Yakshi" and password=="Yakshi@123":
        messagebox.showinfo("Authorization Section","Access Authorize")
        os.system(r"C:\Users\saini\Downloads\Mess-Management-main")
        
    elif username=="Nitesh" and password=="Nitesh@123":
        messagebox.showinfo("Authorization Section","Access Authorize") 
        os.system(r"C:\Users\saini\Downloads\Mess-Management-main")
       
    else:
        messagebox.showwarning("Authorization Section","Unauthorization to System")
        messagebox.showinfo("Authorization Section","Enter Correct Username or Password")


















root=Tk()



root.geometry("1800x1800")

root.title("Mess Managment system")
string1=StringVar()
string2=StringVar()
bg = PhotoImage(file = r"C:\Users\saini\Downloads\jpg2png (2)\himansu12.png")
canvas1 = Canvas( root, width = 1200, height = 1200) 
  
canvas1.pack(side=TOP,expand=True,fill=tk.Y) 
  
# Display image 
canvas1.create_image( 10,10, image = bg,  anchor = "nw") 


label=Label(root,text=" M.D.U Mess Managment  System",font=(("", 30,"bold", )),bg="gray", fg="white").place(x=470,y=120)
label=Label(root,text="Authorization section",font=("Times New Roman TUR", 30, "bold"),bg="gray",fg="white" ).place(x=570,y=220)
label2=Label(root,text="Enter your name :",bg="Black",font=("Times New Roman TUR", 16, "bold"),fg="white").place(x=550,y=390)
label3=Entry(root,width=45,bg="black",textvariable=string1,fg="white").place(x=900,y=390)
label4=Label(root,text="Enter your password :",bg="black" , font=("Times New Roman TUR", 16, "bold"),fg="white").place(x=560,y=490)
label5=Entry(root,textvariable=string2,width=45,bg="black",fg="white").place(x=900,y=490)
button1=Button(root,text="Submit",bg="black",command=autroization,cursor="hand2",width=17,fg="white",font=("Times New Roman TUR", 12, "bold")).place(x=650,y=570)
button2=Button(root,text="Quit",bg="black",command=quit,cursor="hand2",width=17,fg="white",font=("Times New Roman TUR", 12, "bold")).place(x=900,y=570)


root.mainloop()