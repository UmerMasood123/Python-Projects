#Our Team Members
''' 1.Umer Bin Masood
    2.Muhammad Hassan
    3.Talha
'''
from tkinter import *
import speedtest 


def speedcheck():
	sp = speedtest.Speedtest()
	sp.get_servers()
	down = str(round(sp.download()/(10**6),3))+"Mbps"
	up = str(round(sp.upload()/(10**6),3))+"Mbps"
	lab_down.config(text=down)
	lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="blue")
sp.resizable(False,False)

lab = Label(sp, text="Internet Speed Test ", font=("Arial", 30, "bold", "underline"), bg="blue", fg="#fff")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed ", font=("Arial", 30, "bold"), bg="blue")
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Arial", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed  ", font=("Arial", 30, "bold"), bg="blue")
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Arial", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Arial", 30, "bold"), relief=RAISED, bg="red", command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

lab_t = Label(sp, text="Product of : Umer Bin Masood, Muhammad Hassan, Talha", font=("Arial", 10, "bold"), bg="blue", fg="#fff")
lab_t.place(x=110, y=530, height=50, width=380)



sp.mainloop()