import customtkinter as ctk

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tempereature Conversion App")
        self.geometry("400x250")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.configure(fg_color="#9fe1d9")
        
        self.label = ctk.CTkLabel(self, text="Temperature Conversion Program" , text_color="#1d3759" , font=("Algerian", 30, "bold"))
        self.label.pack(pady=50)
        
        self.mainframe = ctk.CTkFrame(self,width=900,height=450,corner_radius=10,border_width=2,border_color="black", fg_color= "#c8b37b" )
        self.mainframe.pack(pady=50)
        
        self.inputLabel = ctk.CTkLabel(self.mainframe,text="Enter temperature :" , text_color= "black",font=("Arial Rounded MT Bold",18))
        self.inputLabel.place(x=150,y=50)
        self.input = ctk.CTkEntry(self.mainframe,width=200,height=30,border_width=2,border_color="#5c7774",placeholder_text="example 210" , font=("Product Sans",15))
        self.input.place(x=330,y=50)
        
        self.tempType = ctk.CTkComboBox(self.mainframe,width=150,height=30,values=["Celsius (°C)","Fahrenheit (°F)","Kelvin (K)"] , border_color="gray",dropdown_font=("Arial Rounded MT Bold", 15),dropdown_fg_color="#717cb0")
        self.tempType.place(x=550,y=50)
        self.tempType.set("Celsius (°C)")
        
        # OUTPUT SECTION
        
        self.celsiusLabel = ctk.CTkLabel(self.mainframe,text="Celsius (°C):" , text_color= "black",font=("Arial Rounded MT Bold",18))
        self.celsiusLabel.place(x=150,y=150)
        self.celsius = ctk.CTkEntry(self.mainframe,state="readonly",width=200,height=30,border_width=2,border_color="#5c7774",text_color="black")
        self.celsius.place(x=330,y=150)
    
        self.fahrenheitLabel = ctk.CTkLabel(self.mainframe,text="Fahrenheit (°F) :" , text_color= "black",font=("Arial Rounded MT Bold",18))
        self.fahrenheitLabel.place(x=150,y=200)
        self.fahrenheit = ctk.CTkEntry(self.mainframe,state="readonly",width=200,height=30,border_width=2,border_color="#5c7774")
        self.fahrenheit.place(x=330,y=200)
        
        self.kelvinLabel = ctk.CTkLabel(self.mainframe,text="Kelvin (K) :" , text_color= "black",font=("Arial Rounded MT Bold",18))
        self.kelvinLabel.place(x=150,y=250)
        self.kelvin = ctk.CTkEntry(self.mainframe,state="readonly",width=200,height=30,border_width=2,border_color="#5c6277")
        self.kelvin.place(x=330,y=250)
        
        self.convertButton = ctk.CTkButton(self.mainframe, text="CONVERT", text_color="white", fg_color="#3f5294", corner_radius=5,hover_color="#1335c0",font=("Arial Rounded MT Bold",15),command=self.convert)
        self.convertButton.place(x=270,y=350)
        
        self.resetButton = ctk.CTkButton(self.mainframe, text="RESET", text_color="white", fg_color="#3f5294", corner_radius=5,hover_color="#1335c0",font=("Arial Rounded MT Bold",15),command=self.clear)
        self.resetButton.place(x=470,y=350)
        print(self.tempType.get())
        
        self.C=""
        self.F=""
        self.K=""
            
    def convert(self):
        self.celsius.configure(state="normal")
        self.fahrenheit.configure(state="normal")
        self.kelvin.configure(state="normal")
        self.celsius.delete(0,"end")
        self.fahrenheit.delete(0,"end")
        self.kelvin.delete(0,"end")
        
        if self.tempType.get()=="Celsius (°C)":
            C=int(self.input.get())
            F=(C*(9/5))+32
            K=C+273.15
            self.C=str(C)+"°C"
            self.F=str(F)+"°F"
            self.K=str(K)+"K"
            
        if self.tempType.get()=="Fahrenheit (°F)":
            F=int(self.input.get())
            C=(F-32)*(5/9)
            K=(F-32)*(5/9)+273.15
            self.C=str(C)+"°C"
            self.F=str(F)+"°F"
            self.K=str(K)+"K"
        
        if self.tempType.get()=="Kelvin (K)":
            K=int(self.input.get())
            F=(K-273.15)*(9/5)+32
            C=K-273.15
            self.C=str(C)+"°C"
            self.F=str(F)+"°F"
            self.K=str(K)+"K"
        
        self.celsius.insert(0,self.C)
        self.fahrenheit.insert(0,self.F)
        self.kelvin.insert(0,self.K)
        
        self.celsius.configure(state="readonly")
        self.fahrenheit.configure(state="readonly")
        self.kelvin.configure(state="readonly")
        
    def clear(self):
        self.celsius.configure(state="normal")
        self.fahrenheit.configure(state="normal")
        self.kelvin.configure(state="normal")
        
        self.input.delete(0,"end")
        self.celsius.delete(0,"end")
        self.fahrenheit.delete(0,"end")
        self.kelvin.delete(0,"end")
        
        self.celsius.configure(state="readonly")
        self.fahrenheit.configure(state="readonly")
        self.kelvin.configure(state="readonly")
        
if __name__ == "__main__":
    app = MyApp()
    app._state_before_windows_set_titlebar_color = "zoomed"
    app.mainloop()
