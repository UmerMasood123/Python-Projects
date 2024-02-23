#Our Team Members
''' 1.Umer Bin Masood
    2.Muhammad Hassan
    3.Talha
'''
from tkinter import *
import os

def restart():
	os.system("shutdown /r /t 1")
def restart_time():
	os.system("shutdown /r /t 20")
def logout():
	os.system("shutdown -1")	
def shutdown():
	os.system("shutdown /s /t 1")


st = Tk()
st.geometry("500x450")
st.title("Shutdown App")
st.config(bg="blue")
st.resizable(False,False)

label = Label(st, text="Power Buttons Action", font=("Arial", 25, "bold", "underline"), fg="#ffffff", bg="#0000ff")
label.place(x=60,y=5, width=380, height=60)

st_button = Button(st, text="Shutdown", font=("Arial", 25, "bold"), cursor="plus", bg="#bbdbff", fg="#0079ff", command=shutdown)
st_button.place(x=60,y=80, width=380, height=60)

r_button = Button(st, text="Restart", font=("Arial", 25, "bold"), cursor="plus", bg="#bbdbff", fg="#0079ff", command=restart)
r_button.place(x=60,y=160, width=380, height=60)

rt_button = Button(st, text="Restart Time", font=("Arial", 25, "bold"), cursor="plus", bg="#bbdbff", fg="#0079ff", command=restart_time)
rt_button.place(x=60,y=240, width=380, height=60)

lg_button = Button(st, text="Log Out", font=("Arial", 25, "bold"), cursor="plus", bg="#bbdbff", fg="#0079ff", command=logout)
lg_button.place(x=60,y=320, width=380, height=60)

n_label = Label(st, text="Group Members: Umer Bin Masood, Muhammad Hassan, Talha ", font=("Arial", 10, "underline"), fg="#ff0000" ,bg="#0000ff")
n_label.place(x=110,y=420)

st.mainloop()