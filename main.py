import tkinter
from tkinter import *
from tkinter import messagebox,filedialog
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
import pytesseract as tess
from  PIL import Image ,ImageTk
from PIL import *
import webbrowser
import os



class Image_Reader(tk.Tk):
    
    
    def ask_directory(self):
      try:
        self.image_entry.delete(0,1000) 
        self.image_label_test=ImageTk.PhotoImage(Image.open((f"{self.home_directory}//test.png")).resize((600,400),resample=Image.LANCZOS)) 
        self.image_viewer.configure(width=600,height=400,image=self.image_label_test)
        self.image_location=f"{self.home_directory}\\test.png"
        self.raed_file=filedialog.askopenfilename(title="Image Reader Browser",filetypes=[("PNG Image", "*.png"),("JPG Image", "*.jpg")],)
        self.image_entry.insert(0,self.raed_file)
        self.image_label=ImageTk.PhotoImage(Image.open((self.raed_file)).resize((600,400),resample=Image.LANCZOS))
        self.image_viewer.configure(width=600,height=400,image=self.image_label)
      except:
          self.image_entry.insert(0,self.image_location)
    
    def read_image_text(self):
      try:
        if self.image_entry.get()=="" :
         messagebox.showwarning("Error","Search Image File To Read Text....")
        elif  self.all_lang.get()=="":
            messagebox.showwarning("Error","Select Language...")  
        else:
         self.read_text.delete("1.0","end")
         tess.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
         self.img=Image.open(self.raed_file)
         self.text=tess.image_to_string(self.img,lang=self.all_lang.get(),config='.')
         self.read_text.insert("1.0",self.text)
      except:
        if self.image_entry.get()=="" :
         messagebox.showwarning("Error","Search Image File To Read Text....")
        elif  self.all_lang.get()=="":
            messagebox.showwarning("Error","Select Language...")  
        else:
         self.read_text.delete("1.0","end")
         tess.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
         self.img=Image.open(self.image_entry.get())
         self.text=tess.image_to_string(self.img,lang=self.all_lang.get(),config='.')
         self.read_text.insert("1.0",self.text)
          
    def copy(self):
        import pyperclip
        pyperclip.copy(self.read_text.get("1.0","end"))
        spam = pyperclip.paste()
        messagebox.showinfo("Successfully","Copied Succefully..")
        return spam
    def open_git(self):
        webbrowser.open("https://github.com/KILLER-RAMADAN")
        
    def open_linked(self):
        webbrowser.open("https://www.linkedin.com/in/ahmed-ramadan-9b5a32221/")
        


    
    def __init__(self):
        
        super().__init__()
        
        
        
        self.home_directory = os.path.expanduser( '~' )
        print(self.home_directory)

        self.geometry("1080x550+250+100")
        self.title("Image Reader Program ")
        self.resizable(0,0)
        self.attributes("-topmost",True)
        self.iconbitmap("images//ico.ico")
        self.configure(bg="#121212")
        
        
        # filedialog to get image source #
        
        self.img1=tk.PhotoImage(file="images//read.png")
        self.img2=tk.PhotoImage(file="images//search.png")
        self.img3=tk.PhotoImage(file="images//copy.png")
        self.img4=tk.PhotoImage(file="images//linked.png")
        self.img5=tk.PhotoImage(file="images//git.png")
        
        
        
        
        
        # filedialog to get image source #
        
        
        
        self.image_entry=tk.Entry(width=57,relief="solid",font=("arial",20,"bold"))
        self.image_entry.place(x=5,y=10)
        
        self.image_button=tk.Button(text="Search Image",fg="white",image=self.img2,compound="left",background="#242526",width=0,font=("arial,10,bold"),command=self.ask_directory,bg="#242526",relief="solid",activebackground="#242526",activeforeground="white")
        
        self.image_button.place(x=910,y=10)
        
        self.frame = Frame(self, relief="solid",width=100, height=200)
        self.frame.pack()
        self.frame.place(anchor='center', x=310,y=320)
        
        self.image_viewer=tk.Label(self.frame,relief="solid",bd=0,width=70,height=15)
        self.image_viewer.pack()
        
        self.image_label_test=ImageTk.PhotoImage(Image.open(("images//test.png")).resize((600,400),resample=Image.LANCZOS)) 
        self.image_viewer.configure(width=600,height=400,image=self.image_label_test)
        
        self.img = Image.open(f"images\\test.png") 
        self. img = self.img .save(f"{self.home_directory}//test.png")
        
        
        
        
        
        self.read_text=tk.Text(self,bd=0,width=50,bg="#242526",fg="white",highlightbackground="black",relief="groove",highlightcolor="black",highlightthickness=2,height=20,font=("arial",12))
        self.read_text.place(anchor='center', x=850,y=303)
        
        
        self.read_text_button=tk.Button(text="Read Image",image=self.img1,fg="white",compound="left",width=0,font=("arial,10,bold"),command=self.read_image_text,bg="#242526",relief="groove",activebackground="#242526",activeforeground="white")
        
        self.read_text_button.place(x=930,y=500)
        
        self.copy_button=tk.Button(text="Copy Text",image=self.img3,fg="white",compound="left",width=0,font=("arial,10,bold"),command=self.copy,bg="#242526",relief="groove",activebackground="#242526",activeforeground="white")
        
        self.copy_button.place(x=780,y=500)
        
        # social buttons #
        
        self.git_button=tk.Button(image=self.img5,bd=0,font=("raial",20,"bold"),bg="#121212",fg="black",compound="left",command=self.open_git,activebackground="white",width=0)
        
        self.git_button.place(x=5,y=70)
        
        
        self.linked_button=tk.Button(image=self.img4,bd=0,font=("raial",20,"bold"),bg="#121212",compound="left",command=self.open_linked,activebackground="white",width=0)
        
        self.linked_button.place(x=60,y=70)
        # social buttons #
        
        
        # combo box to get lang #
        
        self.label_text=tk.Label(text="Select Lang:",bg="#121212",fg="white",font=("arial",10,"bold"))
        self.label_text.place(x=668,y=493)
        
        self.all_lang=ttk.Combobox(width=10,validate="focus",values=["ara","eng","rus","jpn"],font=("arial",10,"bold"))
        self.all_lang.place(x=670,y=515)
        self.all_lang.set("ara")
        
        # combo box to get lang #
        
        
        
        
        
        
        
app=Image_Reader()

app.mainloop()





