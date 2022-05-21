import tkinter
from tkinter import *
from applescript import tell
import os
from tkinter import messagebox
import subprocess


WINDOW_SIZE = "300x200"
root = tkinter.Tk()
root.title('FLUSHI v1.0')
root.geometry(WINDOW_SIZE)

def helloCallBack(pwd):
   command = 'echo '+str(pwd)+' | sudo -S killall -HUP mDNSResponder;sudo killall mDNSResponderHelper;sudo dscacheutil -flushcache'
   command2 = 'echo '+str(pwd)+' | sudo -S killall -HUP mDNSResponder;sudo killall mDNSResponderHelper;sudo dscacheutil -flushcache'
   list = [command, command2]
   for i in list:
      result = subprocess.getoutput(i)
      print("HOLA "+str(result))
   print(result)
   if "No matching processes were found" in result:
      tkinter.messagebox.showinfo("FLUSHI", "FLUSH HAS BEEN DONE \n YOU ARE GOOD TO GO")
   else:
      tkinter.messagebox.showinfo("FLUSHI", "ERROR \n PLEASE CHECK YOUR PASSWORD")


def show():
   pwd = password.get()  # get password from entry
   print(pwd)
   helloCallBack(pwd)

def byeClick():
   tkinter.messagebox.showinfo("FLUSHI", "BYE THANK YOU FOR USING FLUSHI")
   root.destroy()
   os.system("""osascript -e 'tell application "Terminal" to quit'""")

label= Label(root, text="TYPE YOUR ROOT PASSWORD", font= ('Helvetica 13 bold'))
label.pack(pady=20)
password = StringVar() #Password variable
passEntry = Entry(root, textvariable=password, show='*')
submit = Button(root, text='FLUSH DNS',command=show)


passEntry.pack()
submit.pack()
quit = tkinter.Button(root, text ="QUIT", command = byeClick)
quit.pack()



termf = Frame(root, height=100, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()



root.mainloop()