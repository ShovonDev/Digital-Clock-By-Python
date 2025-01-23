from tkinter import *
import datetime
import calendar

root = Tk()
root.configure(bg='#d4c5ad')
root.geometry('700x600')
root.resizable(0, 0)
root.title('Python Clock with Calendar')

# Clock section
Label(root, text='Digital Clock', font='Bruce 20 bold').pack(side=TOP, pady=10)

def clock():
    now = datetime.datetime.now()
    date = now.strftime("%A, %d-%b-%Y")
    time = now.strftime("%I:%M:%S %p")
    date_label.config(text=date)
    time_label.config(text=time)
    time_label.after(1000, clock)

date_label = Label(root, font="calibri 30 bold", foreground='#FFFFFF', background='black')
date_label.pack(anchor='center', pady=5)
time_label = Label(root, font="calibri 60 bold", foreground='#6CA0DC', background='black')
time_label.pack(anchor='center', pady=5)

# Calendar section
Label(root, text='Calendar', font='Bruce 20 bold').pack(side=TOP, pady=10)

def show_calendar():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day

    cal = calendar.TextCalendar().formatmonth(current_year, current_month)
    calendar_text.delete(1.0, END)  # Clear existing text
    calendar_text.insert(END, cal)

    # Highlight the current day
    lines = cal.splitlines()
    for i, line in enumerate(lines):
        if f"{current_day:2}" in line.split():  # Find the current day in the calendar
            start_index = line.index(f"{current_day:2}")
            calendar_text.tag_add("highlight", f"{i + 1}.{start_index}", f"{i + 1}.{start_index + 2}")
            break

    calendar_text.tag_config("highlight", background="yellow", foreground="red")

calendar_text = Text(root, font="Courier 12", height=8, width=20, bg='#d4c5ad', fg='black', bd=0, wrap=NONE)
calendar_text.pack(anchor='center', pady=10)

show_calendar()
clock()
root.mainloop()
