import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")
app._min_height(400)
app._min_width(500)

def button_function():
    print("button pressed")

label = customtkinter.CTkLabel(master=app, text="Account")
textbox = customtkinter.CTkTextbox(app)

textbox2= customtkinter.CTKTextbox(app)

# textbox.place(in_=app, relx=0.2, rely=0.1,anchor=tkinter.N)
label.place(in_=app, relx=0.4,rely=0.4,anchor=tkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)





app.mainloop()