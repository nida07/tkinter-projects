from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def generate():
    lname=nent.get()
    rname=lent.get()
    flname=lname +".png"
    url=pyqrcode.create(rname)
    url.png(flname,scale=8)
    im=ImageTk.PhotoImage(Image.open(flname))
    imglb=Label(image=im)
    imglb.image=im
    cv.create_window(200,450, window=imglb)
cv=Canvas(root,bg="white",width="400",height="800")
cv.pack()
lb=Label(root,text="QR Code Generator",fg="#042c6b",bg="white",font=("Verdana",30))
cv.create_window(200,50,window=lb)
nlb=Label(root,text='Link Name',bg="white",fg="#080808")
llb=Label(root,text="Link",bg="white",fg="#080808")
cv.create_window(200,100,window=nlb)
cv.create_window(200,160,window=llb)
nent=Entry(root)
lent=Entry(root)
cv.create_window(200,130,window=nent)
cv.create_window(200,180,window=lent)
bt=Button(root,text="GENERATE",bg="#12a133",command=generate)
cv.create_window(200,240,window=bt)

root.mainloop()
