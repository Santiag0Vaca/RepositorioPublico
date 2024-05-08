import customtkinter as ctk
import PIL
from PIL import Image,ImageTk

ventana=ctk.CTk()
ventana.geometry("5000x500")
ventana.title("Ruta de micros")
######
ctk.set_appearance_mode("dark")
######

rectangulo_azul = ctk.CTkFrame(master=ventana, corner_radius=0, fg_color="#052D37")
rectangulo_azul.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

rectangulo_cafe = ctk.CTkFrame(master=ventana, corner_radius=0, fg_color="transparent")
rectangulo_cafe.place(relx=0, rely=0, relwidth=1, relheight=0.1)

minirectangulo_cafe = ctk.CTkFrame(master=ventana, corner_radius=0,)
minirectangulo_cafe.place(relx=0.7, rely=0.099, relwidth=0.3, relheight=0.08)

boton_segmentado = ctk.CTkSegmentedButton(ventana, values=["Buses", "Trufis"])
boton_segmentado.place(relx=0.75, rely=0.12, relwidth=0.2, relheight=0.04)
boton_segmentado.set("Buses")

bus_numero = "Bus Numero"

boton1=ctk.CTkButton(ventana,text="            M. Campesino", fg_color= "#392823", font=("Comic Sans", 25), corner_radius=100)
boton1.place(relx=0.725, rely=0.23, relwidth=0.25, relheight=0.1)
boton2=ctk.CTkButton(ventana,text="            M. La Loma", fg_color= "#392823", font=("Comic Sans", 25), corner_radius=100)
boton2.place(relx=0.725, rely=0.38, relwidth=0.25, relheight=0.1)
boton3=ctk.CTkButton(ventana,text="            M. Central", fg_color= "#392823", font=("Comic Sans", 25), corner_radius=100)
boton3.place(relx=0.725, rely=0.53, relwidth=0.25, relheight=0.1)
boton4=ctk.CTkButton(ventana,text="            P. Bolivar", fg_color= "#392823", font=("Comic Sans", 25), corner_radius= 100)
boton4.place(relx=0.725, rely=0.68, relwidth=0.25, relheight=0.1)
boton5=ctk.CTkButton(ventana,text="            B. Juan XXIII", fg_color= "#392823", font=("Comic Sans", 25), corner_radius= 100)
boton5.place(relx=0.725, rely=0.83, relwidth=0.25, relheight=0.1)

etiqueta=ctk.CTkLabel(ventana, text="   Micro 9", fg_color="transparent", font=("Comic Sans", 55), anchor="w")
etiqueta.place(relx=0.700, rely=0, relwidth=10, relheight=0.1)

ventana.mainloop()
ventana.mainloop()
