from unidecode import unidecode
from tkinter import filedialog
import tkinter
from pytube import YouTube, streams
import os
import tkinter as tk
import customtkinter
import subprocess
from pathlib import Path


def konvers(folder_path,file_name):
            na_co = '.mp3'
            input_file = os.path.join(folder_path, file_name+".mp4")
            output_file = os.path.join(folder_path, os.path.splitext(file_name)[0] + na_co)
            subprocess.call(['ffmpeg', '-i', input_file, output_file])
            if var2.get() == "off":
              os.remove(input_file)# do usuniecia

 
def get_yt(url, folder_path):
  yt = YouTube(url)
  ys = yt.streams.get_highest_resolution()
  file_name=yt.title
  file_name=unidecode(file_name.replace('"','').replace("|", "").replace("'","").lower())
  if var1.get()=='on':
    typ='.mp3'
  if var2.get()=='on':
    typ='.mp4'  
  try:
          if var1.get()=='on' and var2.get()=='on':
              ys.download(folder_path, filename=file_name+'.mp4')
              ys.download(folder_path, filename=file_name+'.mp3')
          ys.download(folder_path, filename=file_name+typ)
          my_label.configure(text='Udalo sie pobrac!')
  except:
          my_label.configure(text='blad poczas pobierania!')
 
def check_for_link():
    link = my_entry.get()
    if link=="":
     my_button1.configure(state=customtkinter.DISABLED, text_color='grey')
     my_label.configure(text= 'podaj link i podaj ponownie gdzie chcesz zapisac!')
    else:
     if var1.get() == "off" and var2.get() == "off":
           my_button1.configure(state=customtkinter.DISABLED, text_color='grey')
           my_label.configure(text= 'podaj typ pliku!') 
     else:
      my_button1.configure(state=customtkinter.NORMAL, text_color='red')  
        
def directory_USB():
    drive_name='muzyka'
    folder_exist=0
    global directory  
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        drive = f'{letter}:/'
        if os.path.exists(drive):
            directories = [d.lower() for d in os.listdir(drive)]  
            if drive_name in directories:
                directory = Path(drive) / drive_name
                print(f'Found {drive_name} in {drive}')
                folder_exist=1
                dir_button2.configure(fg_color=('blue','white'),text_color='black')
                dir_button3.configure(fg_color=('blue','white'),text_color='black')
            if folder_exist==1:
                dir_button4.configure(fg_color=('white','green'),text_color='red', text='znaleziono folder')
                check_for_link()
            else:
                dir_button4.configure(fg_color=('blue','white'),text_color='black' ,text='nie znaleziono foldera', font=('arial',10))
                check_for_link()
    
def directory_desktop():
  global directory
  directory = Path.home() / 'Desktop' 
  dir_button3.configure(fg_color=('white','green'),text_color='red')
  dir_button2.configure(fg_color=('blue','white'),text_color='black')
  dir_button4.configure(fg_color=('blue','white'),text_color='black')
  check_for_link()

def directory():
  global directory
  directory = filedialog.askdirectory()
  dir_button2.configure(fg_color=('white','green'),text_color='red')
  dir_button3.configure(fg_color=('blue','white'),text_color='black')
  dir_button4.configure(fg_color=('blue','white'),text_color='black')
  check_for_link()
    
def submit():
    get_yt(my_entry.get(), directory)  

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root=customtkinter.CTk()
root.title('Vivaldi-0.1')
root.geometry('550x250')
root.iconbitmap('C:\\Users\\Duszy\\Desktop\\DJ_naplet\\icon.ico')
my_entry=customtkinter.CTkEntry(root, placeholder_text='wklej link do Youtuba', width=500, font=('arial',16))
my_entry.pack(pady=15)

my_label=customtkinter.CTkLabel(root, text="Wybierz gdzie chcesz zapisac i wcisnij 'pobierz'")
my_label.pack(pady=15)


var1 = tk.StringVar()
my_checkbox1 = customtkinter.CTkCheckBox(root, text="mp3", variable=var1, onvalue="on", offvalue="off")
my_checkbox1.pack(side=tk.TOP, pady=1)
var1.set("on") 
var2 = tk.StringVar()
my_checkbox2=customtkinter.CTkCheckBox(root, text="mp4",variable=var2,onvalue="on", offvalue="off")
my_checkbox2.pack(side=tk.TOP,pady=1)
var2.set("off") 

my_button1=customtkinter.CTkButton(root, text='Pobierz', command=submit, text_color='grey', state=customtkinter.DISABLED)
my_button1.pack(side=tk.LEFT,pady=20)

dir_button2=customtkinter.CTkButton(root, text='wybierz folder', command=directory, fg_color=('blue','white'),text_color='black')
dir_button2.pack(side=tk.LEFT,pady=20)

dir_button3=customtkinter.CTkButton(root, text='zapisz na pulpit', command=directory_desktop, fg_color=('blue','white'),text_color='black')
dir_button3.pack(side=tk.LEFT,pady=20)

dir_button4=customtkinter.CTkButton(root, text='zapisz na USB', command=directory_USB, fg_color=('blue','white'),text_color='black')
dir_button4.pack(side=tk.LEFT,pady=20)


if __name__=='__main__':
    while True:
        root.mainloop()
