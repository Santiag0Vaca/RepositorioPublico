import customtkinter as ctk
import PIL
from PIL import Image,ImageTk

ventana=ctk.CTk()
ventana.geometry("700x400")
ventana.title("Micro Numero")
######
ctk.set_appearance_mode("dark")
######
rectangulo_cafe = ctk.CTkFrame(master=ventana, corner_radius=0, fg_color="#392823")
rectangulo_cafe.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)

rectangulo_azul = ctk.CTkFrame(master=ventana, corner_radius=0, fg_color="#052D37")
rectangulo_azul.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

etiqueta1=ctk.CTkLabel(ventana, text="                          Bus numero", fg_color="transparent", font=("Comic Sans", 25), anchor="w")
etiqueta1.place(relx=0, rely=0.2)

etiqueta2=ctk.CTkLabel(ventana, text="""              -Mercado Central
-La loma
    -Exterminal""", fg_color="transparent", font=("Comic Sans", 25), anchor="w")
etiqueta2.place(relx=0, rely=0.6)




ventana.mainloop()