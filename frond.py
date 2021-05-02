from tkinter import * 
import PIL 
from PIL import ImageTk, Image
from tkinter import Canvas
from pytube import YouTube
import requests
import os 
import time
import tkinter
import PIL.Image
import io
import urllib.request
import tkinter as tk
from PIL import Image
from tkinter import ttk
from back import Download_completo
import back as lista_calidad
from pytube import *
from tkinter import filedialog
import back

class Perro:
    def __init__(self):
        self.root = Tk()
        self.root.title("Youtube Download")
        icono = ("youtube_icono.ico")
        ico_root = tk.PhotoImage(file=icono)
        self.root.iconphoto(True, ico_root)
        self.root.geometry("600x300")
        self.c_size = (320,180)

        self.setup(self.c_size)

        #self.root.mainloop()
        #self.backend_obj = backend_obj


    def setup(self, s):
        self.var = StringVar()
        self.var_2 = StringVar()
    
        self.cava = Canvas(self.root, height=s[1], width=s[0],
			bg='black',bd=10,relief='ridge')
        self.caja_tipo_codec = ttk.Combobox(self.root, value=["MP4", "WEBM", "AUDIO"])
        self.caja_tipo_codec.set("Formato")
        self.caja_tipo_codec['state'] = 'readonly'

        self.combo = ttk.Combobox (self.root, width= 35, postcommand = self.seleccion) 
        self.combo['state'] = 'readonly'
        self.combo.set('Calidad')
        self.combo.grid(row=0, column=2)
        
        self.guardado = Entry(self.root, width=30, text=self.var_2)
        self.boton_descarga = Button(self.root, text='DESCARGAR', width=15, height=2 , command=self.boton_de_descarga)
        self.boton_save = Button(self.root, text = 'GUARDAR...', command=self.boton_de_guardado)
   
        
        texto = Label(self.root, text='LINK:')
        texto.grid()
        self.guardado.grid(column=1)
       
        link = Entry(self.root, width=55, textvariable=self.var)
        self.var.trace("w", self.miniatura_cava)
        self.var.trace("w", self.lista_del_resolucion_con_el_link_mp4)
        self.var.trace("w", self.lista_del_resolucion_con_el_link_webm)
     
        
        link.grid()
        self.cava.grid()
        self.guardado.grid()
        self.boton_descarga.grid()
        self.boton_save.grid()
        self.caja_tipo_codec.grid()
        self.guardado.config(state=DISABLED)
        self.guardado.place(y=250, x=370)
        self.boton_save.place(y=200, x=430)
        self.boton_descarga.place(y=250, x=125)
        self.caja_tipo_codec.place(x=350, y=20)
        self.combo.place(x=350, y=60)
        



    def miniatura_cava(self, *args):

        obj = self.var.get()
        tmp_directory = os.path.join(os.getcwd(), 'tmp')

        if len(obj) >= 1: 
            yt = YouTube(obj)
            cs = yt.thumbnail_url
            myfile = requests.get(cs)
            casa = open('tmp/PythonImage.jpg', 'wb').write(myfile.content)
            self.pilmage = Image.open('tmp/PythonImage.jpg')
            re = self.pilmage.resize((320,180),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.cava.delete(ALL)
            self.cava.create_image(self.c_size[0]/2+10, self.c_size[1]/2+10, anchor=CENTER, image=self.img)

        elif len(obj) == 0:
            self.cava.delete(ALL)
            os.remove("tmp/PythonImage.jpg")


    def lista_del_resolucion_con_el_link_mp4(self, st, *args):
        res = self.var.get()
        self.super_calidad = Download_completo()
        self.back_resolucion = self.super_calidad.lista_calidad_mp4(res)

    def lista_del_resolucion_con_el_link_webm(self, s, *args):
        res_webm = self.var.get()
        self.new_webm = Download_completo()
        self.back_resolucion_webm = self.new_webm.lista_calidad_webm(res_webm)

    def seleccion(self):
        now = self.caja_tipo_codec.get()
        if (combo_sel:= self.caja_tipo_codec.get()) == "MP4":
            self.combo.config(value=self.back_resolucion)
            

        elif (combo_sel:= self.caja_tipo_codec.get()) == "WEBM":
            self.combo.config(value=self.back_resolucion_webm)

        elif  (combo_sel:= self.caja_tipo_codec.get()) == "AUDIO":
            self.combo.config(value="MP3")

          
        link = self.var.get()
        if len(link) == 0:
                self.combo.config(value="")
                self.combo.set("Calidad")

        else:
            removedor = os.remove("tmp/PythonImage.jpg")
            


    def boton_de_descarga(self):
        link_descarga = self.var.get()
        resolucion_mp4 = self.combo.get()
        guardado = self.var_2.get()
        codec = self.caja_tipo_codec.get()

        if codec == "MP4":
            codec_mp4 = "mp4"
            down_final = Download_completo()
            down_final.download_intento(link_descarga, resolucion_mp4, codec_mp4, guardado)

        elif codec == "WEBM":
            codec_webm = "webm"
            down_final = Download_completo()
            down_final.download_intento(link_descarga, resolucion_mp4, codec_webm, guardado)

        elif  codec == "AUDIO":
            codec_mp3 = "mp3"
            audio_mp3 = Download_completo()
            audio_mp3.audio(link_descarga, guardado)


        

    def boton_de_guardado(self):
        self.var_2.set(filedialog.askdirectory())


    def run(self):
        self.root.mainloop()


if __name__ ==  '__main__':
    fron = Perro()
    fron.run()





        


