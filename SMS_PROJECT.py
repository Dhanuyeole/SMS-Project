#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from tkinter import*
from tkinter import messagebox #used for message display
from tkinter import ttk #is used for combobox,scrollbar,treeview
win=Tk()
win.title('Student Management System')
win.iconbitmap('coding.ico')
win.minsize(width=800,height=600)
win.configure(bg='skyblue')

#functions
def show():
    conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
    mycur=conn.cursor()
    mycur.execute("select* from pro1t")
    result=mycur.fetchall()
    for i in result:
        treev.insert("",'end',values=(i[0],i[1],i[2],i[3]))
        
def add():
    global n1
    global m1
    global d1
    global e1
    
    name=n1.get()
    mob=m1.get()
    dept=d1.get()
    email=e1.get()
    
    if(name=="" or mob=="" or dept=="" or email==""):
        messagebox.showinfo('stu info','all filed are required to fill')
    else:
        conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
        qur1="INSERT INTO pro1t(name,mobno,dept,emailid) VALUES('%s','%s','%s','%s')"%(name,mob,dept,email)
        mycur=conn.cursor()
        mycur.execute(qur1)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('stu info','info succesfully submitted')
        n1.set('')
        m1.set('')
        d1.set('')
        e1.set('')
                
def result():
    root=Tk()
    root.configure(bg='white')
    root.title('Result')
    root.geometry('500x400')
    def disp():
         reldata=relent.get()
            
         if reldata=='':
            messagebox.showinfo("student info","all fields are required to fill")
         else:
            conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
            qur1="SELECT mobno from pro1t where name='%s'"%(reldata)
            mycur=conn.cursor()
            mycur.execute(qur1)
            result=mycur.fetchone()
            new.config(text='marks='+result[0]+'%')
        
            relent.delete(0,'end')
    resl=Label(root,text="Enter the name of student :",height=2,font="Cooper  8 bold",fg="black",bg="white")
    resl.place(x=10,y=40)
    
    rc=StringVar()
    relent=Entry(root,bg='white',fg='black',width=30,bd=5,textvariable=rc,font=('times new roman',14))
    relent.place(x=200,y=40)
    relbtn=Button(root,text='Show Result',width=20,command=disp)
    relbtn.place(x=200,y=90)
    
    new=Label(root,text="MARKS :",height=10,width=40,font="Cooper  8 bold",fg="black",bg="skyblue")
    new.place(x=10,y=200)        
    resl=Label(root,text='Enter the name of student',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
    resl.place(x=10,y=40)
    relent=Entry(root,bd=5,fg='black',width=40,bg='white',textvariable=rc,font=('times new roman',12,'bold'))
    relent.place(x=200,y=40)
    relbtn=Button(root,text='Show result',width=20,command=disp)
    relbtn.place(x=200,y=90)

    root.mainloop()

def delete():
    global tt
    rs=tt.get()
    if rs=="":
        messagebox.showinfo('stu info','all filed are required to fill')
    else:
        conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
        qur1="DELETE FROM pro1t WHERE name='%s'"%(rs)
        mycur=conn.cursor()
        mycur.execute(qur1)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('stu info','Record Deleted')
        tt.set('')
def select():
    global up
    upd=up.get()
    if upd=="":
        messagebox.showinfo('stu info','all filed are required to fill')
    else:
        conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
        qur1="SELECT * from pro1t where name='%s'"%(upd)
        mycur=conn.cursor()
        mycur.execute(qur1)
        result=mycur.fetchall()
        for i in result:
            ent2.insert(0,i[0])
            ent3.insert(0,i[1])
            ent4.insert(0,i[2])
            ent5.insert(0,i[3])
        up.set('')
            
def update():
    global n1
    global m1
    global d1
    global e1
    
    name=n1.get()
    mob=m1.get()
    dept=d1.get()
    email=e1.get()
    
    if(name=="" or mob=="" or dept=="" or email==""):
        messagebox.showinfo('stu info','all filed are required to fill')
    else:
        conn=mysql.connector.connect(user='root',password='Dhanu@0211',host='localhost',database='data11')
        qur1="UPDATE pro1t SET mobno='%s',dept='%s',emailid='%s' where name='%s'"%(mob,dept,email,name)
        mycur=conn.cursor()
        mycur.execute(qur1)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('stu info','info updated')
        n1.set('')
        m1.set('')
        d1.set('')
        e1.set('')
                
    

def clear():
    treev.delete(*treev.get_children())
    
n1=StringVar()
m1=StringVar()
d1=StringVar()
e1=StringVar()
tt=StringVar()
up=StringVar()
rc=StringVar()


#labels
lbl1=Label(win,text='Student Managment System',relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',16,'bold'))
lbl1.place(x=268,y=40)

lbl2=Label(win,text='Name',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl2.place(x=190,y=100)
ent2=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=n1,font=('times new roman',12,'bold'))
ent2.place(x=385,y=100)

lbl3=Label(win,text='Mobile Number',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl3.place(x=190,y=140)
ent3=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=m1,font=('times new roman',12,'bold'))
ent3.place(x=385,y=140)

lbl4=Label(win,text='Department',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl4.place(x=190,y=180)
ent4=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=d1,font=('times new roman',12,'bold'))
ent4.place(x=385,y=180)

lbl5=Label(win,text='Email',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl5.place(x=190,y=220)
ent5=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=e1,font=('times new roman',12,'bold'))
ent5.place(x=385,y=220)

lbl6=Label(win,text='Delete by name',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl6.place(x=190,y=400)
ent6=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=tt,font=('times new roman',12,'bold'))
ent6.place(x=385,y=400)

lbl7=Label(win,text='Update by name',width=20,relief='ridge',bd=5,fg='black',bg='white',font=('times new roman',12,'bold'))
lbl7.place(x=190,y=520)
ent7=Entry(win,bd=5,fg='black',width=40,bg='white',textvariable=up,font=('times new roman',12,'bold'))
ent7.place(x=385,y=520)

#Buttons
shwbtn=Button(win,text='SHOW',width=20,command=show)
shwbtn.place(x=200,y=320)

addbtn=Button(win,text='ADD',width=20,command=add)
addbtn.place(x=500,y=320)

exbtn=Button(win,text='EXIT',width=20,command=win.destroy)
exbtn.place(x=200,y=360)

restbtn=Button(win,text='RESULT',width=20,command=result)
restbtn.place(x=500,y=360)

delbtn=Button(win,text='Delete',width=20,command=delete)
delbtn.place(x=300,y=440)

upbtn=Button(win,text='Update',width=20,command=update)
upbtn.place(x=460,y=560)

selbtn=Button(win,text='Select',width=20,command=select)
selbtn.place(x=300,y=560)

#Treeview
treev=ttk.Treeview(win,selectmode='browse',height=20)
treev.place(x=900,y=100,width=450)

verscrlbar=ttk.Scrollbar(win,orient="vertical",command=treev.yview)
verscrlbar.pack(side='right',fill='x')
treev.configure(xscrollcommand=verscrlbar.set)

treev["columns"]=("1","2","3","4")
treev['show']='headings'
treev.column("1",width=90,anchor='c')
treev.column("2",width=90,anchor='se')
treev.column("3",width=90,anchor='se')
treev.column("4",width=90,anchor='se')

treev.heading("1",text="Name")
treev.heading("2",text="Mobaile No")
treev.heading("3",text="Dept")
treev.heading("4",text="EmailID")

clearbtn=Button(win,text='clear',width=20,command=clear).place(x=1080,y=560)

win.mainloop()


# In[ ]:




