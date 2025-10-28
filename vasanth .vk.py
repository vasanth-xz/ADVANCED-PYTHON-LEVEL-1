from tkinter import *

root=Tk()
root.title("BCA APPS")
root.geometry("200x500")

f1=Frame(root)
f1.config(bg="Red")
f1.pack(fill=BOTH,expand=True)

l1=Label(f1,text="TAKSHASHILA UNIVERSITY",bg="RED",fg="YELLOW",font=("Arial",25,"bold"))
l1.pack()

l2=Label(f1,text="ONGUR,TINDIVANAM,VILLUPURAM DISTRICT",bg="RED",fg="YELLOW",font=("Arial",25,"bold"))
l2.pack()

f2=Frame(root)
f2.config(bg="pink")
f2.pack(fill=BOTH,expand=True)

l3=Label (f2,text="STUDFENT INFORMATION")
l3.pack()

l4=Label (root, text="ENROLLMENT ID")
l4.pack()

e=Entry(root)
e.pack()

l5=Label(root,text="NAME OF THE STUDENT")
l5.pack()

e=Entry(root)
e.pack()

l6=Label (root, text="DATE OF BIRTH")
l6.pack()

e=Entry (root)
e.pack()

l7=Label(root,text="ADDERESS FOR COMMUNICATION")
l7.pack()

e=Entry (root)
e.pack()

l8=Label (root,text="PHONE NO")
l8.pack()

e=Entry (root)
e.pack()

root.mainloop()
