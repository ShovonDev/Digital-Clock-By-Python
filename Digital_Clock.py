from tkinter import*
import datetime


root=Tk() 
root.configure(bg='#d4c5ad')
root.geometry('700x400')
root.resizable(0,0)
root.title('Python Clock')
Label(root,text='Digital Clock', font='Bruce 20 bold').pack(side=TOP)



def clock():
     date_time=datetime.datetime.now().strftime( "%A:%d-%b-%Y %I:%M:%S%p")
     date,time= date_time.split()
     time_label.config(text=time)
     date_label.config(text=date)
     time_label.after(1000, clock)
    
    
    
    
time_label=Label(root, font ="calibri 60 bold", foreground='#6CA0DC',background='black')  
time_label.pack(anchor='center')
date_label= Label(root, font="calibri 30 bold", foreground='#FFFFFF', background='black')
date_label.pack(anchor='s') 
    
    
clock()
root.mainloop()    
         