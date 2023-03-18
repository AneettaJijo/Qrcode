from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    filename=link_name + ".png"
    url=pyqrcode.create("link")
    url.png(filename,scale=8)
    img=ImageTk.PhotoImage(Image.open(filename))
    image_label=Label(image=img)
    image_label.image=img
    canvas1.create_window(200,450,window=image_label)


canvas1=Canvas(root,width=400,height=600)
canvas1.pack()
app=Label(root,text="QR CODE GENERATOR",fg="brown",font=('arial=50'))
canvas1.create_window(200,50,window=app)
link_name=Label(root,text="Link name")
link=Label(root,text="Link")
canvas1.create_window(200,100,window=link_name)
canvas1.create_window(200,200,window=link)

name_entry=Entry(root)
link_entry=Entry(root)
canvas1.create_window(200,130,window=name_entry)
canvas1.create_window(200,230,window=link_entry)

b1=Button(text="To generate QR code",command=generate)
canvas1.create_window(200,300,window=b1)
root.mainloop()
