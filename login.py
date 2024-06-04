from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os



class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Logistic Management System | Developed By Group-4")
        self.root.geometry("1350x700+0+0")
        #self.config(bg="#fafafa")
        
        
        #==================images======================#
        self.phone_image=ImageTk.PhotoImage(file="images/login2.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
        
        
        #================================Login_ frame=====================#
        self.employee_id=StringVar()
        self.password=StringVar()
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=720,y=90,width=350,height=460)
         
        
        title=Label(login_frame,text="Login System",font=("goudy old style",30,"bold")).place(x=0,y=30,relwidth=1)
        
        
        
        lbl_user=Label(login_frame,text="Employee ID",font=("Elephnat",15),bg="white",fg="#767171").place(x=50,y=100)
        
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Elephnat",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=240)
        
        
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arian Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        #or_=Label(login_frame,text="OR",bg="white",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        #btn_forget=Button(login_frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)
        
        
        
        #========================Frame-2===================#
        register_frame=Frame(self.root,bd=2,relief=RIDGE)
        register_frame.place(x=720,y=570,width=350,height=60)
        
        
        lbl_reg=Label(register_frame,text="Sign up Here",font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)
        btn_signup=Button(register_frame,text="Sign Up",command=self.register,font=("times new roman",13,"bold"),bd=0,bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E",cursor="hand2").place(x=220,y=15)
        
    
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error', "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                
                
                if user==None:
                    messagebox.showerror("Error","Invalid Username/Password",parent=self.root)    
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
            
            
    def register(self):
        self.root.destroy()
        os.system("python register.py")  


root=Tk()
obj=Login_System(root)
root.mainloop()    