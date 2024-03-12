import tkinter as tk
import speedtest

root=tk.Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False, False)
root.config(bg="#1a212d")
            
def check_speed():
    test=speedtest.Speedtest()
    uploading=round(test.upload()/(1024*1024),2)
    downloading=round(test.download()/(1024*1024),2)
    
    servernames=[]
    test.get_servers(servernames)
    
    
    upload.config(text=uploading)
    download.config(text=downloading)
    DOWNLOAD.config(text=downloading)
    ping.config(text=test.results.ping)
    print("Ping :",test.results.ping)
    print("Upload :",uploading)
    print("Download :",downloading)

Top=tk.PhotoImage(file="top.png")
tk.Label(root,image=Top,bg="#1a212d").pack()


Main=tk.PhotoImage(file="main.png")
tk.Label(root,image=Main,bg="#1a212d").pack(pady=(40,0))

button=tk.PhotoImage(file="button.png")
Button=tk.Button(root,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=check_speed)
Button.pack(pady=10)


#Label

tk.Label(root,text="PING",font="arial 10 bold",bg="#384056",fg="#FF8000").place(x=50,y=0)
tk.Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056",fg="#FF8000").place(x=140,y=0)
tk.Label(root,text="UPLOAD",font="arial 10 bold",bg="#384056",fg="#FF8000").place(x=260,y=0)


tk.Label(root,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
tk.Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
tk.Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)



tk.Label(root,text="DOWNLOAD",font="arial 15 bold",bg="#384056",fg="white").place(x=130,y=280)
tk.Label(root,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

ping=tk.Label(root,text="00",font="arial 13 bold",bg="#1a212d",fg="white")
ping.place(x=70,y=60,anchor="center")

download=tk.Label(root,text="00",font="arial 13 bold",bg="#1a212d",fg="white")
download.place(x=180,y=60,anchor="center")

upload=tk.Label(root,text="00",font="arial 13 bold",bg="#1a212d",fg="white")
upload.place(x=290,y=60,anchor="center")

DOWNLOAD=tk.Label(root,text="00",font="arial 13 bold",bg="#1a212d",fg="white")
DOWNLOAD.place(x=180,y=350,anchor="center")


root.mainloop()
