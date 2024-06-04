from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os


class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Registration Window")
        self.root.config(bg="white")
        
#======================Registration Images===================#

        self.left=ImageTk.PhotoImage(file="images/register_new.png") 
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=400)        

#=========================register-frame========================#
            
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=30)


    #=================row-1======================#  
        self.var_fname=StringVar()
        fname=Label(frame1,text="Full Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=70)
        self.txt_fname=Entry(frame1,font=("times new romnan",15),bg="lightgray",textvariable=self.var_fname)
        self.txt_fname.place(x=50,y=95,width=250)

        email=Label(frame1,text="E Mail",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=70)
        self.txt_email=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_email.place(x=350,y=95,width=240)
        

    #=================row-2======================#
        gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=120)
        self.txt_gender=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_gender.place(x=50,y=145,width=240)
        
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=120)
        self.txt_contact=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_contact.place(x=350,y=145,width=250)
        
        
#==========================Row 3=================#
        dob=Label(frame1,text="D-O-B in DD-MM-YYYY",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_dob=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_dob.place(x=50,y=195,width=240)
        
        doj=Label(frame1,text="D-O-J in DD-MM-YYYY",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=170)
        self.txt_doj=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_doj.place(x=350,y=195,width=240)


#=================row-4======================#
        password=Label(frame1,text="Enter Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=220)
        self.txt_password=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_password.place(x=50,y=245,width=245)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=220)
        self.txt_cpassword=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_cpassword.place(x=350,y=245,width=245)
        
#=================row-4======================#
        utype=Label(frame1,text="Enter user: Employee",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=270)
        self.txt_utype=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_utype.place(x=50,y=295,width=245)

        Address=Label(frame1,text="Enter Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=270)
        self.txt_address=Entry(frame1,font=("times new romnan",15),bg="lightgray")
        self.txt_address.place(x=350,y=295,width=245)
        
#====================terms&conditions=======================#

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree with Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=330)


        self.btn_img=ImageTk.PhotoImage(file="images/register_button_new (1).png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=360)


        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2").place(x=230,y=390,width=100)


    def register_data(self):
            if self.txt_fname.get()=="" or self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)

            elif self.txt_password.get()!= self.txt_cpassword.get():
                messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)

            elif self.var_chk.get()==0:
                messagebox.showinfo("Error","Please Agree to our Terms & Conditions",parent=self.root)  

            else:
                try:
                    con=sqlite3.connect(database="ims.db")
                    cur=con.cursor()
                    cur.execute("insert into employee (name, email, gender, contact, dob, doj, pass, utype, address) values (?,?,?,?,?,?,?,?,?)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_email.get(),
                                    self.txt_gender.get(),
                                    self.txt_contact.get(),
                                    self.txt_dob.get(),
                                    self.txt_doj.get(),
                                    self.txt_password.get(),
                                    self.txt_utype.get(),
                                    self.txt_address.get()
                            
                                ))
                    con.commit()
                    con.close()    
                    messagebox.showinfo("Success","Registration Sucessful")    
                    
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
                     


        


root=Tk()
obj=Register(root)
root.mainloop()